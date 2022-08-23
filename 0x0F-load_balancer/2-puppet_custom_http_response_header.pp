#This script automate the task of creating a custom HTTP header response

exec {'update':
    provider => shell,
    command  => 'sudo apt -y update',
} ~>

exec {'nginx_install':
    provider => shell,
    command  => 'sudo apt -y install nginx',
} ~>

exec {'add_header':
    provider => shell,
    command  => "sed -i '/listen 80 default_server;/a add_header X-Served-By $hostname;' /etc/nginx/sites-available/default",
} ~>

exec {'restart':
    provider => shell,
    command  => 'sudo service nginx restart'
}
