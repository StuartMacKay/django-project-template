=======================
Django Project Template
=======================
Half the battle to create a successful project is getting everything
organized. This is a Github template repository for a Django-based website
that is runnable out of the box, using either a virtualenv or Docker.

This template is part of a family. There are  also `Related Templates`_ for
frontend frameworks and to help you deploy your site. Together, they should
get your next project off to a good start.

This project is documented in detail. There are plenty of comments describing
the what and, the why, so how the project is organised should be clear, now,
and in six months time. The docs directory also contains a set of how-tos,
showing the steps to perform various tasks and manage your project. Each
commit has a full description of why a given change was made. Extras which
are generally useful, but don't quite fit into the project are written up
in the docs snippets directory. Incorporate them if you find them useful.
There is also a `Project Board`_, where you can see what is being worked
on and what changes are planned.

.. _Project Board: https://github.com/users/StuartMacKay/projects/2

When you create a project from this template, you should replace the contents
of this file with your own.

Features
--------
This project is opinionated. It takes a good set of tools and configures them
to deliver a project that is production ready. The configuration will not to
everybody's liking but it is easy enough to change.

* For Django 4.2 LTS and Python 3.12
* Configured with `Celery: <https://docs.celeryq.dev/en/stable/>`_ for running background tasks
* Configured with `Memcached: <https://memcached.org/>`_ for caching
* Configured with `gunicorn: <https://gunicorn.org/>`_ for serving views
* Configured with `whitenoise: <//https://github.com/evansd/whitenoise>`_ for serving static files
* Configured with `Sentry: <https://sentry.io/>`_ for error reporting
* Configured with `python-json-logger: <https://github.com/madzak/python-json-logger>`_ for logging
* Development with `black: <https://github.com/psf/black>`_ so everybody gets the code formatting rules they deserve
* Development with `flake8: <https://flake8.pycqa.org/en/latest/>`_ so people using ed get syntax checking
* Development with `isort: <https://pycqa.github.io/isort/>`_ for automatically sorting imports
* Development with `mypy: <https://mypy-lang.org/>`_ for type-hinting to catch errors
* Development with `pre-commit: <https://pre-commit.com/>`_ git hooks for running code checks
* Testing with `pytest: <https://docs.pytest.org/>`_ and `FactoryBoy: <https://factoryboy.readthedocs.io/en/stable/>`_
* Manage versions with `bumpver: <https://github.com/mbarkhau/bumpver>`_ - for semantic or calendar version numbers
* Manage dependencies with `pip-tools: <https://github.com/jazzband/pip-tools>`_

Prerequisites
-------------
If you want to run the site using a virtualenv, then you will need to install
`PostgreSQL`_, `RabbitMQ`_ and `Memcached`_. If you intend to use containers
then you will need to install `Docker Engine` and `Docker Compose`_, Version 2,
or `Docker Desktop`_.  Of course, you can mix the two together and run any
combination of the backend services from native installs or in containers.

.. _PostgreSQL: https://www.postgresql.org/download/
.. _RabbitMQ: https://www.rabbitmq.com/download.html
.. _Memcached: https://memcached.org/downloads
.. _Docker Engine: https://docs.docker.com/engine/
.. _Docker Compose: https://github.com/docker/compose
.. _Docker Desktop: https://docs.docker.com/desktop/

Project Layout
--------------
The templates are organised around three top-level directories for code and
two run-time directories for storing and serving files.

..  code-block:: shell

    .
    ├── backend
    ├── deploy
    ├── frontend
    ├── media
    └── static

The ``backend`` directory contains core set of files for a Django site. The
``frontend`` is the integration point for templates containing frontend
(javascript and/or css) frameworks and ``deploy`` is integration point for
the files used to deploy the site.

The only point of coupling between a frontend and a backend project is
STATIC_FILES_DIR setting which points to the ``frontend/dist`` where static
assets are built in frontend templates. The collectatic management command
can then copy the assets to the ``static`` directory where they can be served
by whitenoise or a reverse proxy such as nginx.

Finally, the ``media`` directory is only created if you use the local
filesystem for storage, either in development or in single server production
environment.

Organising around top-level directories makes the project modular and easy to
divide responsibilities across different teams. It can also be extended, for
example to add a ``backups`` directory in production for database dumps. That
way everything is located in one space and easy to manage.

The organsiation of the Django files in the backend is reasonably standard:

