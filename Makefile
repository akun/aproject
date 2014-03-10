SUBDIR = ./docs
MAKE = make

all:
	make lint
	make test
	make html

lint:
	pylint --rcfile=.pylintrc dolphin -E

test:
	./bin/nosetests -c nose.cfg

html:
	cd $(SUBDIR) && $(MAKE) html
