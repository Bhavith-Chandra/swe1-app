# SWE1 Django Polls Assignment

[![Build Status](https://app.travis-ci.com/Bhavith-Chandra/swe1-app.svg?branch=main)](https://app.travis-ci.com/github/Bhavith-Chandra/swe1-app)
[![Coverage Status](https://coveralls.io/repos/github/Bhavith-Chandra/swe1-app/badge.svg?branch=main)](https://coveralls.io/github/Bhavith-Chandra/swe1-app?branch=main)

Deployed app: http://swe1-app-env.eba-3igipvfy.us-east-2.elasticbeanstalk.com/polls/

Django polls application following Django tutorial parts 1-4, with AWS Elastic Beanstalk deployment configuration.

## Local setup

```bash
python3.12 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Open http://127.0.0.1:8000/polls/

After creating a question and choices in `/admin/`, the poll will appear on the public page.

## AWS Elastic Beanstalk

```bash
eb init
eb create swe1-django-env
eb status
```

After `eb status`, add the Elastic Beanstalk CNAME to `ALLOWED_HOSTS` in `mysite/settings.py`, then:

```bash
eb deploy
eb open
```

## Continuous integration

Travis CI runs on every push and pull request:

```bash
black --check .
flake8
coverage run manage.py test
coveralls
```

Successful builds on `main` deploy to Elastic Beanstalk (`swe1-app-env`).
