tabled
======

print textual tabular data in organized form, regarding east asian width


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
	
