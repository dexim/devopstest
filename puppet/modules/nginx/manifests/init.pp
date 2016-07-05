# == Class: ngnix
#
# Installs packages for Ngnix and sets config files.
#
class nginx {
  package { ['nginx']:
    ensure => present,
    require => Exec['apt-get update'];
  }

  # create a directory for content    
  file { '/var/www':
    ensure => 'directory',
    owner  => 'root',
    group  => 'root',
    mode   => '0744',
  }

  #Make configuration
  nginx::conf { [$hostname]: }

  service { 'nginx':
    ensure  => running,
    require => Package['nginx'];
  }

}
