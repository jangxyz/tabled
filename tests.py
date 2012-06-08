#!/usr/bin/python
# -*- coding: utf8 -*-

import tabled

import unittest
unittest.TestCase.eq_ = unittest.TestCase.assertEquals

class WidthTestCase(unittest.TestCase):
    def test_ascii_string_word(self):
        self.eq_(4, tabled.width('word'))
        self.eq_(5, tabled.width('^-_-^'))

    def test_ascii_unicode_word(self):
        self.eq_(4, tabled.width(u'word'))

    def test_cjk_unicode_word(self):
        self.eq_(4, tabled.width(u'한글'))
        self.eq_(8, tabled.width(u'ㅋㅋㅋㅋ'))

    def test_cjk_str_word(self):
        self.eq_(4, tabled.width('한글'))

    def test_cjk_and_ascii_mixed(self):
        self.eq_(27, tabled.width(u'한글과 english가 섞여 있음.'))
        self.eq_(5, tabled.width(u'ㅡㅡ?'))


if __name__ == '__main__':
    unittest.main()

