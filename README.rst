requery
=======

Simple way to store and use queries in database for use of DBA in Django Admin

.. image:: https://d2weczhvl823v0.cloudfront.net/ebertti/requery/trend.png
.. image:: https://pypip.in/v/requery/badge.png
.. image:: https://pypip.in/d/requery/badge.png

Installation
------------

1. ``pip install requery``

2. Add ``requery`` to your ``INSTALLED_APPS`` in ``settings.py`` ::

.. code-block:: python

        INSTALLED_APPS = (
            # ...
            'requery',
        )

3. Run ``python manage.py migrate``

Screenshot
----------

1) Create and edit query

You can use ``:param_name`` to use to run your queries later.

.. image:: https://raw.githubusercontent.com/ebertti/requery/master/screenshot/change_form.png

2) Listing your queries stored in Django Admin

You can choose a query to run, just click in **Run**

.. image:: https://raw.githubusercontent.com/ebertti/requery/master/screenshot/change_list.png

3) Running and show result

Fill the form with your parameters and click in **Run** to see the results

.. image:: https://raw.githubusercontent.com/ebertti/requery/master/screenshot/running.png


Please help us
--------------
This project is still under development. Feedback and suggestions are very welcome and I encourage you to use the `Issues list <http://github.com/ebertti/requery/issues>`_ on Github to provide that feedback.

Authors
-------
The requery was original created by Ezequiel Bertti `@ebertti <https://github.com/ebertti>`_ and João Leite `@joaoleite <https://github.com/joaoleite>`_ in September 2012.

Changelog
---------

* 0.3.5.1

  * Working on Python 3 - `@tomatohater <https://github.com/tomatohater>`_
