# -*- mode: ruby -*-
# vi: set ft=ruby :

# All Vagrant configuration is done below. The "2" in Vagrant.configure
# configures the configuration version (we support older styles for
# backwards compatibility). Please don't change it unless you know what
# you're doing.
Vagrant.configure(2) do |config|

#Check if Nginx listen 80 port
  config.vm.provision "checknginx", type: "shell" do |checknginx|
         checknginx.path = "check_nginx.sh"
  end

#Install Puppet on VMs
  config.vm.provision "puppetinstall", type: "shell" do |pkginstall|
        pkginstall.path = "package_install.sh"
	pkginstall.args = "puppet"
  end

# Define and configure proxy
 config.vm.define :websrv do |websrv|
	websrv.vm.box = "puppetlabs/ubuntu-14.04-64-nocm"
        websrv.vm.hostname = "websrv"
        websrv.vm.network "private_network", ip: "192.168.33.10", virtualbox__intnet: true
	websrv.vm.network "public_network", ip: "192.168.0.110"
 end

#Apply Puppet manifests (Nginx)
 config.vm.provision :puppet do |puppet|
	puppet.manifests_path = "puppet/manifests"
	puppet.manifest_file = "site.pp"
	puppet.module_path = "puppet/modules"
	puppet.options="--verbose --debug"
  end
end
