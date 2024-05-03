# Executing command 'killmenow' using puppet

exec { 'pkill':
  command  => 'pkill killmenow',
  provider => 'shell',
}
