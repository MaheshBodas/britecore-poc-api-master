# BriteCore PoC API Server

Source code for the [BriteCore PoC Server][server].

[server]: https://github.com/MaheshBodas/britecore-poc-api-master

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)

# Set up instrctions
mkvirtualenv britecore-poc-api
setprojectdir .
git clone https://github.com/MaheshBodas/britecore-poc-api-master
workon britecore-poc-api
python manage.py makemigrations riskapi
python manage.py migrate
python manage.py shell

# Creating superuser
manage.py createsuperuser --username=mahesh.bodas --email=mahesh.bodas@gmail.com
manage.py createsuperuser --username=root --email=root@example.com --noinput

# Generating tokens
manage.py drf_create_token mahesh.bodas

# To Run test cases
python manage.py test riskapi

# Running application locally
manage.py runserver localhost:9527
manage.py runserver 127.0.0.1:9527

# Run following code to deploy it to AWS (zappa_settings.json is in repository)
pip install zappa
set AWS_ACCESS_KEY_ID={Your AWS_ACCESS_KEY_ID}
set AWS_SECRET_ACCESS_KEY={Your AWS_SECRET_ACCESS_KEY}
set AWS_DEFAULT_REGION={Your preferred region}
zappa deploy dev
