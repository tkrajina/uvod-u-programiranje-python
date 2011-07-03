import re

file = open( "pznp.tex", "r" )
all = file.read()
file.close()

str = ""

results = re.findall( "\\\\include\{(\w+)\}.*", all )
for a in results:
	try:
		file = open( a + ".tex", "r" )
		str = str + file.read()
		file.close()
	except:
		print "Nesto nije valjalo"

# \var :
str = re.sub( "\\\\var\{([^\}]+)\}", "\\1", str )
str = re.sub( "\\\\var ", "", str )

# micanje sourcee
str = re.sub( "\\\\source\{([^\}]+)\}\{", "Listing programa (\\1): \n", str )
str = re.sub( "\\\\sourcee\{", "Listing programa (Python): \n", str )

# sad se u str nalazi sadrzaj cijele skripte u latexu

re.sub( "(a)b", "\\1x", "abcd" )
str = re.sub( "\\\\chapter\**\{([^\}]+)\}", "Poglavlje: \\1 \n", str )

# micanje \\-ova
str = re.sub( "\\\\\\\\", "", str )

# micanje $-ova
str = re.sub( "\$", "", str )

# micanje \- ova
str = re.sub( "\\\\-", "", str )

# viticaste zagrade
str = re.sub( "\\\\([\{\}])", "\\1", str )

# hrvatski palatali:
str = re.sub( "\\\\v\s{0,1}(\w)", "\\1", str )
str = re.sub( "\\\\v\{(\w)\}", "\\1", str )
str = re.sub( "\\\\'\s{0,1}(\w)", "\\1", str )
str = re.sub( "\\\\'\{(\w)\}", "\\1", str )
str = re.sub( "\\\\dj\{\}", "dj", str )

# naredbe koje jednostavno ignorira a oblika su \naredba{...}
# ostavlja ono u zagradama:
ignore = [ "emph", "footnote", "textbf", "underline", "wrd", "var", "com" ]
for x in ignore:
	str = re.sub( "\\\\" + x + "\{([^\}]+)\}", "\\1", str )

# naredbe koje potpuno ignorira
ignore2 = [ "begin", "end" ]
for x in ignore2:
	str = re.sub( "\\\\" + x + "\{[^\}]+\}", "", str )

str = re.sub( "\\\\dots", "... ", str )

# itemovi:
str = re.sub( "\s*\\\\item\[([^\]]+)\]", "\n\\1 ", str )
str = re.sub( "\s*\\\\item", "\n - ", str )

# bojanje sintakse:
str = re.sub( "\\\\textcolor{[^\}]+\}{([^\}]+)\}", "1 ", str )

str = re.sub( "\\\\addcontentsline[^\n]*", "", str )

str = re.sub( "\\\\section\**\{([^\}]+)\}", "-------------\nTema: \\1 \n", str )
str = re.sub( "\\\\subsection\**\{([^\}]+)\}", "-------------\nPodtema: \\1 \n", str )

# razmaci na pocetku:
# pripaziti da ne makne i tabove s pocetka programa!
str = re.sub( "\n[^\n\w\"\\\\\-]+", "\n", str )

str = re.sub( "\\\\hspace\*{0,1}\{10mm\}", "	", str )
str = re.sub( "\\\\hspace\*{0,1}\{20mm\}", "		", str )
str = re.sub( "\\\\hspace\*{0,1}\{30mm\}", "			", str )

print str
