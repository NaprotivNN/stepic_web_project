sudo ln -sf /home/box/web/etc/nginx.conf /etc/nginx/sites-enabled/default
sudo /etc/init.d/nginx restart

sudo ln -sf /home/box/web/etc/hello.py /etc/gunicorn.d/hello.py

sudo /etc/init.d/gunicorn restart

#sudo gunicorn -c /home/box/web/etc/gunicorn.conf hello:wsgi_application
#sudo gunicorn -c /home/box/web/etc/gunicorn-django.conf ask.wsgi:application

#sudo gunicorn -c hello.py hello:wsgi_app

#вместо 2х верхних строчек можно написать и так,но тогда в hello.py нужно добавить
#bind='0.0.0.0:8080'

