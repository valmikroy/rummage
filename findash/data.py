from datetime import date
from dateutil.relativedelta import relativedelta
import yfinance as yf
import pyfredapi as pf 
from . import tech


class TickerData:
    
    def __init__(self, stock: str, history=400) -> None:
        self.name = stock 
        self.history = history
        self.window = round(history * 5/100)
    

        today = date.today().replace(month=date.today().month)
        start_date = today - relativedelta(days=self.history)       

        self.df = yf.download(self.name,
                 start=start_date,
                 end=today,
                 progress=False)
        
        self.df.reset_index(inplace=True)
        self.df.dropna(inplace=True)

    def last_price(self):
        df = self.df
        if df.empty:
            return None
        return tech.last_entry(df,'Close')

    def last_volume(self):
        df = self.df
        if df.empty:
            return None
        return tech.last_entry(df,'Volume')

    def bolinger(self):
        df = self.df
        return tech.bolinger(df,'Close',self.window)
           
    def rsi(self):
        df = self.df
        return tech.rsi(df,'Close',self.window)
        
    def macd(self,fast=12, slow=26, signal=9):
        df = self.df
        return tech.macd(df,'Close',fast,slow,signal)    

    def vol_history(self):
        df = self.df
        return tech.history(df,'Volume')    

    def price_history(self):
        df = self.df
        return tech.history(df,'Close')    

class FredData:
    def __init__(self, series: str) -> None:
        self.series = series
        self.df = pf.series.get_series(series_id=self.series)
        self.df.dropna(inplace=True)

    def last_data(self):
        df = self.df
        if df.empty:
            return None
        return tech.last_entry(df,'value')

    def bolinger(self, win=90):
        df = self.df
        return tech.bolinger(df,'value',win)
           
    def rsi(self, win=30):
        df = self.df
        return tech.rsi(df,'value',win)
        
    def macd(self,fast=13, slow=26, signal=9):
        df = self.df
        return tech.macd(df,'value',fast*5,slow*5,signal*5)    



# GDP data released twice a week so every 3 days
class GDPData(FredData):
    def __init__(self) -> None:
        super().__init__("GDP")

    # Based on the frequency there should 36 datapoints in the quarter
    def bolinger(self, win=12):
        df = self.df
        return tech.bolinger(df,'value',win)

# term premium
# Data point available for each day
class THREEFYTP10Data(FredData):
    def __init__(self) -> None:
        super().__init__("THREEFYTP10")

# real rates
# Data point available for each day
class DFII10Data(FredData):
    def __init__(self) -> None:
        super().__init__("DFII10")

# Data point is available for each month
class CPIAUCSLData(FredData):
    def __init__(self) -> None:
        super().__init__("CPIAUCSL")

# non-farm payroll data, data available each month
class PAYEMSData(FredData):
    def __init__(self) -> None:
        super().__init__("PAYEMS")

# Personal consumption expenditure data available each month
class PCEData(FredData):
    def __init__(self) -> None:
        super().__init__("PCE")