..  code-block:: shell

    .
    ├── backend
    │   ├── manage.py
    │   ├── bin
    │   ├── project
    │   │   ├── apps
    │   │   ├── asgi.py
    │   │   ├── celery.py
    │   │   ├── gunicorn.py
    │   │   ├── settings.py
    │   │   ├── static
    │   │   ├── templates
    │   │   │   ├── base.html
    │   │   │   ├── robots.txt
    │   │   │   └── site
    │   │   │       └── index.html
    │   │   ├── tests
    │   │   ├── urls.py
    │   │   ├── views
    │   │   │   ├── index.py
    │   │   │   ├── robots.py
    │   │   │   └── sitemap.py
    │   │   └── wsgi.py
    │   ├── .env.example
    │   ├── .envrc
    │   ├── docker-compose.override.yml.example
    │   ├── docker-compose.yml
    │   ├── Dockerfile
    │   ├── Makefile
    │   ├── pyproject.toml
    │   └── requirements
    │       ├── development.in
    │       ├── docs.in
    │       ├── production.in
    │       └── tests.in
    └── docs
        ├── howtos
        └── snippets

The ``backend`` directory contains the configuration files for the project
tooling (Docker, etc.) The ``requirements`` are divided into separate files
so only the dependencies for production or testing are installed. The code
for Django is organised into a root ``project`` module. This in turn has
all the configuration files needed to run the site.

The ``apps`` module is where you add your code. This is more or less for
aesthetic reasons than anything else. It keeps all the project related
code under one tree, so imports take the form:

..  code-block:: python

    from project.apps.reports import models

That way you can easily see which imports are from the project and which
are from third-party libraries. It is simply a preference, since the
``backend`` directory is on the python path, ypu could add the apps there.
Imports would then take the form:

..  code-block:: python

    from reports import models

The only downside is more clutter in the ``backend`` directory, which is
entirely subjective.

The root module is named ``project`` purely as a default. Typically, this is
named after the project/site, however, since it's just a python module, as long
it is unique for the site, the name does not really matter. However, if you want
to rename it then there is a script that will take care of it:

..  code-block:: shell

    cd backend
    ./bin/rename-app <new name>

Since this a one-time operation you can delete the script afterwards.

If you are not using a Unix-like platform then you'll need to edit the files
manually. The How-To, "Rename The Project App" in the docs directory lists
all the files, with the line numbers that need to change.

How To Run
----------
The project has sensible defaults and will run out of the box, using either
a virtualenv or Docker, so you don't need to set any environment variables
to get started.

..  code-block:: shell

    cd backend

For a virtualenv, it is as simple as:

..  code-block:: shell

    make venv run

For docker:

..  code-block:: shell

    docker compose up

If you don't want to use the Makefile then there is a guide in the How-Tos
section of the docs, "Using Virtualenv", which will take you through all
the steps.

If you need to customise things, port numbers, for example, then the full
set of environment variables used can be found in ``.env.example``. Create
a copy and edit as needed:

..  code-block::

    cp .env.example .env

The environment variables are exported, so if you use a Unix-like operating
system you can set them by running:

..  code-block::

    source .env

Also, `direnv`_ is particularly handy. When you cd to the project directory,
the direnv config file, ``.envrc``, a) activates the virtualenv (if it exists)
and, b) sets environment variables for everything in the .env file.

.. _direnv: https://direnv.net/

The Docker files are intended for a production deploy, with storage managed
by the Docker Engine. For development, there is an override file which maps
the services to local port numbers and define mount points for project files:

..  code-block::

    cp docker-compose.override.yml.example docker-compose.override.yml

Related Templates
-----------------
This template contains the core files needed for a Django-based site. There
are a number of related template for different frontend and deployment options.

+-----------------=------------+----------------------------------------------------------+
| Project                      | Description                                              |
+==============================+==========================================================+
| `django-ansible-template`_   | Adds files to deploy to a VPS using Ansible              |
+------------------------------+----------------------------------------------------------+
| `django-bootstrap-template`_ | Adds files to create a customized version of Bootstrap 5 |
+------------------------------+----------------------------------------------------------+

To use these, simply checkout the template at the integration points mentioned
in the `Project Layout`_ section:

..  code-block::

    git clone git@github.com:StuartMacKay/django-ansible-template.git deploy
    git clone git@github.com:StuartMacKay/django-template-template.git frontend

Incidentally, if you are looking for a template to create a project for a reusable
Django app, then take a look at `django-app-template`_

.. _django-ansible-template: https://github.com/StuartMacKay/django-ansible-template
.. _django-bootstrap-template: https://github.com/StuartMacKay/django-bootstrap-template
.. _django-app-template: https://github.com/StuartMacKay/django-app-template

Acknowledgements
----------------
The production Docker files were based on Nick Janetakis' rather excellent
`docker-django-example`_, with a few tweaks, of course. His `Docker Tips`_
are packed with interesting and useful information. Highly recommended (not
affiliated, just grateful).

.. _docker-django-example: https://github.com/nickjj/docker-django-example/
.. _Docker Tips: https://nickjanetakis.com/blog/tag/docker-tips-tricks-and-tutorials
