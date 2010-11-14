#!/usr/bin/env python
import re
def bash_escape(s, inside=None):
	s = repr(str(s))[1:-1]
	s = "$'%s'" % (s,)
	if inside:
		s = "%s%s%s" % (inside, s, inside)
	return s

def assign_to_bash_array(name, a):
	result = ""
	for i, elem in enumerate(a):
		result += "%s[%s]=%s\n" % (name, i, bash_escape(elem))
	return result

if __name__ == '__main__':
	import sys
	sys.exit(0)
	import os, string
	expected = string.printable
	import subprocess
	def check_matches(expected, s):
		print repr(s)
		p = subprocess.Popen(['bash', '-c', 'echo -n ' + s], stdout=subprocess.PIPE)
		p.wait()
		result = p.stdout.read()
		print repr(result)
		assert result == expected
		print "--"
	check_matches(expected, escape(expected))
	check_matches(expected, "'%s'" % (escape(expected, inside="'")))
	check_matches(expected, '"%s"' % (escape(expected, inside='"')))
	check_matches('', escape(''))
	print "SUCCESS!"
