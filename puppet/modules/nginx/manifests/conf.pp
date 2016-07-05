# == Define: conf
#
# Adds an Ngnix configuration file.
#
define nginx::conf() {
  $cnf_file = "nginxproxy"

  #Set up virtual_host
  file {'setup-vhost-nginx': 
    path => "/etc/nginx/sites-available/${cnf_file}",
    source  => "puppet:///modules/nginx/${cnf_file}",
    require => Package['nginx'],
    notify  => Service['nginx'];
  }

  # Disable default nginx config
  file { 'default-nginx-disable':
      path => '/etc/nginx/sites-enabled/default',
      ensure => absent,
      require => Package['nginx'],
  }

  # Enable virtual_host
  file { 'vhost-nginx-enable':
      path => "/etc/nginx/sites-enabled/${cnf_file}",
      target => "/etc/nginx/sites-available/${cnf_file}",
      ensure => link,
      notify => Service['nginx'],
      require => [
          File['setup-vhost-nginx'],
          File['default-nginx-disable'],
      ],
  }
}
