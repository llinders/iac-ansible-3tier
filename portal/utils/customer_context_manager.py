""" Customer Context Manager

Holds customer data in memory and synchronized customer data with persistent storage.
Acts as a facade to simplify customer data management and persistent storage synchronization.
This manager class is also used to simplify environment deployments, since it is responsible for updating in-memory and
persistent data of deployed environments.

"""

import vagrant
from domain.customer import Customer
from domain.prod_environment import ProductionEnvironment
from domain.test_environment import TestEnvironment
from .deployment.customer_env_dir_builder import build_customer_env_dir
import utils.data.customer_data_utils as cdu

import utils.data.customer_data_utils as cdu
import utils.data.ip_data_utils as idu
import utils.deployment.deployment_file_handler as dfh


class CustomerContextManager:
    __customer: Customer
    
    def __init__(self, customer_number: int):
        if (customer_number <= 0):
            return
        self.load(customer_number)


    def load(self, customer_number: int) -> None:
        if not (cdu.check_if_exists(customer_number)):
            raise Exception(f'Customer with customer number {customer_number} does not exist')
        
        customer_data = cdu.get_customer(customer_number)

        # Initialize prod environment domain object
        prod_env_data = customer_data['prod_env_setup']
        prod_env = ProductionEnvironment(
            files_prepared=prod_env_data['files_prepared'],
            deployed=prod_env_data['deployed'],
            loadbalancer_ip=prod_env_data['loadbalancer_ip'],
            database_ip=prod_env_data['database_ip'],
            webserver_ips=prod_env_data['webservers']
            )
        
        # Initialize test environment domain object
        test_env_data = customer_data['test_env_setup']
        test_env = TestEnvironment(
            files_prepared=test_env_data['files_prepared'],
            deployed=test_env_data['deployed'],
            database_ip=test_env_data['database_ip'],
            webserver_ip=test_env_data['webserver_ip']
            )

        # Initialize customer domain object
        self.__customer = Customer(
            customer_number=customer_number, 
            username=customer_data['username'], 
            prod_env=prod_env,
            test_env=test_env
            )
        
    def create_and_load_new_customer(self, username: str) -> None:
        self.load(cdu.write_new_customer(username))

    def deploy_test_environment(self) -> None:
        """
        Acts as a facade method to create a new customer test deployment directory, modify j2 templates, 
        copy files and update customer data.
        When Ansible and Vagrant files are prepared a prompt is given which allows the user to chose to deploy to vagrant.
        """
        if self.__customer.test_env.deployed:
            raise Exception('Test environment is already deployed, cannot deploy multiple test environments')
        
        if not (self.__customer.test_env.files_prepared):
            print('Preparing environment files...')

            webserver_ip, database_ip = idu.find_next_available_ips(2)[:2]
            
            dfh.prepare_test_env_files(self.get_customer_number(), webserver_ip, database_ip)

            # Update domain model and write to persistent storage
            self.__customer.test_env.files_prepared = True
            self.__customer.test_env.webserver_ip = webserver_ip
            self.__customer.test_env.database_ip = database_ip
            idu.remove_ips([webserver_ip, database_ip])

            self.__persist_customer_data()
        else:
            print('Environment files are already prepared')

        deploy_to_vagrant = input('Do you want to deploy to vagrant right now? (Y/N): ')
        if (deploy_to_vagrant.lower() == 'y'):
            raise NotImplementedError

    def delete_test_environment(self) -> None:
        dfh.delete_test_environment(self.get_customer_number())
        idu.add_ips([self.__customer.test_env.webserver_ip, self.__customer.test_env.database_ip])

    def deploy_prod_environment(self, number_of_webservers: int) -> None:
        """
        Acts as a facade method to create a new customer production deployment directory, modify j2 templates, 
        copy files and update customer data.
        When Ansible and Vagrant files are prepared a prompt is given which allows the user to chose to deploy to vagrant.
        """
        if 1 < number_of_webservers <= 5:
            raise ValueError("Number of webservers must be a minimum of 1 and maximum of 5")
        if self.__customer.prod_env.deployed:
            raise Exception("Production environment is already deployed, cannot deploy multiple production environments")
        
        if not (self.__customer.prod_env.files_prepared):
            print('Preparing environment files...')

            ip_list = idu.find_next_available_ips(2 + number_of_webservers)
            loadbalancer_ip, database_ip = ip_list[:2]
            webserver_ips = ip_list[2:]
            
            dfh.prepare_prod_env_files(self.get_customer_number(), webserver_ips, database_ip, loadbalancer_ip)
            print('Environment directory and files succesfully created')

            # Update domain model and write to persistent storage
            self.__customer.prod_env.files_prepared = True
            self.__customer.prod_env.webserver_ips = webserver_ips
            self.__customer.prod_env.database_ip = database_ip
            idu.remove_ips(ip_list)

            print("Saving deployment information... ", end="")
            self.__persist_customer_data()
            print("succes!")
        else:
            print('Environment files are already prepared')

        deploy_with_vagrant = input('Do you want to deploy with vagrant right now? (Y/N): ')
        if (deploy_with_vagrant.lower() == 'y'):
            env_dir = build_customer_env_dir(self.get_customer_number(), "prod")
            v = vagrant.Vagrant(root=env_dir, quiet_stderr=False, quiet_stdout=False)
            v.up()
            self.__customer.prod_env.deployed = True
            self.__persist_customer_data()

    def modify_prod_environment(self, number_of_webservers: int):
        """
        Modifies Vagrantfile while keeping all server ips the same.
        For webservers the difference in the specified number is either added or removed from the Vagrantfile.
        """
        if 1 < number_of_webservers <= 5:
            raise ValueError("Number of webservers must be a minimum of 1 and maximum of 5")
        
        if number_of_webservers == len(self.__customer.prod_env.webserver_ips):
            print("Number of servers the same amount as servers deployed. No changes made")
            return
        
        # Add or remove difference in webservers
        webserver_ips = self.__customer.prod_env.webserver_ips
        difference = abs(len(webserver_ips) - number_of_webservers)
        if len(webserver_ips) < number_of_webservers:
            additional_ips = idu.find_next_available_ips(difference)
            webserver_ips.extend(additional_ips) # Assign ips to newly added servers
        elif len(webserver_ips) > number_of_webservers:
            removed_server_ips = self.__customer.prod_env.webserver_ips[-difference:]
            idu.add_ips(removed_server_ips) # Add back removed server ips to available ip list

        database_ip = self.__customer.prod_env.database_ip
        loadbalancer_ip = self.__customer.prod_env.loadbalancer_ip
        dfh.prepare_prod_env_files(self.get_customer_number(), webserver_ips, database_ip, loadbalancer_ip)

        # Update domain model and write to persistent storage
        self.__customer.prod_env.webserver_ips = webserver_ips

        print("Saving deployment information... ", end="")
        self.__persist_customer_data()
        print("succes!")

        deploy_with_vagrant = input('Do you want to deploy the updated environment with vagrant right now? (Y/N): ')
        if (deploy_with_vagrant.lower() == 'y'):
            env_dir = build_customer_env_dir(self.get_customer_number(), "prod")
            v = vagrant.Vagrant(root=env_dir, quiet_stderr=False, quiet_stdout=False)
            if len(webserver_ips) < number_of_webservers:
                v.up()
            elif len(webserver_ips) > number_of_webservers:
                for server_number in range(number_of_webservers+1, len(webserver_ips)+1):
                    v.destroy(f"www{server_number}")
            self.__customer.prod_env.deployed = True
            self.__persist_customer_data()
    
    def delete_prod_environment(self) -> None:
        """
        Destroys vagrant environment and removes production environment files
        """
        env_dir = build_customer_env_dir(self.get_customer_number(), "prod")
        v = vagrant.Vagrant(root=env_dir, quiet_stderr=False, quiet_stdout=False)
        print("Running vagrant destroy...")
        v.destroy()

        dfh.delete_prod_enviroment(self.get_customer_number())

        # Update domain model and write to persistent storage
        self.__customer.prod_env.deployed = False

        raise NotImplementedError

    def print_deployment_info(self) -> None:
        customer_info = cdu.get_customer(self.get_customer_number())
        test_env = customer_info['test_env_setup']
        prod_env = customer_info['prod_env_setup']

        print('                 ## Information about current deployment ##')
        print('Test environment:')
        for item in test_env:
            print('\t%s:\t\t%s'%(item.replace('_ip', ''), test_env.get(item)))

        print('Production environment:')
        for item in prod_env:
            if (item != 'webservers'):
                print('\t%s:\t\t%s'%(item.replace('_ip', ''), prod_env.get(item)))
            else:
                print('\t' + 'webservers:')
                for server in prod_env['webservers']:
                    print('\t\t%s:\t%s'%(server.replace('_ip', ''), prod_env.get('webservers').get(server)))

        print('')

    def get_customer_number(self) -> int:
        return self.__customer.customer_number
    
    def get_username(self) -> str:
        return self.__customer.username

    
    def __persist_customer_data(self) -> None:
        """
        Persist customer data by converting customer object, including sub-objects to dicts and saving those as json files
        """
        cdu.update_customer(self.__customer.customer_number, dict(self.__customer))





