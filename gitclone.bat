mkdir /p ..\sphinxdoc-test-docs
echo origin  https://github.com/notmikeb/sphinxdoc-test.git
cd ..\sphindoc-test-docs
git clone http://github.com/notmikeb/sphinxdoc-test.git html
cd html
del .git\index
git clean -fdx