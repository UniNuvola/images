FIRSTDIRS=./unihub ./unihubsingle ./unihubbackup ./base
ALLDIRS:=$(shell find . -mindepth 2 -name Makefile | xargs dirname)
DIRS:=$(FIRSTDIRS) $(filter-out $(FIRSTDIRS), $(ALLDIRS))

.PHONY: all
all: build push tag

.PHONY: build
build:
	@bash -c 'for i in $(DIRS) ; do make --no-print-directory -C $$i build ; done'

.PHONY: push
push:
	@bash -c 'for i in $(DIRS) ; do make --no-print-directory -C $$i push ; done'

.PHONY: tag
tag:
	@bash -c 'for i in $(DIRS) ; do make --no-print-directory -C $$i tag ; done'
