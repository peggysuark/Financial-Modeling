import pandas as pd
import numpy as np

def calculate_sma(data, window=20):
    """
    Calculate Simple Moving Average (SMA) for the given data.
    """
    if 'Close' not in data:
        raise ValueError("Input data must contain a 'Close' column.")
    if data.empty:
        return pd.Series(dtype=float)
    return data['Close'].rolling(window=window, min_periods=1).mean()

def calculate_ema(data, span=20):
    """
    Calculate Exponential Moving Average (EMA) for the given data.
    """
    if 'Close' not in data:
        raise ValueError("Input data must contain a 'Close' column.")
    if data.empty:
        return pd.Series(dtype=float)
    return data['Close'].ewm(span=span, adjust=False).mean()

def calculate_rsi(data, window=14):
    """
    Calculate Relative Strength Index (RSI) for the given data.
    """
    if 'Close' not in data:
        raise ValueError("Input data must contain a 'Close' column.")
    if data.empty:
        return pd.Series(dtype=float)
    
    delta = data['Close'].diff()
    gain = delta.clip(lower=0).rolling(window=window, min_periods=1).mean()
    loss = -delta.clip(upper=0).rolling(window=window, min_periods=1).mean()
    rs = gain / loss
    rsi = 100 - (100 / (1 + rs))
    return rsi

def calculate_bollinger_bands(data, window=20, num_std=2):
    """
    Calculate Bollinger Bands for the given data.
    """
    if 'Close' not in data:
        raise ValueError("Input data must contain a 'Close' column.")
    if data.empty:
        return pd.Series(dtype=float), pd.Series(dtype=float)
    
    sma = calculate_sma(data, window)
    std_dev = data['Close'].rolling(window=window, min_periods=1).std()
    upper_band = sma + num_std * std_dev
    lower_band = sma - num_std * std_dev
    return upper_band, lower_band

def add_indicators(data, indicators=["SMA", "EMA", "RSI", "Bollinger Bands"], window=20):
    """
    Add selected technical indicators to the DataFrame.
    """
    if data.empty:
        print("Empty DataFrame provided. Returning empty DataFrame.")
        return data
    
    if "SMA" in indicators:
        data['SMA'] = calculate_sma(data, window=window)
    if "EMA" in indicators:
        data['EMA'] = calculate_ema(data, span=window)
    if "RSI" in indicators:
        data['RSI'] = calculate_rsi(data, window=window)
    if "Bollinger Bands" in indicators:
        data['Upper Band'], data['Lower Band'] = calculate_bollinger_bands(data, window=window)
    
    return data
