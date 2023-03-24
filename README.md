# 3-tier IaC web-application with Vagrant and Ansible
## Description
In this project a 3-tiered application is automatically deployed using Vagrant and Ansible for provisioning. The application consists of:
* An HAProxy load balancer, 
* Apache servers that host the web-application
* A PostgreSQL database

## How to install and run the project
### Prerequisite
For this project an eSXI host is used for the deployment of the Virtual Machines. This should be up and running before continuing.

Optionally you can also alter the Vagrantfile to deploy the Virtual Machines to a host of your liking.

### Setup
1. Make sure you have `Vagrant`, `Ansible` and `Python3` installed on your machine.
2. Clone this repository with the following command:
`git clone git@github.com:llinders/iac-ansible-3tier.git`
3. Alter all ip addresses in the Vagrantfile to match your infrastructure.

### Running the project
Once you have completed the setup steps you can deploy the infrastructure with the following command from command line:
`vagrant up`