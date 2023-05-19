""" Jinja2 template modifier

This file contains functions that renders the 'Vagrantfile' and other necessary files that contain customer specific variables. 

"""

from jinja2 import Template

__VAGRANTFILE_TEMPLATE_DIR_TEST__ = './templates/Vagrantfile_testenv.j2'
__VAGRANTFILE_TEMPLATE_DIR_PROD__ = './templates/Vagrantfile_prodenv.j2'

def modify_vagrantfile_testenv(webserver_ip: str, database_ip: str) -> str:
    with open(__VAGRANTFILE_TEMPLATE_DIR_TEST__, 'r') as in_file:
        template = Template(in_file.read())


    context = {
        "webserver_ip": webserver_ip,
        "database_ip": database_ip
    }

    return template.render(context)
        

def modify_vagrantfile_prodenv():
    return