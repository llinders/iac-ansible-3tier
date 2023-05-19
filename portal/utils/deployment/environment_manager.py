import os
import shutil
from data.customer_data_utils import environment_deployed


def deploy_new_test_environment(customer_number: int):
    if environment_deployed(env='test', customer_number=customer_number) == False:
        customer_dir = './deployments/customer_%d/test'%customer_number
        if not os.path.exists(customer_dir):
            os.makedirs(customer_dir)

            # Copy role dependencies
            shutil.copytree('./base/roles', f'{customer_dir}/roles', dirs_exist_ok=True) 

            # Copy Ansible config file
            shutil.copy('./base/ansible.cfg', f'{customer_dir}/ansible.cfg')

            # Copy 
            shutil.copy('./templates/Vagrantfile_testenv.j2', f'{customer_dir}/Vagrantfile.j2')
            shutil.copy('./base/playbook.yml', f'{customer_dir}/playbook.yml')
            
            # Copy Ansible var files


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
