#!/usr/bin/env bash
# Adding Server Header with puppet

sudo apt-get -y update 
sudo apt-get -y upgrade 
sudo apt-get -y install nginx
sudo apt-get -y install puppet
sudo service nginx start

echo "Holberton School for the win!" | sudo tee /var/www/html/index.nginx-debian.html

sudo touch /var/www/html/error404.html
sudo echo "Ceci n'est pas une page" | sudo tee /var/www/html/error404.html

find_str="^\tlocation / {"
replace_str="\tadd_header X-Served-By ${HOSTNAME}; \n\n\terror_page 404 /error404.html;\n\n\tlocation /redirect_me {\n\t\treturn 301 \$scheme://https://www.youtube.com/watch?v=QH2-TGUlwu4;\n\t}\n\n\tlocation / {"
sudo sed -i "s@${find_str}@${replace_str}@" /etc/nginx/sites-available/default

sudo service nginx restart
