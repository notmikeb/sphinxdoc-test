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

`unittest usage <https://docs.python.org/3/library/unittest.html>`_

- setup.py 加上 test_suite = {tests.my_test_suite}
- 加上 tests 子目錄, 加上"example_test.py"
- 可以在tests 目錄執行看看, python example_test.py 看看結果
- 執行python setup.py test 看看
- 執行python setup.py install --record install.log 查看install.log

.. code-block:: python
  
  """ tests/__init__.py """
  import unittest
  """
  reference
  https://stackoverflow.com/questions/17001010/how-to-run-unittest-discover-from-python-setup-py-test
  """
  def my_test_suite():
    test_loader = unittest.TestLoader()
    test_suite = test_loader.discover('tests', pattern='*.py')
    import time
    print("my_test_suite is invoked {}".format(time.time()))
    import traceback
    traceback.print_exc()
    return test_suite
  
  """ tests/example_test.py """
  import unittest

  class TestStringMethods(unittest.TestCase):

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)

  if __name__ == '__main__':
        unittest.main()

.. code-block:: python
  
  """ setup.py """
  setup(
      ....
      test_suite='tests.my_test_suite',
  )
  

 .. code-block:: python
 
    __title__ = 'pytest1'
    __version__ = '1.2.0'
    __license__ = 'Apache License, Version 2.0 and MIT License'
    __copyright__ = 'Copyright 2015 Stratos Inc. and Orion Labs'

    try:
        from setuptools import setup, find_packages
    except ImportError:
        from distutils.core import setup  # pylint: disable=F0401,E0611

    #with open('README.rst') as f:
    #    readme = f.read()
    readme = "this is readme content"
    #with open('CHANGELOG.rst') as f:
    #    changelog = f.read()
    changelog = "this is changelog content"

    setup(
        name=__title__,
        version=__version__,
        description='Python Bluetooth LE (Low Energy) and GATT Library',
        author='Chris Peplin <github@rhubarbtech.com>',
        author_email='github@rhubarbtech.com',
        packages=find_packages(exclude=("tests", "tests.*")),
        package_data={'': ['LICENSE']},
        license="Apache 2.0 and MIT",
        long_description=readme + '\n\n' + changelog,
        url='https://github.com/peplin/pygatt',
        install_requires=[
            'pyserial',
            'enum-compat'
        ],
        setup_requires=[
            'coverage >= 3.7.1',
            'nose >= 1.3.7'
        ],
        extras_require={
            'GATTTOOL': ["pexpect"],
        },
        test_suite='tests.my_test_suite',
        zip_safe=False,
        include_package_data=True,
        classifiers=(
            'Intended Audience :: Developers',
            'License :: OSI Approved :: Apache Software License',
            'License :: OSI Approved :: MIT License',
            'Programming Language :: Python',
            'Programming Language :: Python :: 2.7',
            'Programming Language :: Python :: 3',
        )
    )

  
  
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