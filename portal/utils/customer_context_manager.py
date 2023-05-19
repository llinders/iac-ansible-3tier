""" Customer Context Manager

Holds customer data in memory and synchronized customer data with persistent storage.
Acts as a facade to simplify customer data management and persistent storage synchronization.

"""

from domain.customer import Customer
from domain.prod_environment import ProductionEnvironment
from domain.test_environment import TestEnvironment

import utils.data.customer_data_utils as cdu
import utils.data.ip_data_utils as idu
import utils.deployment.environment_manager as em


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
        ip_list = idu.find_next_available_ips(2)
        webserver_ip = ip_list[0]
        database_ip = ip_list[1]
        try:
            em.deploy_new_test_environment(self.get_customer_number(), webserver_ip, database_ip)
            self.customer.test_env.webserver_ip = webserver_ip
            self.customer.test_env.database_ip = database_ip
            idu.remove_ips(ip_list)
        except Exception as ex:
            print(ex)

    def destroy_test_environment(self) -> None:
        em.delete_test_environment(self.get_customer_number())
        # add ips back to available ips

    def get_customer_number(self) -> int:
        return self.customer.customer_number
    
    def get_username(self) -> str:
        return self.customer.username

        

