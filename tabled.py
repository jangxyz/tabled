#!/usr/bin/python
# -*- coding: utf8 -*-

import os
import sys

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


def fill(word, length, fillchar=' '):
    return '%s%s' % (word, fillchar * (length - width(word)))

def read(filename, sep='\t', output_sep='    '):
    if not os.path.exists(filename):
        sys.stderr.write('cannot find file: %s\n' % filename)
        return

    # 1st cycle - determine max width
    maxwidths = None
    for line in open(filename):
        line = line.rstrip("\n")
        widths = (width(word) for word in line.split(sep))
        if maxwidths is None:
            maxwidths = list(widths)
            continue
        maxwidths = [max(w,max_w) for w,max_w in zip(widths, maxwidths)]

    # 2nd cycle - print
    for line in open(filename):
        words = [word for word in line.rstrip("\n").split(sep)]
        last_index = line.count(sep)
        for i,w in enumerate(words):
            sys.stdout.write(fill(w, maxwidths[i]))
            if i != last_index:
                sys.stdout.write(output_sep)
        sys.stdout.write("\n")


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Usage: %s filename' % sys.argv[0])
        sys.exit(1)

    read(sys.argv[1])


# vim: sts=4 et
