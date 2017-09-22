sudo /etc/init.d/mysql stop
sudo /etc/init.d/gunicorn stop
sudo /etc/init.d/nginx stop
sudo killall -s 9 gunicorn
