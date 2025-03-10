import unittest
import pandas as pd
import os 

from findash.data import TickerData
from findash.data import FredData
from mock import patch

from dotenv import load_dotenv

load_dotenv(dotenv_path = os.path.dirname(os.path.realpath(__file__)) + '../')




class TestTicker(unittest.TestCase):
    def setUp(self) -> None:
        dir_path = os.path.dirname(os.path.realpath(__file__))
        test_data = dir_path + "/fixtures/meta_ticker.data"
        with patch.object(TickerData,"__init__", lambda x, z:None):
            self.ticker = TickerData('')
            self.ticker.name = 'META'
            self.ticker.history = 2
            self.ticker.df = pd.read_pickle(test_data)
        
    def testLastData(self):
        self.assertEqual(self.ticker.last_price(),591.24)
        self.assertEqual(self.ticker.bolinger(),[582.33, 609.67, 637.0])
        self.assertEqual(self.ticker.rsi(),40.15)




class TestFred(unittest.TestCase):
    def setUp(self) -> None:
        dir_path = os.path.dirname(os.path.realpath(__file__))
        test_data = dir_path + "/fixtures/DFII10.data"
        with patch.object(FredData,"__init__", lambda x, z:None):
            self.d = FredData('')
            self.d.series= 'DFII10'
            self.d.df = pd.read_pickle(test_data)
        
    def testLastData(self):
        self.assertEqual(self.d.last_data(),2.24)
