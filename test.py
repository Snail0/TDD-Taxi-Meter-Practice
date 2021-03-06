# -*- coding: utf-8 -*-

import unittest
from taxi_meter import TaxiMeter


class TaxiMeterTestCase(unittest.TestCase):

    def setUp(self):
        self.taxi_meter = TaxiMeter()
        pass

    def tearDown(self):
        pass

    # @unittest.skip('')
    def test_mile_lt_3_normal_time(self):
        self.taxi_meter.start(6.0)
        self.taxi_meter.receive(7.0, 2)
        self.assertEqual(self.taxi_meter.cash, 14)

    def test_mile_mt_3_lt_10_normal_time(self):
        self.taxi_meter.start(6.0)
        self.taxi_meter.receive(8.0, 4)
        self.assertEqual(self.taxi_meter.cash, 16.4)

    def test_mile_mt_10_normal_time(self):
        self.taxi_meter.start(6.0)
        self.taxi_meter.receive(8.0, 11)
        self.assertEqual(self.taxi_meter.cash, 14+7*2.4+1*3.6)


if __name__ == '__main__':
    unittest.main()
