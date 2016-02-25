files = adaptpath/version.py adaptpath/adaptpath.py
file_pytest_genscript = adaptpath/_test_adaptpath_pytest.py

default: test
	echo ''



test: ${files}
	echo ''
	echo '==> use "pytest test" directly: '
	pytest test 
	echo ''
	echo '==> use "python setup.py test": '
	python setup.py test

# just pytest adaptpath
stest: 
	pytest test 


# make a source distribution in dist/
sdist: ${files} test
	python setup.py sdist


# upload to pypi
upload: sdist
	python setup.py sdist upload


install : test
	python setup.py install


# git push to github
# do `git remote add origin https://github.com/darkdarkfruit/python-adaptpath.git` first
git_push:
	git push 


# git push with tags
git_push_tags:
	git push --tags