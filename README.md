tabled
======

print textual tabular data in organized form, regarding east asian width

```python
$ cat testfile.tsv			# each space is TAB
A	B	C
abcdef	def	ghi
한글	바보	멍텅구리야

$ python tabled.py testfile.tsv
A         B       C         
abcdef    def     ghi       
한글      바보    멍텅구리야
```


comes _width_: method to compute **east asian width** 

```python
>>> import tabled
>>> tabled.width('word')
4
>>> tabled.width('ㅋㅋㅋㅋ')	# NOTE: not 4
8
>>> tabled.width(u'ㅡㅡ?')
5
```
	
