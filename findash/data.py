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



    def last_price(self):
        df = self.df
        if df.empty:
            return None
        return tech.last_price(df)

    def last_volume(self):
        df = self.df
        if df.empty:
            return None
        return tech.last_volume(df)

    def bolinger(self):
        df = self.df
        return tech.bolinger(df,self.window)
           
    def rsi(self):
        df = self.df
        return tech.rsi(df,self.window)
        
    def macd(self,fast=12, slow=26, signal=9):
        df = self.df
        return tech.macd(df,fast,slow,signal)    

    def vol_history(self):
        df = self.df
        return tech.vol_history(df)    

    def price_history(self):
        df = self.df
        return tech.price_history(df)    

class FredData:
    def __init__(self, series: str) -> None:
        self.series = series
        self.df = pf.series.get_series(series_id=self.series)

    def last_data(self):
         return round(float(self.df['value'].iloc[-1]),2)




class GDPData(FredData):
    def __init__(self) -> None:
        super().__init__("GDP")


class THREEFYTP10Data(FredData):
    def __init__(self) -> None:
        super().__init__("THREEFYTP10")


class DFII10Data(FredData):
    def __init__(self) -> None:
        super().__init__("DFII10")
