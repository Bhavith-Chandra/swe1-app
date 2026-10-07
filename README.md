# SWE1 Django Polls Assignment

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
