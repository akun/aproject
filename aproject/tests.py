#!/usr/bin/env python
# coding=utf-8


import unittest

from aproject.ship_it import ship_it

class ShipItTestCase(unittest.TestCase):

    def test_ship_it(self):
        self.assertEqual('ship it!', ship_it())
