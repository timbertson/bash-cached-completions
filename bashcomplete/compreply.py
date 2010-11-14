#!/usr/bin/env python
import escape
import os
import sys

def filter_matches(words, current_word):
	return [word for word in words if word.startswith(current_word)]

def concat_colons(words, current_index, argv):
	"""hack around bash's splitting of http:// into ['http', ':', '//']
	by joining up colons, matching against words, and putting
	a modified version of each word in the completions so that it'll match
	the part after the last colon"""
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
	reply = filter_matches(words, current_word)

	if non_response_chars:
		reply = map(lambda w: w[non_response_chars:], reply)
	return reply
