# ansible-hello-world

## Run the project
    
Start vagrant VMs (1 nginx and 2 application servers)

    vagrant up
    
Install nginx and the hello world service on both application servers

    playbooks/main.yml -i inventory/vagrant
    
Call the hello world service through nginx

    curl -i http://localhost:8080/hello/info
    
And repeat to get the response from the other instance

    curl -i http://localhost:8080/hello/info

## vagrant cheat sheet

### create the Vagrantfile
    
    vagrant init ubuntu/trusty64
    
### frequently used commands
    
    vagrant up|halt|destroy|status
    
### ssh to vagrant
    
    # get the ssh config to connect to the VM
    vagrant ssh-config
    # connect with vagrant command
    vagrant ssh
    # or with ssh command (password: ansible)
    ssh vagrant@127.0.0.1 -p 2222
    # or with the privacy key
    ssh vagrant@127.0.0.1 -p 2222 -i .vagrant/machines/default/virtualbox/private_key


## nginx cheat sheet

### create TLS certificate for the https
    openssl req -x509 -nodes -days 3650 -newkey rsa:2048 \
      -subj /CN=localhost \
      -keyout nginx/nginx.key -out nginx/nginx.crt

## ansible cheat sheet

### intall ansible

    sudo pip install ansible
    
    
    
### run a task on a host or a group

    ansible server1 -m ping -i inventory/vagrant
    ansible virtual-machines -m ping -i inventory/vagrant
    ansible all -m ping -i inventory/vagrant
    ansible '*' -m ping -i inventory/vagrant
    
### run with docker

    docker run --rm -v `pwd`:/ansible -w /ansible williamyeh/ansible:ubuntu16.04 \
      ansible server1 -m ping -i inventory/vagrant

### modules

    # command module
    ansible server1 [-m command] -a uptime
    
    # apt module as root
    ansible server1 -b -m apt -a name=nginx
    
    # service module as root
    ansible server1 -b -m service -a "name=nginx state=restarted"
    
    # get module doc
    ansible-doc service

### getting facts

    ansible server1 -m setup [-a 'filter=ansible_eth*'] -i inventory/vagrant

### getting hostvars

    ansible server1 -m debug -a var=hostvars -i inventory/vagrant


### playbooks

#### list tasks
    playbooks/playbook.yml -i inventory/vagrant --list-tasks

#### execute a playbook
    ansible-playbook playbooks/playbook.yml -i inventory/vagrant
    # or if the playbook file is executable and starts with `#!/usr/bin/env ansible-playbook`
    playbooks/playbook.yml -i inventory/vagrant

#### handlers
    
Handlers should be used only to restart services.

WARNING :
  a handler may not be triggered if an error occurs on a task.
  Plus, re-running the play won't help, since the task which notifies the handler won't be executed (no state change)
  

#### roles

create a new role

    ansible-galaxy init <role>

#### protect sensitive data with vault

    # Encrypt file with vault (password: secret)
    ansible-vault encrypt|decrypt|view|edit|rekey secrets.yml
    
    # run ansible with vault pass
    ansible all -m ping -i inventory/vagrant --ask-vault-pass
    # or
    ansible all -m ping -i inventory/vagrant --vault-password-file password.txt
    
NB: you can define vault-password-file in ansible.cfg

# take aways

“Simple things should be simple, complex things should be possible.”
― Alan Kay




# Ansible troubleshooting


Error message like "WARNING: REMOTE HOST IDENTIFICATION HAS CHANGED!"
Can happen after reloading an image.
    
    rm ~/.ssh/known_hosts


 
# Resources

[Ansible up and running]: http://shop.oreilly.com/product/0636920065500.do

[ansible.cfg file entries]: https://docs.ansible.com/ansible/latest/reference_appendices/config.html

# TODO
 add role dependency (Ansible up and running p184)
 test roles
 upgrade appservers by removing them from the nginx