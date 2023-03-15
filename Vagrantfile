# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure("2") do |config|
    config.vm.box = "generic/ubuntu2004"
    config.ssh.insert_key = false
    config.vm.synced_folder('.', '/vagrant', disabled: true)
  
    config.vm.provider :vmware_esxi do |esxi|
        esxi.esxi_hostname = '192.168.1.101'
        esxi.esxi_username = 'root'
        esxi.esxi_password = '5Vhj2WzmGE45cxp'
        esxi.esxi_virtual_network = ['VM Network']
        esxi.guest_memsize = '2048'
        esxi.guest_numvcpus = '1'
    end

    # Apache webserver 1
    config.vm.define "www1" do |www1|
        www1.vm.hostname = "webserver01.iac"
        www1.vm.define "192.168.1.51"
        www1.vm.network :private_network, ip: "192.168.1.51"
    
        www1.vm.provision "ansible" do |ansible|
            ansible.playbook = "playbook.yml"
            ansible.extra_vars = {
              ansible_user: 'vagrant',
              ansible_ssh_private_key_file: "~/.vagrant.d/insecure_private_key"
            }
        end
    end

    # Apache webserver 2
    config.vm.define "www2" do |www2|
        www2.vm.hostname = "webserver02.iac"
        www2.vm.define "192.168.1.52"
        www2.vm.network :private_network, ip: "192.168.1.52"

        www2.vm.provision "ansible" do |ansible|
            ansible.playbook = "playbook.yml"
            ansible.extra_vars = {
              ansible_user: 'vagrant',
              ansible_ssh_private_key_file: "~/.vagrant.d/insecure_private_key"
            }
        end
    end

    # Load balancer
    config.vm.define "lb" do |lb|
        lb.vm.hostname = "lb.iac"
        lb.vm.define "192.168.1.53"
        lb.vm.network :private_network, ip: "192.168.1.53"

        lb.vm.provision "ansible" do |ansible|
            ansible.playbook = "playbook.yml"
            ansible.extra_vars = {
                ansible_user: 'vagrant',
                ansible_ssh_private_key_file: "~/.vagrant.d/insecure_private_key"
            }
        end
    end

    # Database
    config.vm.define "db" do |db|
        db.vm.hostname = "db.iac"
        db.vm.define "192.168.1.54"
        db.vm.network :private_network, ip: "192.168.1.54"

        db.vm.provision "ansible" do |ansible|
            ansible.playbook = "playbook.yml"
            ansible.extra_vars = {
                ansible_user: 'vagrant',
                ansible_ssh_private_key_file: "~/.vagrant.d/insecure_private_key"
            }
        end
    end
end