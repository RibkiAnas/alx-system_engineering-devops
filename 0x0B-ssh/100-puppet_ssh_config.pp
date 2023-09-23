# Configure SSH file to connect to a server without typing a password.

include stdlib

# Ensure that the IdentityFile option is set to ~/.ssh/school
file_line { 'Identity file':
  path  => '/etc/ssh/ssh_config',
  line  => 'IdentityFile ~/.ssh/school',
  match => '^IdentityFile',
}

# Ensure that the PasswordAuthentication option is set to no
file_line { 'Turn off passwd':
  path  => '/etc/ssh/ssh_config',
  line  => 'PasswordAuthentication no',
  match => '^PasswordAuthentication',
}
