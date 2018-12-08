mkdir  ..\sphinxdoc-test-docs
echo origin  https://github.com/notmikeb/sphinxdoc-test.git
cd ..\sphinxdoc-test-docs
git clone http://github.com/notmikeb/sphinxdoc-test.git html
cd html
rem del .git\index
rem git clean -fdx