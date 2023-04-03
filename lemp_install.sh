#!/bin/bash

# Update the package index and upgrade all installed packages
sudo apt update && sudo apt upgrade -y

# Install Nginx, MySQL, and PHP
sudo apt install -y nginx mysql-server php-fpm php-mysql

# Secure MySQL installation and set authentication method to mysql_native_password
sudo mysql -e "ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY '';"
echo -e "n\ny\ny\ny\nn" | sudo mysql_secure_installation

# Configure Nginx to use PHP
sudo sed -i 's/index.html index.nginx-debian.html/index.php index.html index.nginx-debian.html/g' /etc/nginx/sites-available/default
sudo sed -i 's/# location ~ \\\.php$ {/location ~ \\\.php$ {/g' /etc/nginx/sites-available/default
sudo sed -i 's/#\tinclude snippets\\/fastcgi-php.conf;/\tinclude snippets\\/fastcgi-php.conf;/g' /etc/nginx/sites-available/default
sudo sed -i 's/#\tfastcgi_pass unix:\/var\/run\/php\/php7.4-fpm.sock;/\tfastcgi_pass unix:\/var\/run\/php\/php7.4-fpm.sock;/g' /etc/nginx/sites-available/default
sudo sed -i 's/#}/}/g' /etc/nginx/sites-available/default

# Restart Nginx and PHP-FPM
sudo systemctl restart nginx php7.4-fpm
