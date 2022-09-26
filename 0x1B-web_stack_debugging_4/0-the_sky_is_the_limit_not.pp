#Sky is the limit, let's bring that limit higher

exec {'ulimit':
    provider => shell,
    command  => "sed -i 's/ULIMIT=\"-n 15\"/ULIMIT=\"-n 2000\"/g' /etc/default/nginx",
    before   => Exec['restart']
}

exec {'restart':
    provider => shell,
    command  => 'sudo service nginx restart'
}