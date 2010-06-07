VERSION=0.1
NAME=bashcomplete
FILES=cached-completion 0init init

BUILD=0inst

package:
	mkdir -p $(BUILD)
	tar czf $(BUILD)/$(NAME)-$(VERSION).tgz $(FILES)
	0publish-gfxmonk "$(NAME)" "$(VERSION)"

upload:
	make sync
	(cd ~/Sites/gfxmonk && make upload)

sync:
	(cd ~/Sites/gfxmonk && rsync -r --delete dist _site/)

0: package copy upload
