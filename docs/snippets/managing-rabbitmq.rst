Managing RabbitMQ With Make
===========================
This code snippet contains a Makefile with targets for managing the account
used by Celery to connect a RabbitMQ broker. Save it to `backend/rabbitmq.mk`,
and it will be included by the main Makefile. IMPORTANT: Remember to convert
the indentations to tabs.

IMPORTANT: rabbitmqctl only runs on the same host as RabbitMQ. Therefore
this Makefile is only useful when you have RabbitMQ installed natively.
When running it in a container you probably have exclusive access to the
node, so the account created from the RABBITMQ_DEFAULT_USER,
RABBITMQ_DEFAULT_PASS and RABBITMQ_DEFAULT_VHOST environment variables
can be used in the CELERY_BROKER_URL without conflict.

The Makefile uses the following variables for the targets:

..  code-block::
    user=guest
    password=guest
    vhost=project

The default guest account is used, however, the vhost is specific to this
project to avoid mixing projects tasks together, even though only one may
be active at any given time.

..  code-block:: makefile
    # ############
    #   RabbitMQ
    # ############
    # Targets for managing a RabbitMQ message broker.

    # Parameters used by the commands in the targets.
    user=guest
    password=guest
    vhost=project

    .PHONY: rabbitmq-clean
    rabbitmq-clean:
        sudo rabbitmqctl delete_user $(user)
        sudo rabbitmqctl delete_vhost $(vhost)

    .PHONY: rabbitmq-init
    rabbitmq-init:
        sudo rabbitmqctl add_user $(user) $(password)
        sudo rabbitmqctl add_vhost $(vhost)
        sudo rabbitmqctl set_permissions --vhost $(vhost) $(user) ".*" ".*" ".*"
