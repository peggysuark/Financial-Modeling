# Top 10 Plotting and Visualization Libraries for Financial Analysts

# Importing the required library for system commands
import os

# List of libraries to install and brief descriptions
libraries = {
    "matplotlib": "A comprehensive library for creating static, animated, and interactive visualizations in Python.",
    "seaborn": "A statistical data visualization library based on Matplotlib, providing a high-level interface for drawing attractive graphs.",
    "pandas": "Though primarily a data manipulation library, Pandas integrates with Matplotlib to enable quick plotting directly from DataFrames.",
    "plotly": "A graphing library that makes interactive, publication-quality graphs online. It's known for its wide variety of plots and dashboards.",
    "bokeh": "An interactive visualization library for modern web browsers, capable of handling big data and streaming data.",
    "altair": "A declarative statistical visualization library for Python, based on Vega and Vega-Lite visualization grammars.",
    "ggplot": "A plotting system for Python based on the grammar of graphics, originally implemented in R's ggplot2.",
    "holoviews": "A library designed to make data analysis and visualization seamless and simple, leveraging Matplotlib and Bokeh.",
    "cufflinks": "A library that connects Plotly with Pandas to create graphs and charts directly from DataFrames.",
    "mplfinance": "A library specifically designed for financial data visualization, making it easy to create financial market charts like candlesticks."
}

# Function to install the libraries using pip
def install_libraries():
    for lib in libraries:
        print(f"Installing {lib}...")
        os.system(f"pip install {lib}")
    print("\nAll libraries installed successfully!")

# Function to print descriptions of each library
def describe_libraries():
    print("\nDescriptions of Top 10 Plotting and Visualization Libraries for Financial Analysts:\n")
    for lib, desc in libraries.items():
        print(f"{lib}:\n{desc}\n")

# Main function to run the installation and descriptions
def main():
    install_libraries()
    describe_libraries()

if __name__ == "__main__":
    main()
