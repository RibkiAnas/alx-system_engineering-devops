# Create a manifest that kills a proccess named killmenow.
exec { 'killmenow':
  command => 'pkill killmenow',
  path    => '/usr/bin:/bin',
}
