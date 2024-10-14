"""
THIS FILE DOES NOT NEED TO BE CHANGED
version of 06.05.2024
"""
import yfinance as yf

def get_current_price(ticker: str) -> int:
    """ 
    Get the last price of a stock
    ticker: ticker symbol of a stock
    """
    # Fetch data for the ticker
    stock = yf.Ticker(ticker)
    
    # Get the latest historical market data (last 5 days by default)
    history_dataframe = stock.history(period="5d")
    
    if history_dataframe.empty:
        print(f"No data available for {ticker}.")
        return None
    
    # Get the last row of the dataframe (most recent data)
    latest_data = history_dataframe.iloc[-1]
    closing_price = latest_data.Close
    date = history_dataframe.index[-1].date()  # Gets the date of the latest data
    return closing_price
        
        
def get_history(ticker: str, period="1y") -> dict:
    """
    Get the data for a stock for the last days
    ticker: ticker symbol of a stock
    period: period of the history from now; can have the format '{x}d' or '{x}y'
    example return { ... ,
        datetime.datetime(2024, 5, 3, 0, 0, tzinfo=<DstTzInfo 'America/New_York' EDT-1 day, 20:00:00 DST>): {
            'Open': 186.6699981689453, 
            'High': 187.0, 
            'Low': 182.66000366210938, 
            'Close': 183.3800048828125, 
            'Volume': 157741757, 
            'Dividends': 0.0, 
            'Stock Splits': 0.0
            }
        }
    """
    stock = yf.Ticker(ticker)
    history_dataframe = stock.history(period=period)
    
    if history_dataframe.empty:
        print(f"No data available for {ticker}.")
        return {}
    
    history_pandas_timestamp: dict = history_dataframe.to_dict('index')
    history_datetime_timestamp: dict = {
        timestamp_key.to_pydatetime(): data_day 
        for timestamp_key, data_day in history_pandas_timestamp.items()
    }
    return history_datetime_timestamp

