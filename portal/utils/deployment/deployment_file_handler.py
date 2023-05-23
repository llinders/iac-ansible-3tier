import os
import shutil
from utils.deployment.j2_template_modifier import modify_vagrantfile_test_env, modify_vagrantfile_prod_env


def prepare_test_env_files(customer_number: int, webserver_ip: str, database_ip: str) -> None:
    env_dir = f'./deployments/customer_{customer_number}/test'
    if not os.path.exists(env_dir):
        os.makedirs(env_dir)

    # Copy Ansible role dependencies and role var files
    shutil.copytree('./base/roles', f'{env_dir}/roles', dirs_exist_ok=True) 
    shutil.copytree('./base/vars', f'{env_dir}/vars', dirs_exist_ok=True)

    __copy_common_files(env_dir)

    # Modify template Vagrantfile.j2 and write to customer deployment folder
    with open(f'{env_dir}/Vagrantfile', 'w') as out_file:
        out_file.write(modify_vagrantfile_test_env(webserver_ip, database_ip))
    

def prepare_prod_env_files(customer_number: int, webserver_ips: list[str], loadbalancer_ip: str, database_ip: str) -> None:
    env_dir = f'./deployments/customer_{customer_number}/prod'
    if not os.path.exists(env_dir):
        os.makedirs(env_dir)

    __copy_common_files(env_dir)

    # Generate and write inventory.ini file
    ini_file: str = f"[webservers]\n"
    for ip in webserver_ips:
        ini_file += f"{ip}\n"
    ini_file += f"[database]\n{database_ip}"
    with open(f'{env_dir}/inventory.ini', 'w') as out_file:
        out_file.write(ini_file)

    # Modify template Vagrantfile.j2 and write to customer deployment folder
    with open(f'{env_dir}/Vagrantfile', 'w') as out_file:
        out_file.write(modify_vagrantfile_prod_env(webserver_ips, database_ip, loadbalancer_ip))

    return

def modify_prod_environment(customer_number: int) -> None:
    raise NotImplementedError

def delete_test_environment(customer_number: int) -> None:
    raise NotImplementedError

def delete_prod_enviroment(customer_number: int) -> None:
    raise NotImplementedError

def __copy_common_files(env_dir: str) -> None:
    # Copy Ansible role dependencies and role var files
    shutil.copytree('./base/roles', f'{env_dir}/roles', dirs_exist_ok=True) 
    shutil.copytree('./base/vars', f'{env_dir}/vars', dirs_exist_ok=True)

    # Copy Ansible config file and other Ansible files
    shutil.copy('./base/ansible.cfg', f'{env_dir}/ansible.cfg')
    shutil.copy('./base/playbook-common.yml', f'{env_dir}/playbook-common.yml')
    shutil.copy('./base/playbook-specific.yml', f'{env_dir}/playbook-specific.yml')
