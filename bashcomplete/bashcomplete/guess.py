import commands
import re
def opts(command):
	out = commands.getoutput(command + ' --help')
	options = re.findall(r'\s-[^\s=]*=?', out)
	return options
