PYTHON = python3


LIB = 96boards/ce96.py 96boards/ee96.py 96boards/iot96.py
SRC = $(wildcard 96boards/*.py paper/*.py parts/*.py private/*.py ukulele/*.py)
ART = $(SRC:.py=.svg)
DOCS = K40.html

all : $(ART) $(DOCS)

# The .svg files are checked in alongside the source as a convenience
# for people who simply want to download the artwork without cloning
# the source (or running any python)
clean :
	@echo "WARNING: svg files will not be cleaned; touching a dependancy instead"
	touch laser/util.py
	$(RM) $(DOCS)

%.svg : %.py
	$(PYTHON) $< $@

%.html : %.md
	cmark $< > $@

# This is over-zealous... but safe
$(ART) : $(wildcard laser/*.py) $(LIB)
