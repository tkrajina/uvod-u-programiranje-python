#!/usr/bin/python
# -*- coding: utf-8 -*-

import re as mod_re
import sys as mod_sys

tex = mod_sys.stdin.read()

result = ''

def hspace_fix( arg ):
	group = arg.groups()[ 0 ]
	group = group.replace( 'mm', '' )
	size = int( group ) / 10
	result = ''
	for i in range( size ):
		result += '\t'
	return result

for line in tex.split( '\n' ):
	if line.strip() == '\\\\':
		pass
	else:
		line = mod_re.sub( '[^\w]\w+\{([^\}]+)\}', '\\1', line )
		line = mod_re.sub( '\$([^\$]+)\$', '\\1', line )
		line = mod_re.sub( '[^\w]hspace\*\{([^\}]+)\}', hspace_fix, line )
		result += line + '\n'

print 'Rezultat:'
print result

opis = raw_input( 'Opis?' )
datoteka = raw_input( 'Datoteka?' )

f = open( datoteka, 'w' )
f.write( result )
f.close()

print 'Latex kod:'
print '\lstinputlisting[firstline=0,language=python,caption=%s]{%s}' % ( opis, datoteka )
