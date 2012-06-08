#!/usr/bin/python
# -*- coding: utf8 -*-

def east_asian_width(letter):
    import unicodedata
    '''According to Unicode Annex 11, every unicode has a property called 
    East Asian Width Property, which is one of the following six values:
    
        Ambiguous, Fullwidth, Halfwidth, Narrow, Wide, or Neutral (= Not East Asian) 

    denoted as 'A', 'F', 'H', 'Na', 'W' and 'N', repsectively.
    
    Fullwidth and Wide are known to take up of length 2.

    read doc/EastAsianWidth-6.1.0.txt for further details.
    '''
    return {
        'W'  : 2,
        'F'  : 2,
        'A'  : 1,
        'H'  : 1,
        'Na' : 1,
        'N'  : 1,
    }[unicodedata.east_asian_width(letter)]


def width(word, encoding='utf8'):
    ''' width of given str/unicode, regarding east asian width '''
    if isinstance(word, str):
        word = word.decode(encoding)
    return sum(east_asian_width(letter) for letter in word)



# vim: sts=4 et
