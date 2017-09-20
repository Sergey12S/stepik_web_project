path1=/home/box/web/ask

sudo ln -sf /home/box/web/etc/nginx.conf  /etc/nginx/sites-enabled/default
sudo /etc/init.d/nginx restart

sudo ln -sf /home/box/web/etc/gunicorn.conf   /etc/gunicorn.d/test
sudo /etc/init.d/gunicorn restart

cd $path1
sudo gunicorn --bind=0.0.0.0:8000 ask.wsgi:application &

sudo /etc/init.d/mysql start

