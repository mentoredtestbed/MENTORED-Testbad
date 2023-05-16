# uwsgi --socket /tmp/mysite.sock --wsgi-file sp_django/wsgi.py --chmod-socket=666
# sudo uwsgi --socket /tmp/mysite.sock --wsgi-file sp_django/wsgi.py --chmod-socket=666 --master
sudo uwsgi --master --socket /tmp/mysite.sock --wsgi-file sp_django/wsgi.py --chmod-socket=666 --enable-threads --processes 2 --lazy-apps