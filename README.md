tabled
======

print textual tabular data in organized form, regarding east asian width

```sh
$ cat testfile.tsv			# each space is TAB
A	B	C
abcdefghi	def	ghi
바보	멍텅구리야	한글

$ python tabled.py testfile.tsv
A            B             C   
abcdefghi    def           ghi 
바보         멍텅구리야    한글

$ # looks even better in Terminal!
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


