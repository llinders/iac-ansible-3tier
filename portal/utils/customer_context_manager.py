""" Customer Context Manager

Holds customer data in memory and synchronized customer data with persistent storage.
Acts as a facade to simplify customer data management and persistent storage synchronization.
This manager class is also used to simplify environment deployments, since it is responsible for updating in-memory and
persistent data of deployed environments.

"""

from domain.customer import Customer
from domain.prod_environment import ProductionEnvironment
from domain.test_environment import TestEnvironment
import portal.utils.data.customer_data_utils as cdu

import utils.data.customer_data_utils as cdu
import utils.data.ip_data_utils as idu
import portal.utils.deployment.deployment_files_manager as dfm


class CustomerContextManager:
    customer: Customer
    
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
            deployed=prod_env_data['deployed'],
            loadbalancer_ip=prod_env_data['loadbalancer_ip'],
            database_ip=prod_env_data['database_ip'],
            webserver_ips=prod_env_data['webservers']
            )
        
        # Initialize test environment domain object
        test_env_data = customer_data['test_env_setup']
        test_env = TestEnvironment(
            deployed=test_env_data['deployed'],
            database_ip=test_env_data['database_ip'],
            webserver_ip=test_env_data['webserver_ip']
            )

        # Initialize customer domain object
        self.customer = Customer(
            customer_number=customer_number, 
            username=customer_data['username'], 
            prod_env=prod_env,
            test_env=test_env
            )
        
    def create_and_load_new_customer(self, username: str) -> None:
        self.load(cdu.write_new_customer(username))

    def deploy_new_test_environment(self) -> None:
        """
        Acts as a facade method to create a new customer test deployment directory, modify j2 templates, 
        copy files and update customer data
        """
        ip_list = idu.find_next_available_ips(2)
        webserver_ip = ip_list[0]
        database_ip = ip_list[1]
        try:
            dfm.create_test_env_files(self.get_customer_number(), webserver_ip, database_ip)
            self.customer.test_env.webserver_ip = webserver_ip
            self.customer.test_env.database_ip = database_ip
            idu.remove_ips(ip_list)
            self._persist_customer_data()
        except Exception as ex:
            print(ex)

    def destroy_test_environment(self) -> None:
        dfm.delete_test_environment(self.get_customer_number())
        idu.add_ips([self.customer.test_env.webserver_ip, self.customer.test_env.database_ip])


    def get_customer_number(self) -> int:
        return self.customer.customer_number
    
    def get_username(self) -> str:
        return self.customer.username

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
    
    def _persist_customer_data(self) -> None:
        """
        Persist customer data by converting customer object, including sub-objects to dicts and saving those as json files
        """
        cdu.update_customer(self.customer.customer_number, dict(self.customer))





