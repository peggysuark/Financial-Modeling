import matplotlib.pyplot as plt

def plot_price_with_indicators(data, indicators=["SMA", "EMA", "RSI", "Bollinger Bands"]):
    """
    Plot stock prices along with selected technical indicators.

    Parameters:
        data (pd.DataFrame): DataFrame containing stock data and technical indicators.
        indicators (list): List of indicators to plot (default includes all supported indicators).

    Returns:
        None: Displays the plot.
    """
    if data.empty:
        print("No data to plot.")
        return

    # Plot Close Price
    plt.figure(figsize=(14, 8))
    plt.plot(data.index, data['Close'], label='Close Price', linewidth=2)

    # Plot Indicators
    if "SMA" in indicators and "SMA" in data.columns:
        plt.plot(data.index, data['SMA'], label='Simple Moving Average (SMA)')
    if "EMA" in indicators and "EMA" in data.columns:
        plt.plot(data.index, data['EMA'], label='Exponential Moving Average (EMA)')
    if "Bollinger Bands" in indicators and "Upper Band" in data.columns and "Lower Band" in data.columns:
        plt.fill_between(
            data.index, data['Upper Band'], data['Lower Band'], 
            color='gray', alpha=0.3, label='Bollinger Bands'
        )

    # Add labels, legend, and grid
    plt.title("Stock Price with Indicators", fontsize=16)
    plt.xlabel("Date", fontsize=12)
    plt.ylabel("Price", fontsize=12)
    plt.legend()
    plt.grid()
    plt.show()

def plot_rsi(data):
    """
    Plot the Relative Strength Index (RSI).

    Parameters:
        data (pd.DataFrame): DataFrame containing stock data with an 'RSI' column.

    Returns:
        None: Displays the RSI plot.
    """
    if "RSI" not in data.columns:
        print("RSI column not found in data. Cannot plot RSI.")
        return

    plt.figure(figsize=(14, 4))
    plt.plot(data.index, data['RSI'], label='Relative Strength Index (RSI)', color='purple', linewidth=2)
    plt.axhline(70, color='red', linestyle='--', label='Overbought (70)')
    plt.axhline(30, color='green', linestyle='--', label='Oversold (30)')
    plt.title("Relative Strength Index (RSI)", fontsize=16)
    plt.xlabel("Date", fontsize=12)
    plt.ylabel("RSI", fontsize=12)
    plt.legend()
    plt.grid()
    plt.show()
