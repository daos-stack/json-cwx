NAME      := json-cwx
SRC_EXT   := gz
SOURCE     = https://github.com/LLNL/$(NAME)/archive/$(NAME)-$(VERSION).tar.$(SRC_EXT)

include packaging/Makefile_packaging.mk
