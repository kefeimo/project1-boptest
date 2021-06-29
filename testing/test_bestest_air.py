# -*- coding: utf-8 -*-
"""
This module runs tests for bestest_air.  To run these tests, testcase
bestest_air must already be deployed.

"""

import requests
import unittest
import os
import utilities
from boptest_client import BoptestClient

class Run(unittest.TestCase, utilities.partialTestTimePeriod):
    '''Tests the example test case.

    '''

    @classmethod
    def setUpClass(cls):
        cls.name = 'bestest_air'
        cls.url = 'http://127.0.0.1:80'
        client = BoptestClient(cls.url)
        cls.testid = client.submit('testcases/{0}/models/wrapped.fmu'.format(cls.name))

    def setUp(self):
        '''Setup for each test.

        '''

        self.name = Run.name
        self.url = Run.url
        self.points_check = ['fcu_reaPCoo_y', 'fcu_reaFloSup_y',
                             'fcu_reaTSup_y', 'fcu_reaFanSet_y',
                             'zon_reaPPlu_y', 'fcu_reaPFan_y',
                             'fcu_reaPHea_y', 'zon_reaPLig_y',
                             'zon_reaTRooAir_y', 'zon_reaCO2RooAir_y',
                             'zon_weaSta_reaWeaTDryBul_y']

    def tearDown(self):
        requests.put('{0}/stop/{1}'.format(self.url, self.testid))

    def test_peak_heat_day(self):
        self.run_time_period('peak_heat_day')

    def test_peak_cool_day(self):
        self.run_time_period('peak_cool_day')

    def test_typical_heat_day(self):
        self.run_time_period('typical_heat_day')

    def test_typical_cool_day(self):
        self.run_time_period('typical_cool_day')

    def test_mix_day(self):
        self.run_time_period('mix_day')

class API(unittest.TestCase, utilities.partialTestAPI):
    '''Tests the api for testcase.

    Actual test methods implemented in utilities.partialTestAPI.  Set self
    attributes defined there for particular testcase in setUp method here.

    '''

    @classmethod
    def setUpClass(cls):
        cls.name = 'bestest_air'
        cls.url = 'http://127.0.0.1:80'
        client = BoptestClient(cls.url)
        cls.testid = client.submit('testcases/{0}/models/wrapped.fmu'.format(cls.name))

    def setUp(self):
        '''Setup for testcase.

        '''
        self.name = API.name
        self.url = API.url
        self.step_ref = 3600.0
        self.testid = API.testid
        self.test_time_period = 'peak_heat_day'

    def tearDown(self):
        requests.put('{0}/stop/{1}'.format(self.url, self.testid))

if __name__ == '__main__':
    utilities.run_tests(os.path.basename(__file__))
