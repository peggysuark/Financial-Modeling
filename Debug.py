from fetch_data import fetch_stock_data
from correlation_analysis import plot_correlation_heatmap

# Fetch stock data
tickers = ['AAPL', 'MSFT', 'GOOG']
start_date = '2023-01-01'
end_date = '2023-12-01'
data = fetch_stock_data(tickers, start_date, end_date)

# Plot correlation heatmap
plot_correlation_heatmap(data)
