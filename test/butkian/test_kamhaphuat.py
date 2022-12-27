# -*- coding: utf-8 -*-
from unittest.case import TestCase
from kesi import kam_haphuat


class TestKamHaphuat(TestCase):

    def test_正常情形(self):
        self.assertTrue(kam_haphuat('tâi'))

    def test_數字調(self):
        self.assertTrue(kam_haphuat('tai5'))

    def test_毋是台語的音節(self):
        self.assertFalse(kam_haphuat('siid'))

    def test_漢字(self):
        self.assertFalse(kam_haphuat('台'))

    def test_超過一个音節(self):
        self.assertFalse(kam_haphuat('tâi-gí'))

    def test_空字串(self):
        self.assertFalse(kam_haphuat(''))
