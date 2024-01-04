==================================
Run the project using a virtualenv
==================================
This How-To shows you how to to install everything for development using a
virtual environment for python. It covers creating the virtualenv, installing
the dependencies and running the Django server.

The assumption is that you are working with a recent version of python, in
a Linux environment with `PostgreSQL <https://www.postgresql.org/download/>`_,
`RabbitMQ <https://www.rabbitmq.com/download.html>`_ and
`Memcached <https://memcached.org/downloads>`_ installed natively.

Create the basic virtual environment:

..  code-block:: shell

    cd backend
    python3.11 -m venv .venv
    source .venv/bin/activate
    pip install --upgrade pip setuptools wheel
    pip install pip-tools

Pin the package versions:

..  code-block:: shell

    pip-compile requirements/production.in
    pip-compile requirements/tests.in
    pip-compile requirements/docs.in
    pip-compile requirements/development.in

Install the dependencies:

..  code-block:: shell

    pip-sync requirements/development.txt

Run the migrations:

.. code-block:: shell

    python manage.py migrate

Bring up the site:

..  code-block:: shell

    python manage.py runserver

Create a superuser account, so you can log into the Django Admin:

..  code-block:: shell

    python manage.py createsuperuser

Using Make
----------
The project includes a Makefile which includes targets to make development
easier. All the steps above, except for creating the admin account can be
completed by running:

..  code-block:: shell

    make clean venv run

Omit the ``clean`` target if you want to keep the pinned package versions that
ship with the project.

Whenever you change any of the dependencies, ``make venv`` will recompile any
requirements source files that were edited and sync the changes to the virtualenv.
