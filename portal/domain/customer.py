from domain.test_environment import TestEnvironment
from domain.prod_environment import ProductionEnvironment


class Customer:
    customer_number: int
    username: str
    test_env: TestEnvironment
    prod_env: ProductionEnvironment

    def __init__(self, customer_number: int, username: str, prod_env: ProductionEnvironment, test_env: TestEnvironment):
        self.customer_number = customer_number
        self.username = username
        self.prod_env = prod_env
        self.test_env = test_env

    def __iter__(self):
        yield 'customer_number', self.customer_number
        yield 'username', self.username
        yield 'test_env_setup', dict(self.test_env)
        yield 'prod_env_setup', dict(self.prod_env)