""" Jinja2 template modifier

This file contains functions that renders the 'Vagrantfile' and other necessary files that contain customer specific variables. 

"""

from jinja2 import Template

__VAGRANTFILE_TEMPLATE_DIR_TEST = './templates/Vagrantfile_testenv.j2'
__VAGRANTFILE_TEMPLATE_DIR_PROD = './templates/Vagrantfile_prodenv.j2'

def modify_vagrantfile_test_env(webserver_ip: str, database_ip: str) -> str:
    with open(__VAGRANTFILE_TEMPLATE_DIR_TEST, 'r') as in_file:
        template = Template(in_file.read())


    context = {
        "webserver_ip": webserver_ip,
        "database_ip": database_ip
    }

    return template.render(context)
        

def modify_vagrantfile_prod_env(webserver_ips: list[str], database_ip: str, loadbalancer_ip: str) -> str:
    with open(__VAGRANTFILE_TEMPLATE_DIR_PROD, 'r') as in_file:
        template = Template(in_file.read())

    context = {
        "webservers": webserver_ips,
        "database_ip": database_ip,
        "loadbalancer_ip": loadbalancer_ip
    }

    return template.render(context)