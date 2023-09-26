# Install and configure nginx server using puppet

package { 'nginx':
  ensure => 'installed',
  before => File['/var/www/html/index.html', '/var/www/html/404.html'],
}

file { '/var/www/html/index.html':
  ensure  => file,
  content => 'Hello World!',
}

file { '/var/www/html/404.html':
  ensure  => file,
  content => 'Ceci n\'est pas une page',
}

file_line { 'nginx_redirect':
  path  => '/etc/nginx/sites-enabled/default',
  line  => 'rewrite ^\/redirect_me https:\/\/www.linkedin.com\/in\/anas-ribki permanent;',
  match => '^server_name _;$',
}

file_line { 'nginx_404':
  path  => '/etc/nginx/sites-enabled/default',
  line  => 'error_page 404 \/404.html;\n\tlocation = \/404.html {\n\t\troot \/var\/www\/html;\n\t\tinternal;\n\t}',
  match => '^listen 80 default_server;$',
}

service { 'nginx':
  ensure     => running,
  enable     => true,
  hasrestart => true,
  subscribe  => [File['/var/www/html/index.html', '/var/www/html/404.html'], File_line['nginx_redirect', 'nginx_404']],
}
