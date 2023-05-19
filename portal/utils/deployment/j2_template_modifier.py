""" Jinja2 template modifier

This file contains functions that renders the 'Vagrantfile' and other necessary files that contain customer specific variables. 

"""

from jinja2 import Template
import data.ip_data_utils as cdi

__VAGRANTFILE_TEMPLATE_DIR_TEST__ = './templates/Vagrantfile_testenv.j2'
__VAGRANTFILE_TEMPLATE_DIR_PROD__ = './templates/Vagrantfile_prodenv.j2'

def modify_vagrantfile_testenv():
    with open(__VAGRANTFILE_TEMPLATE_DIR_TEST__, 'r') as in_file:
        template = Template(in_file.read())

    ip_list: list = cdi.find_next_available_ips(2)

    context = {
        "webserver_ip": ip_list[0],
        "database_ip": ip_list[1]
    }

    return template.render(context)
        

def modify_vagrantfile_prodenv():
    return