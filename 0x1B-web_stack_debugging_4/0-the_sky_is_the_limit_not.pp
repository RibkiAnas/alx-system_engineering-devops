# let's bring that limit higher of nginx server
exec {'replace-soft-limit':
  provider => shell,
  command  => 'sudo sed -i "s/15/4096/g" /etc/default/nginx',
  before   => Exec['restart-nginx'],
}

exec {'restart-nginx':
  provider => shell,
  command  => 'sudo service nginx restart',
}
