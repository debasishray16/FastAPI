# Steps to setup SSH directly

1. Generate keys in your local machine,

```bash
# generates the keys
ssh-keygen

cd .ssh
ls -a

cat id_ed25519.pub
# ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIBiZnLYtgQa5CGcpFXmr03D2AKcxnWkssjw+jArKNQf4 lenovo@LAPTOP-SLGF694A

```

2. Now, navigate to VM and allow SSH connection

```bash
mkdir -p ~/.ssh
chmod 700 ~/.ssh
nano ~/.ssh/authorized_keys

# Add this in authorized_keys file
ssh-ed25519 ....C3NzaC1lZDI1NTE5AAAAIBiZnLYtgQa5CGcpFXmr03D2AKcxnWkssjw+jArKNQf4 lenovo@LAPTOP-SLGF694B

chmod 700 ~/.ssh
chmod 600 ~/.ssh/authorized_keys
```

3. Now, Navigate to local machine and run VM

```bash
ssh debasishray864534@34.180.51.21
```

# To send file using scp

```bash
scp -r "D:\Personal_Projects\FastAPI" debasishray864534@34.180.51.21:/home/debasishray864534/Project

# adding your key
scp -i "C:\Users\Lenovo\.ssh\id_ed25519" -r "D:\Personal_Projects\FastAPI" debasishray864534@34.180.51.21:/home/debasishray864534/Project
```

# Steps to connect to github

1. Navigate to VM and create an SSH keys for it.

```bash

ssh-keygen -t ed25519 -C "debasishray3275@gmail.com"
# ssh-ed25519 ....C3NzaC1lZDI1NTE5AAAAILWmMj/rVqoczmNUoz7qw8MvhCu/WjlodCcCQv5lgAfC debasishray3275@gmail.com
chmod 700 ~/.ssh
chmod 600 ~/.ssh/authorized_keys

```

2. Navigate to GitHub -> Settings -> SSH and GPG Keys

```text

name: gcp_server_ssh
value: ssh-ed25519 ....C3NzaC1lZDI1NTE5AAAAILWmMj/rVqoczmNUoz7qw8MvhCu/WjlodCcCQv5lgAfC debasishray3275@gmail.com

```
