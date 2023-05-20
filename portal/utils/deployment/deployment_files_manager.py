import os
import shutil
from utils.data.customer_data_utils import environment_deployed
from utils.deployment.j2_template_modifier import modify_vagrantfile_testenv


def create_test_env_files(customer_number: int, webserver_ip: str, database_ip: str) -> None:
    if environment_deployed(env='test', customer_number=customer_number):
        raise Exception('Test environment is already deployed, cannot deploy multiple test environments')
    
    customer_dir = f'./deployments/customer_{customer_number}/test'
    if not os.path.exists(customer_dir):
        os.makedirs(customer_dir)

    # Copy Ansible role dependencies and role var files
    shutil.copytree('./base/roles', f'{customer_dir}/roles', dirs_exist_ok=True) 
    shutil.copytree('./base/vars', f'{customer_dir}/vars', dirs_exist_ok=True)

    # Copy Ansible config file and other Ansible files
    shutil.copy('./base/ansible.cfg', f'{customer_dir}/ansible.cfg')
    shutil.copy('./base/playbook-common.yml', f'{customer_dir}/playbook-common.yml')
    shutil.copy('./base/playbook-specific.yml', f'{customer_dir}/playbook-specific.yml')

    # Generate and write inventory.ini file
    with open(f'{customer_dir}/inventory.ini', 'w') as out_file:
        out_file.write(f'[webservers]\n{webserver_ip}\n[database]\n{database_ip}')

    # Modify template Vagrantfile.j2 and write to customer deployment folder
    #shutil.copy('./templates/Vagrantfile_testenv.j2', f'{customer_dir}/Vagrantfile.j2')
    with open(f'{customer_dir}/Vagrantfile', 'w') as out_file:
        out_file.write(modify_vagrantfile_testenv(webserver_ip, database_ip))
    

def create_prod_env_files(customer_number: int) -> None:
    # check if environment already exists
    return

def modify_prod_environment(customer_number: int) -> None:
    return

def delete_test_environment(customer_number: int) -> None:
    return

def delete_prod_enviroment(customer_number: int) -> None:
    return
