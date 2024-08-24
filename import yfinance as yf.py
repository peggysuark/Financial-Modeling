import yfinance as yf
import pandas as pd

# Define a list of stock symbols
stocks = ['AAPL', 'MSFT', 'GOOGL', 'AMZN']

# Download historical data for these stocks from Yahoo Finance
data = yf.download(stocks, start='2020-01-01', end='2023-01-01')['Adj Close']

# Display the first few rows of data
print(data.head())

# Calculate daily returns
returns = data.pct_change().dropna()

# Display the first few rows of returns
print(returns.head())

import numpy as np

# Function to calculate portfolio returns
def portfolio_returns(weights, returns):
    return np.sum(weights * returns.mean()) * 252

# Function to calculate portfolio volatility
def portfolio_volatility(weights, returns):
    return np.sqrt(np.dot(weights.T, np.dot(returns.cov() * 252, weights)))

# Function to calculate the Sharpe Ratio (assuming risk-free rate is 0 for simplicity)
def sharpe_ratio(weights, returns):
    return portfolio_returns(weights, returns) / portfolio_volatility(weights, returns)

from scipy.optimize import minimize

# Number of stocks
num_stocks = len(stocks)

# Initial weights (equal distribution)
initial_weights = np.ones(num_stocks) / num_stocks

# Constraints: weights must sum to 1
constraints = {'type': 'eq', 'fun': lambda weights: np.sum(weights) - 1}

# Bounds: weights can only be between 0 and 1
bounds = [(0, 1) for _ in range(num_stocks)]

# Optimize portfolio for maximum Sharpe ratio
optimized = minimize(lambda weights: -sharpe_ratio(weights, returns), initial_weights, 
                     method='SLSQP', bounds=bounds, constraints=constraints)

# Get the optimized weights
optimal_weights = optimized.x

# Display the optimized weights
print("Optimized Portfolio Weights:")
for stock, weight in zip(stocks, optimal_weights):
    print(f"{stock}: {weight:.2%}")

# Display the optimized portfolio's expected return and volatility
print(f"Expected Portfolio Return: {portfolio_returns(optimal_weights, returns):.2%}")
print(f"Portfolio Volatility: {portfolio_volatility(optimal_weights, returns):.2%}")

import matplotlib.pyplot as plt

# Generate random portfolio weights
num_portfolios = 10000
results = np.zeros((num_portfolios, 3))

for i in range(num_portfolios):
    weights = np.random.random(num_stocks)
    weights /= np.sum(weights)
    port_return = portfolio_returns(weights, returns)
    port_volatility = portfolio_volatility(weights, returns)
    results[i] = [port_return, port_volatility, port_return / port_volatility]

# Plot the efficient frontier
plt.scatter(results[:, 1], results[:, 0], c=results[:, 2], cmap='viridis')
plt.colorbar(label='Sharpe Ratio')
plt.xlabel('Volatility (Risk)')
plt.ylabel('Expected Return')
plt.title('Efficient Frontier')
plt.show()

