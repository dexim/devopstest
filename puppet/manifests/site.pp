#Run apt-get update;
exec { 'apt-get update':
 path   => '/usr/bin',
}

node 'websrv' {

  package { ['python3']:
    ensure => present,
    require => Exec['apt-get update'];
  }

include nginx
}
