# -*- mode: ruby -*-
# vi: set ft=ruby :

VAGRANTFILE_API_VERSION = "2"

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|

  # complete reference: https://docs.vagrantup.com.

  # Use the same key for each machine
  # ( ~/.vagrant.d/insecure_private_key instead of .vagrant/machines/<VM>/virtualbox/private_key
  config.ssh.insert_key = false

  config.vm.define "vagrant1" do |node|
    node.vm.box = "ubuntu/trusty64"
    node.vm.hostname = "vagrant1"
    node.vm.network "private_network", ip: "192.168.33.11"
    node.vm.network "forwarded_port", guest: 80, host: 8080
    node.vm.network "forwarded_port", guest: 443, host: 8443
  end

  config.vm.define "vagrant2" do |node|
    node.vm.box = "ubuntu/trusty64"
    node.vm.hostname = "vagrant2"
    node.vm.network "private_network", ip: "192.168.33.12"
    node.vm.network "forwarded_port", guest: 80, host: 8081
    node.vm.network "forwarded_port", guest: 443, host: 8444
  end

  config.vm.define "vagrant3" do |node|
    node.vm.box = "ubuntu/tru ;sty64"
    node.vm.hostname = "vagrant3"
    node.vm.network "private_network", ip: "192.168.33.13"
    node.vm.network "forwarded_port", guest: 80, host: 8082
    node.vm.network "forwarded_port", guest: 443, host: 8445
  end

end
