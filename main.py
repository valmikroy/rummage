
#from findash.index import TickerData
from findash.data import FredData
from findash.data import GDPData
from findash.data import DFII10Data


#i = TickerData("META")
#i.last_price()
#print("blah")
import os 
from dotenv import load_dotenv

load_dotenv()




#r = FredData("GDP")
#r = FredData("THREEFYTP10")
r = DFII10Data()