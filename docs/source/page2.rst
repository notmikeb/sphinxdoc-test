Python modules
=======================

this is content of page2

Module List

 * `coverage <https://coverage.readthedocs.io/en/v4.5.x/>`_ - calculate code run coverage

Extra Module Usage
---------------

coverage usage `coverage <https://coverage.readthedocs.io/en/v4.5.x/>`_ - calculate code run coverage

.. code-block:: sh

  >python -m pip install coverage  
  >coverage run <your-program>
  >coverage report -m
  
builtin Module
-----------------

`sched usage <https://pymotw.com/2/sched/>`_

.. code-block:: python

  import sched
  import time

  scheduler = sched.scheduler(time.time, time.sleep)

  def print_event(name):
    print 'EVENT:', time.time(), name

  print 'START:', time.time()
  scheduler.enter(2, 1, print_event, ('first',))
  scheduler.enter(3, 1, print_event, ('second',))

  scheduler.run()


This is a statement.

.. warning::
  this is used to develop python liveimport with fronline application
  
.. code-block:: sh

  - run frontline to accept data
  "C:\Program Files (x86)\Frontline Test System II\Frontline 15\Executables\Core\Fts.exe" "/ComProbe Protocol Analysis System=Wizard"

  - use ini to connect to frontline app
  C:\Program Files (x86)\Frontline Test System II\Frontline 15
  liveimport.ini

  d:\git_home\sphinxdoc\sphinxdoc-test\docs\source\live

.. literalinclude:: scripts\live2.py

`sphinx.html <https://pythonhosted.org/an_example_pypi_project/sphinx.html#is-sweaty>`_