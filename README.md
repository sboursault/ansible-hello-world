# ansible-hello-world

# TLDR;
    
    # start VMs
    vagrant up
    
    # run playbooks
    playbooks/main.yml -i inventory/vagrant
    
    # watch the result
    curl -i http://localhost:8080
    curl -i http://localhost:8080/hello

## vagrant servers

### create and run Vagrant VM

    # create the Vagrantfile
    vagrant init ubuntu/trusty64
    # start vagrant servers
    vagrant up

Eventually, add port mapping in your vagrantfile and run `vagrant reload`

### get the ssh config for to connecto to the VM
    vagrant ssh-config
    
### stop image
    vagrant halt

### destroy image
    vagrant destroy [--force]

### ssh to vagrant
    vagrant ssh
    # or
    ssh vagrant@127.0.0.1 -p 2222 -i .vagrant/machines/default/virtualbox/private_key

### get vm status
    vagrant status

## nginx

### create TLS certificate for the https
    openssl req -x509 -nodes -days 3650 -newkey rsa:2048 \
      -subj /CN=localhost \
      -keyout nginx/nginx.key -out nginx/nginx.crt

## ansible

### intall ansible

    sudo pip install ansible
    
Global configuration can be stored in ansible.cfg

### ping a host or a group

    ansible testserver -m ping
    ansible webservers -m ping
    ansible all -m ping
    ansible '*' -m ping

### ansible modules

    # command module
    ansible testserver [-m command] -a uptime
    
    # apt module as root
    ansible testserver -b -m apt -a name=nginx
    
    # service module as root
    ansible testserver -b -m service -a "name=nginx state=restarted"
    

### restart nginx

### get module doc
    ansible-doc service

### playbooks

### list tasks
    playbooks/playbook.yml -i inventory/vagrant --list-tasks

#### execute a playbook
    ansible-playbook playbooks/playbook.yml -i inventory/vagrant
    # or if the playbook file is executable and starts with `#!/usr/bin/env ansible-playbook`
    playbooks/playbook.yml -i inventory/vagrant
    
handlers should be used only to restart servicesd
WARNING :
  a handler may not be triggered if an error occurs on a task.
  Plus, re-running the play won't help, since the task which notifies the handler won't be executed (no state change)
  
### getting facts
    ansible nginx -m setup [-a 'filter=ansible_eth*'] -i inventory/vagrant

### roles

create a new role

    ansible-galaxy init <role>

# take aways

“Simple things should be simple, complex things should be possible.”
― Alan Kay



# anisble runner with doker

docker run --rm -v `pwd`:/ansible -w /ansible williamyeh/ansible:ubuntu16.04 playbooks/test.yml -i inventory/vagrant



