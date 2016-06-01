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

# if task:upload is not working, use task:upload0
upload0: sdist
	python setup.py register sdist upload


install : test
	python setup.py install


# git push to github
# do `git remote add origin https://github.com/darkdarkfruit/python-adaptpath.git` first
git_push:
	git push

#  --all
#           Push all branches (i.e. refs under refs/heads/); cannot be used with other <refspec>.
git_push_all:
	git push --all


# git push only tags
git_push_tags:
	git push --tags
