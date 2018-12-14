RST links
######################

title
****************
this is content of rst

include-raw-code-block
**************

* basic intro `http://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html <http://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html>`_

.. code-block:: rst
  
  表示外部的連結
  `text <link>`_

* code intro `http://www.sphinx-doc.org/en/1.5/markup/code.html <http://www.sphinx-doc.org/en/1.5/markup/code.html>`_

* this uses literalinclude directive
.. literalinclude:: setup_1.py
 
* this use code-block directive
.. code-block:: python

	from setuptools import setup

	test_deps = [
		'coverage',
		'pytest',
	]
	extras = {
		'test': test_deps,
	}

	#setup(
	## Other metadata...
	#    tests_require=test_deps,
	#    extras_require=extras,
	#)



show title 
`<http://www.kimo.com.tw>`_

* :ref:`page1a`
* :ref:`page1b`