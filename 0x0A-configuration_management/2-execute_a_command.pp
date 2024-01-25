# Executing a command using puppet

exec { 'pkill':
  command  => 'pkill killmenow',
  provider => 'shell',
}
