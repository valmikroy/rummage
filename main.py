
#from findash.index import TickerData
from findash.data import FredData
from findash.data import GDPData


#i = TickerData("META")
#i.last_price()
#print("blah")
import os 
from dotenv import load_dotenv

load_dotenv()




r = FredData("GDP")
r.print()

g = GDPData()
g.print()