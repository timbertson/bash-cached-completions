#!/usr/bin/env python
import escape
import os
import sys

def perform_completion(words, *a):
	return escape.assign_to_bash_array('COMPLETION_WORDS', words + concat_colons(words, *a))

def concat_colons(words, current_index, argv):
	current_word = argv[current_index]
	non_response_chars = 0
	if any([':' in w for w in words]):
		while current_index > 1:
			if argv[current_index-1] == ':':
				current_index -= 2
				last_word = argv[current_index]
				current_word = ":".join((last_word, current_word))
				non_response_chars += len(last_word) + 1
			else:
				break
	reply = [word for word in words if word.startswith(current_word)]

	if non_response_chars:
		reply = map(lambda w: w[non_response_chars:], reply)
	return reply

if __name__ == '__main__':
	argv = sys.argv[1:]
	separator = os.environ.get("COMPLETION_WORDS_SEP", '\n')
	words = os.environ['COMPLETION_WORDS'].split(separator)
	current_index = int(argv.pop(0))
	print perform_completion(words, current_index, argv)
