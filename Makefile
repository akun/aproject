SRC_DIR = aproject
DOC_DIR = docs
MAKE = make

all:
	make lint
	make test
	make html
	make clean

lint:
	pylint --rcfile=.pylintrc -E $(SRC_DIR)

lintall:
	pylint --rcfile=.pylintrc $(SRC_DIR)

test:
	nosetests -c nose.cfg

html:
	cd $(DOC_DIR) && $(MAKE) html

clean:
	rm -rf *.egg-info
	rm -rf build/*
	rm -rf dist/*
	rm -rf $(SRC_DIR)/*.egg-info
	find $(SRC_DIR) -name "*.pyc" | xargs rm
