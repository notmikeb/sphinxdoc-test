m2r --overwrite README.md 
start cmd /c  "cd docs && make html && cd .."

start ..\sphinxdoc-test-docs\html\index.html