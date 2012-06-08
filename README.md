tabled
======

print textual tabular data in organized form, regarding east asian width


comes width: method to compute east asian width 

	>>> import tabled
	>>> tabled.width('word')
	4
	>>> tabled.width('ㅋㅋㅋㅋ')	# NOTE: not 4
	8
	>>> tabled.width(u'ㅡㅡ?')
	5
	
