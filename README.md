# My Portfolio

This is my personal portfolio made with Django framework in the backend
and frontend files are performed by gulp.

[![Built with Cookiecutter Django](https://img.shields.io/badge/built%20with-Cookiecutter%20Django-ff69b4.svg?logo=cookiecutter)](https://github.com/cookiecutter/cookiecutter-django/)
[![Black code style](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)

License: MIT

![Logo](https://i.postimg.cc/cH1mJV4f/saif.png)


## Demo

see the webisite in action https://saif.tn


## Features

- Light/dark mode toggle
- For Django 3.2
- Works with Python 3.9
- Twitter Bootstrap
- 12-Factor based settings via django-environ
- Secure by default. We believe in SSL.
- Optimized development and production settings
- Registration via django-allauth
- static build using Gulp and livereload
- Run tests with unittest or pytest
- Customizable PostgreSQL version
- Default integration with pre-commit for identifying simple issues before submission to code review
- Environment variables for configuration


## Run Locally

Clone the project

```bash
  git clone https://github.com/zarrai/My-Portfolio.git
```

Go to the project directory

```bash
  cd my_portfolio
```

Install dependencies

```bash
  pip -r install requirements/local.txt
```
Environment variables configuration

```
DEBUG=True
DJANGO_ALLOWED_HOSTS=
DJANGO_SECRET_KEY=
DATABASE_URL=
REDIS_URL=
DJANGO_ADMIN_URL=
DJANGO_SECURE_SSL_REDIRECT=
META_SITE_PROTOCOL=https
META_DEFAULT_KEYWORDS=
META_INCLUDE_KEYWORDS=
```

Start the server

```bash
  python manage.py migrate
  python manage.py runserver
```


## Environment Variables

To run this project, you will need to add the following environment variables to your .env file

`DEBUG`
`DJANGO_ALLOWED_HOSTS`
`DJANGO_SECRET_KEY`
`DATABASE_URL`
`REDIS_URL`
`DJANGO_ADMIN_URL`
`DJANGO_SECURE_SSL_REDIRECT`
`META_SITE_PROTOCOL`
`META_DEFAULT_KEYWORDS`
`META_INCLUDE_KEYWORDS`

### Type checks

Running type checks with mypy:

    $ mypy my_portfolio

### Test coverage

To run the tests, check your test coverage, and generate an HTML coverage report:

    $ coverage run -m pytest
    $ coverage html
    $ open htmlcov/index.html

#### Running tests with pytest

    $ pytest

### Live reloading and Sass CSS compilation

Moved to [Live reloading and SASS compilation](https://cookiecutter-django.readthedocs.io/en/latest/developing-locally.html#sass-compilation-live-reloading).

## Deployment

The following details how to deploy this application.
### Custom Bootstrap Compilation

The generated CSS is set up with automatic Bootstrap recompilation with variables of your choice.
Bootstrap v5 is installed using npm and customised by tweaking your variables in `static/sass/custom_bootstrap_vars`.

You can find a list of available variables [in the bootstrap source](https://github.com/twbs/bootstrap/blob/main/scss/_variables.scss), or get explanations on them in the [Bootstrap docs](https://getbootstrap.com/docs/5.1/customize/sass/).

Bootstrap's javascript as well as its dependencies is concatenated into a single file: `static/js/vendors.js`.
