.POSIX:
.PHONY: tests

# Default target.
help::
	@echo "Command  Meaning"
	@echo "-------  -------"
	@sed -n -e '/##/s/:.*\#\#/\t/p' -e '/@sed/d' Makefile

tests::  ## run the examples in the modules as tests.
	pytest --doctest-modules

format:: ## format the source files.
	black *.py
