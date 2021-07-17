### Setup and run celery with rabbitmq ###
* install celery using pip
* install rabbitmq - sudo apt-get install rabbitmq-server
* sudo systemctl enable rabbitmq-server
  
* Create user - sudo rabbitmqctl add_user username password
* Create vhost - sudo rabbitmqctl add_vhost vhost_name
* Set tags - sudo rabbitmqctl set_user_tags username mytag
* Assign permissions - sudo rabbitmqctl set_permissions -p vhost_name username ".*" ".*" ".*"
* start your server using command: sudo systemctl start rabbitmq-server
* check rabbitmq is running using command: sudo systemctl status rabbitmq-server
  
* RUN celery using command: celery -A celeryproject worker -l info --concurrency=1
* RUN celery beat for daily horoscope notification: celery -A celeryproject beat -l INFO
* worker and beat together: celery -A celeryproject worker --beat -l info --concurrency=1