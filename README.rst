Pyramid FLASH MESSAGE
=====================

Small tool to add and show flash messages
for add new message to flash message queue

.. code-block:: python

    from pyramid_flash_message import MessageQueue
    flash_message = MessageQueue()
    flash_message.add('some message')
    flash_message.add('danger message', message_type='danger')
    flash_message.add('danger message', message_type=MessageQueue.danger)

by default in instant of MessageQueue added to request object so you can use request object without importing MessageQueue

.. code-block:: python

    request.flash_message.add('some message')
    request.flash_message.add('danger message', message_type='danger')
    request.flash_message.add('danger message', message_type=request.flash_message.danger)

pyramid_flash_message use default pyramid i18n system. so you can pass `mapping` arg to use in translation.
also if you like to show source of message you can use `source` arg.

now for show flash message you can use `flash_message` panel in your templates

.. code-block:: html

    panel('flash_message', per_page=20, read=False)

for instance in jinja2 templates

.. code-block:: html

    {{ panel('flash_message', per_page=20, read=False) }}


there is also flash_message view than get `page` and `per_page` and `read` params for paged view of messages.
this params will get via GET method so you can use it via

.. code-block:: html

    <a href="{{ request.route_url('flash_message') }}">View all messages</a>
    <a href="{{ request.route_url('flash_message') }}?read=true">View and mark read</a>



Installation
------------

for installing pyrmaid_flash_message

.. code-block:: bash

    pip install pyramid_flash_message

add then add this package to your application

.. code-block:: ini

    pyramid.includes =
        pyramid_flash_message


or

.. code-block:: python

    config.include('pyramid_flash_message')


Support
-------

You can use `project issue page <https://github.com/sahama/pyramid_flash_message/issues/>`_ to submit your issue


Changes
=======

v 0.2.2
-------

 - get and use domain in translation

v 0.2.1
-------

 - add message count
 - some bugfix

v 0.2
-----

 - some bugfix and documentation

v 0.1.6
-------

 - some bugfix (now you can use it)

v 0.1
-----

 - refactor as package
 - some bugfix

v 0.0
-----

 - init project and create skeleton of it