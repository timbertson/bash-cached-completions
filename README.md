<img src="http://gfxmonk.net/dist/status/project/bash-cached-completions.png">

An easy way to generate a set of bash completion words.
Word sets are cached, and generated in the background (so
your terminal doesn't hang).

The config is all written in python, because python is ace.
Every set of words is tied to the cache_key you generate -
if you return the same cache_key, the completion will re-use
the same set of words. If completion depends on existing
arguments, you will need to factor that into your cache_key
generation. Cache_keys need to be valid filenames, so
b32encode can be useful.


Example setup:
To enable completions for "my-command":

-----------------------------------------
~/.config/bashcomplete/my-command.py:

	max_age = 5 * 60 # 5 minutes

	def cache_key(command, args):
		import os
		import base64
		return base64.b32encode(os.getcwd())

	def get_words(command, args):
		import time
		time.sleep(2) # won't lock bash
		return ['aaa','bbbb','cccc', 'ccdd']

-----------------------------------------
~/.bashrc:

	export PATH="$PATH:/path/to/bashcomplete"
	. /path/to/bashcomplete/init


(Or, if you're using 0install) :

-----------------------------------------
~/.bashrc:

	. $(0launch -c http://gfxmonk.net/dist/0install/bashcomplete.xml __init)


