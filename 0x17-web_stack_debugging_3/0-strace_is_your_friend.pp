# Fix phpp extensions in wp-settings.php

exec {'Fix phpp extension':
  command => 'sed -i \'s/phpp/php/g\' /var/www/html/wp-settings.php',
  path    => '/usr/local/bin/:/bin/'
}
