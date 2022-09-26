#changing OS configuration

exec {'hardnf':
    provider => shell,
    command  => "sed -i 's/holberton hard nofile 5/holberton hard nofile 5000/g' /etc/security/limits.conf",
    before   => Exec['softnf']
}

exec {'softnf':
    provider => shell,
    command  => "sed -i 's/holberton soft nofile 4/holberton soft nofile 5000/g' /etc/security/limits.conf",
}