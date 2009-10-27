subdirs = kinit

.PHONY: $(subdirs)
all: $(subdirs)
install: $(subdirs)
clean: $(subdirs)

$(subdirs):
	$(MAKE) -C "$@" $(MFLAGS) $(MAKECMDGOALS)
