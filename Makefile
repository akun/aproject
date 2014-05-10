MAKE = make

test:
	cookiecutter . --no-input && cd aproject && $(MAKE)

clean:
	rm -rf aproject
