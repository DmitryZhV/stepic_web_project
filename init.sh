sudo ln -s /home/box/web/etc/nginx.conf  /etc/nginx/sites-enabled/test.conf
sudo rm -rf /etc/nginx/sites-enabled/default
sudo pip install --upgrade django
sudo /etc/init.d/gunicorn stop
sudo /etc/init.d/nginx restart
mkdir /home/box/web/public
mkdir /home/box/web/public/img
mkdir /home/box/web/public/css
mkdir /home/box/web/public/js
mkdir /home/box/web/uploads
#sudo ln -s /home/box/web/etc/gunicorn.py   /etc/gunicorn.d/gunicorn.py
sudo gunicorn -b 0.0.0.0:8080 hello:app 
sudo gunicorn -b 0.0.0.0:8000 ask.wsgi:application
#sudo /etc/init.d/mysql start
