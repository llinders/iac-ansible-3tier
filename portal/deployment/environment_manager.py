import os
import shutil
from data.customer_data_utils import environment_deployed


def deploy_new_test_environment(customer_number: int):
    if environment_deployed('test', customer_number) == False:
        newdir = './deployments/customer_%d/test'%customer_number
        if not os.path.exists(newdir):
            os.makedirs(newdir)
            shutil.copy('./templates/Vagrantfile_testenv.j2', newdir + '/Vagrantfile.j2')
            shutil.copy('./base/playbook.yml', newdir + '/playbook.yml')


            return
    print('Test environment is already deployed, cannot deploy multiple test environments')
    return

def deploy_new_prod_environment(customer_number: int):
    # check if environment already exists
    return

def modify_prod_environment(customer_number: int):
    return

def delete_test_environment(customer_number: int):
    return

def delete_prod_enviroment(customer_number: int):
    return
