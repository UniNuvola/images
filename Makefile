DIRS=unihub \
unihubsingle \
unihubbackup \
base \
base/conda \
base/conda/pytorch \
base/conda/pytorch-gpu \
base/engineering \
basedev

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
