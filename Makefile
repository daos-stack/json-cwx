NAME      := json-cwx
SRC_EXT   := gz

include packaging/Makefile_packaging.mk

test:
	$(call install_repos,$(NAME)@$(BRANCH_NAME):$(BUILD_NUMBER))
	yum -y install $(NAME)
	ls -al /usr/include/json-cwx
