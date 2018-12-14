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
