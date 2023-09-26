# Install and configure nginx server using puppet

# Ensure nginx package is installed
package { 'nginx':
  ensure => 'present',
}

# Update system and install nginx
exec { 'install_nginx':
  command  => 'sudo apt-get update && sudo apt-get -y install nginx',
  provider => 'shell',
}

# Create a simple "Hello World!" index.html file
exec { 'create_index_html':
  command  => 'echo "Hello World!" | sudo tee /var/www/html/index.html',
  provider => 'shell',
}

# Add a redirect rule to the default nginx configuration
exec { 'add_redirect_rule':
  command  => 'sudo sed -i "s/listen 80 default_server;/listen 80 default_server;\\n\\tlocation \/redirect_me {\\n\\t\\treturn 301 https:\/\/linkedin.com\/in\/anas-ribki;\\n\\t}/" /etc/nginx/sites-available/default',
  provider => 'shell',
}

# Restart the nginx service to apply changes
exec { 'restart_nginx':
  command  => 'sudo service nginx restart',
  provider => 'shell',
}
