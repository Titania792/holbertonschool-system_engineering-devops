# 0x0B. SSH
## Tasks

### 0. Use a private key
Write a Bash script that uses  `ssh`  to connect to your server using the private key  `~/.ssh/school`  with the user  `ubuntu`.
Requirements:
-   Only use  `ssh`  single-character flags
-   You cannot use  `-l`
-   You do not need to handle the case of a private key protected by a passphrase
-   File:  [`0-use_a_private_key`](https://github.com/Titania792/holberton-system_engineering-devops/blob/main/0x0B-ssh/0-use_a_private_key)

### 1. Create an SSH key pair

Write a Bash script that creates an RSA key pair.
Requirements:
-   Name of the created private key must be  `school`
-   Number of bits in the created key to be created 4096
-   The created key must be protected by the passphrase  `betty`
-   File:  [`1-create_ssh_key_pair`](https://github.com/Titania792/holberton-system_engineering-devops/blob/main/0x0B-ssh/1-create_ssh_key_pair)

### 2. Client configuration file
Your machine has an SSH configuration file for the local SSH client, let’s configure it to our needs so that you can connect to a server without typing a password. Share your SSH client configuration in your answer file.
Requirements:
-   Your SSH client configuration must be configured to use the private key  `~/.ssh/school`
-   Your SSH client configuration must be configured to refuse to authenticate using a password
-   File:  [`2-ssh_config`](https://github.com/Titania792/holberton-system_engineering-devops/blob/main/0x0B-ssh/2-ssh_config)

### 4. Client configuration file (w/ Puppet)
Let’s practice using Puppet to make changes to our configuration file. Just as in the previous configuration file task, we’d like you to set up your client SSH configuration file so that you can connect to a server without typing a password.

Requirements:
-   Your SSH client configuration must be configured to use the private key  `~/.ssh/school`
-   Your SSH client configuration must be configured to refuse to authenticate using a password
-   File:  [`100-puppet_ssh_config.pp`](https://github.com/Titania792/holberton-system_engineering-devops/blob/main/0x0B-ssh/100-puppet_ssh_config.pp)