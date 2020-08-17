# -*- coding: utf-8 -*-
from unittest import TestCase
import unittest
from bowling import check_errors, get_score


class Test(TestCase):

    def test_check_errors(self):
        with self.assertRaises(ValueError):
            check_errors('XX4-/1744XX23--4/')
            # check_errors('/34-/1744XX23--4/')
            # check_errors('X340/1744XX23--4/')

        # self.assertRaises(ValueError, check_errors, 'X340/1744XX23--4/')

    def test_get_score(self):
        with self.assertRaises(Exception):
            get_score('1744XX23--4/')


if __name__ == '__main__':
    unittest.main()