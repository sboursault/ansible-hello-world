# ansible-hello-world

## Run the project

Prerequisites : vagrant and ansible installed
    
Start vagrant VMs (1 nginx and 2 application servers)

    vagrant up
    
Install nginx and the hello world service on both application servers

    playbooks/main.yml -i inventory/vagrant
    
Call the hello-world service through nginx

    curl -i http://localhost:8080/hello/info
    
And repeat to get the response from the other instance

    curl -i http://localhost:8080/hello/info
    
Upgrade the hello-service on one instance

    # remove app-server1 from load balancer and upgrade
    playbooks/upgrade-hello-world.yml -i inventory/vagrant --limit app-server1 --tags prepare

Verify the deployment

    curl -i http://localhost:8080/hello/info # no more response from app-server1
    curl -i http://localhost:8080/app-server1/hello/info # verify the upgraded instance

Finalize the deployment on both instance

    playbooks/upgrade-hello-world.yml -i inventory/vagrant --limit app-server1 --tags finalize
    playbooks/upgrade-hello-world.yml -i inventory/vagrant --limit app-server2


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


## ansible cheat sheet

### intall ansible

    sudo apt-get install python python-pip
    sudo pip install ansible
    
### run a task on a host or a group

    ansible app-server1 -m ping -i inventory/vagrant
    ansible virtual-machines -m ping -i inventory/vagrant
    ansible all -m ping -i inventory/vagrant
    ansible '*' -m ping -i inventory/vagrant
    
### run with docker

    docker run --rm -v `pwd`:/ansible -w /ansible williamyeh/ansible:ubuntu16.04 \
      ansible app-server1 -m ping -i inventory/vagrant

### modules

    # command module
    ansible app-server1 [-m command] -a uptime
    
    # apt module as root
    ansible app-server1 -b -m apt -a name=nginx
    
    # service module as root
    ansible app-server1 -b -m service -a "name=nginx state=restarted"
    
    # get module doc
    ansible-doc service

### getting facts

    ansible app-server1 -m setup [-a 'filter=ansible_eth*'] -i inventory/vagrant

### getting hostvars

    ansible app-server1 -m debug -a var=hostvars -i inventory/vagrant


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

    # with
    ansible-galaxy init <role>
    # with molecule
    sudo pip install molecule docker-py
    molecule init role -r <role-name> -d docker
    
test your roles with molecule

    molecule [--debug] test
    
_[...] don’t unit test your playbook.
Ansible describes states of resources declaratively, so you don’t have to.
If there are cases where you want to be sure of something though, that’s great, and things like stat/assert are great go-to modules for that purpose.
(https://docs.ansible.com/ansible/latest/reference_appendices/test_strategies.html)_

#### protect sensitive data with vault

    # Encrypt file with vault (password: secret)
    ansible-vault encrypt|decrypt|view|edit|rekey secrets.yml
    
    # run ansible with vault pass
    ansible all -m ping -i inventory/vagrant --ask-vault-pass
    # or
    ansible all -m ping -i inventory/vagrant --vault-password-file password.txt
    
NB: you can define vault-password-file in ansible.cfg


# Ansible troubleshooting

Error message like "WARNING: REMOTE HOST IDENTIFICATION HAS CHANGED!"
Can happen after reloading an image.
    
    rm ~/.ssh/known_hosts

# Resources

[Ansible up and running](http://shop.oreilly.com/product/0636920065500.do)

[infrastructure as code](https://www.youtube.com/watch?v=K843Ukiw3d8)

[Test roles with Molecule](https://www.jeffgeerling.com/blog/2018/testing-your-ansible-roles-molecule)

[multistage environments](https://www.digitalocean.com/community/tutorials/how-to-manage-multistage-environments-with-ansible)

# 2 quotes from Kief Morris

_The essence of Infrastructure as Code is to treat the configuration of systems the same way that software source code is treated.
Source code management systems, Test Driven Development (TDD), Continuous Integration (CI), refactoring, and other XP practices are especially useful for making sure that changes to infrastructure are thoroughly tested, repeatable and transparent.
(https://www.thoughtworks.com/insights/blog/infrastructure-code-iron-age-cloud-age)_

_The only way to break the spiral is to face your fears. Pick a subset of your servers, choose one or two things on them to put under configuration management, and then schedule these to be applied unattended, at least once an hour.
Starting small and simple helps to limit the risk. The important thing is that you take the leap—let the automation go on its own, without you holding its hand. Then you can increase the scope—add a few more parts of the server to the automation, and extend it to more servers.
You should also build out other things that will give you more confidence, piece by piece. Add monitoring to detect when the thing you’ve automated goes wrong. Set up Continuous Integration to automatically test the configuration change every time you commit.
Again, getting these pieces in place with a small, simple set of configuration, creates the platform. You can then extend the coverage with confidence.*
(https://www.thoughtworks.com/insights/blog/infrastructure-code-automation-fear-spiral)_

# TODO

- add role dependency (Ansible up and running p184)
- create a playbook that makes sure a container is up
   - see docker dynamic inventory https://docs.ansible.com/ansible/2.7/scenario_guides/guide_docker.html
   - docker container module https://docs.ansible.com/ansible/latest/modules/docker_container_module.html
   - ansible container may not be a good idea https://blog.octo.com/en/ansible-container-chronicle-of-a-death-foretold/
