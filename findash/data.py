from datetime import date
from dateutil.relativedelta import relativedelta
import yfinance as yf
import pyfredapi as pf 




class TickerData:
    
    def __init__(self, stock: str, history=2) -> None:
        self.stock = stock 
        self.history = history
    

        today = date.today().replace(month=date.today().month)
        start_date = today - relativedelta(days=self.history)       

        self.df = yf.download(self.stock,
                 start=start_date,
                 end=today,
                 progress=False)
        
        self.df.reset_index(inplace=True)

    def last_price(self):
        df = self.df
        if df.empty:
            return None
        return round(float(df['Close'].iloc[-1]),2) 
        

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
