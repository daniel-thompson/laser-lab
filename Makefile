PYTHON = python3


LIB = 96boards/ce96.py 96boards/ee96.py 96boards/iot96.py
SRC = $(filter-out $(LIB),$(wildcard 96boards/*.py paper/*.py parts/*.py private/*.py))
ART = $(SRC:.py=.svg)
DOCS = K40.html

all : $(ART) $(DOCS)

# The .svg files are checked in alongside the source as a convenience
# for people who simply want to download the artwork without cloning
# the source (or running any python)
clean :
	@echo "WARNING: clean is not implemented; touching a dependancy instead"
	touch laser/util.py

%.svg : %.py
	$(PYTHON) $< $@

%.html : %.md
	cmark $< > $@

# This is over-zealous... but safe
$(ART) : $(wildcard laser/*.py) $(LIB)
