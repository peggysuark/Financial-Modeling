import yfinance as yf
import pandas as pd

def fetch_stock_data(tickers, start_date, end_date):
    """
    Fetch historical stock data for given tickers and date range.

    Parameters:
        tickers (list): List of stock tickers (e.g., ['AAPL', 'MSFT']).
        start_date (str): Start date in 'YYYY-MM-DD' format.
        end_date (str): End date in 'YYYY-MM-DD' format.

    Returns:
        pd.DataFrame: Combined stock data for all tickers with a 'Ticker' column.
    """
    combined_data = []

    for ticker in tickers:
        try:
            # Fetch stock data
            stock_data = yf.download(ticker, start=start_date, end=end_date)
            stock_data['Ticker'] = ticker
            combined_data.append(stock_data)
        except Exception as e:
            print(f"Error fetching data for {ticker}: {e}")

    # Combine all data into a single DataFrame
    if combined_data:
        return pd.concat(combined_data, ignore_index=True)
    else:
        print("No data fetched. Returning an empty DataFrame.")
        return pd.DataFrame()

def preprocess_data(data):
    """
    Prepares the data by filling missing values and calculating daily returns.

    Parameters:
        data (pd.DataFrame): Raw stock data with columns like 'Open', 'Close', etc.

    Returns:
        pd.DataFrame: Preprocessed data with filled missing values and 'Daily Return' column.
    """
    if data.empty:
        print("Empty DataFrame provided for preprocessing. Returning empty DataFrame.")
        return data
    
    data = data.copy()

    # Reset index to avoid ambiguity with 'Ticker'
    data = data.reset_index()

    # Fill missing values
    data = data.groupby("Ticker").apply(
        lambda group: group.ffill(limit=5).bfill(limit=5)
    ).reset_index(drop=True)  # Flatten the grouped data

    # Calculate daily returns
    if 'Close' in data.columns:
        data['Daily Return'] = data.groupby("Ticker")['Close'].pct_change()
    else:
        print("Column 'Close' not found in the data. Skipping Daily Return calculation.")

    return data
