Pyramid FLASH MESSAGE
=====================

Small tool to add and show flash messages

Installation
------------

.. code-block:: bash

    pip install pyramid_flash_message

add then add this package to your application

.. code-block:: ini

    pyramid.includes =
        pyramid_layout
        pyramid_jinja2
        pyramid_flash_message


or

.. code-block:: python

    config.include('pyramid_layout')
    config.include('pyramid_jinja2')
    config.include('pyramid_flash_message')


Support
-------

You can use `project issue page <https://github.com/sahama/pyramid_flash_message/issues/>`_ to submit your issue


Changes
=======


v 0.1
-----

 - refactor as package
 - some debug

v 0.0
-----

 - init project and create skeleton of it