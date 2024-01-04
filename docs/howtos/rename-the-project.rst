======================
Rename The Project App
======================
The main/root app for the site is in the ``project`` module. This is where
``settings.py``, ``urls.py``, etc. are found. It's just a python module and
the name has no special significance other than it should be unique within
the scope of your site. If you don't like the default name, then there is a
script in the bin directory that will edit all the files where ``project``
if referenced:

..  code-block:: shell

    cd backend
    ./bin/rename-app mysite

Since this a one-time operation you can delete the script afterwards.

If you are not on a Unix-like platform, then you'll need to update the
name in the following files:

..  code-block:: docker

    # .env.example
    # line 25
    #export COMPOSE_PROJECT_NAME=project
    # line 75
    #export DATABASE_URL=postgres://project:password@localhost:5432/project

..  code-block:: docker

    # Dockerfile, line 52
    CMD ["gunicorn", "-c", "/app/backend/project/gunicorn.py", "project.wsgi"]

..  code-block:: make

    # backend/Makefile, line 18
    src_dir = $(root_dir)/project

..  code-block:: python

    # backend/manage.py, line 6
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings")

..  code-block:: python

    # backend/project/asgi.py, line 14
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings")

..  code-block:: python

    # backend/project/celery.py, line 6
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings")

..  code-block:: python

    # backend/project/settings.py
    # line 91
    ROOT_URLCONF = "project.urls"
    # line 93
    WSGI_APPLICATION = "project.wsgi.application"
    # line 121
    DATABASES = {
        "default": env.db_url(default="postgres://project:password@localhost:5432/project")
    }

..  code-block:: python

    # backend/project/wsgi.py, line 14
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings")

..  code-block:: toml

    # backend/pyproject.toml
    # line 37
    known_first_party = "project"
    # line 51
    DJANGO_SETTINGS_MODULE = "project.settings"
    # line 77
    django_settings_module = "project.settings"
    # line 93
    "project/__init__.py" = [
        '^__version__ = "{version}"$',
    ]
