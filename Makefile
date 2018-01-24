PREFIX:=/usr/local
SHAREDIR:=$(PREFIX)/share/b36
BINDIR:=$(PREFIX)/bin

all:
	@echo "Usage: sudo make install"

install: env
	install -m 644 b36.py $(SHAREDIR)/
	mkdir -p $(BINDIR)
	@echo Creating $(BINDIR)/b36...
	@echo '#!/bin/sh\n$(SHAREDIR)/env/bin/python $(SHAREDIR)/b36.py "$$@"' > $(BINDIR)/b36
	chmod +x $(BINDIR)/b36

env: $(SHAREDIR)/env/bin/python

$(SHAREDIR)/env/bin/python:
	mkdir -p $(SHAREDIR)/
	virtualenv $(SHAREDIR)/env
	$(SHAREDIR)/env/bin/pip install -r requirements.txt

uninstall:
	rm -rf $(SHAREDIR)
	rm -f $(BINDIR)/b36


