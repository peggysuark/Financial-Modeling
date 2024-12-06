import streamlit as st
from fetch_data import fetch_stock_data
from analyze_indicators import add_indicators
from visualize_data import plot_price_with_indicators
from correlation_analysis import plot_correlation_heatmap
import pandas as pd
import io


def main():
    # Sidebar for input options
    st.sidebar.title("Analysis Options")
    tickers = st.sidebar.text_input("Enter stock tickers (comma-separated):", "AAPL, MSFT, GOOG")
    start_date = st.sidebar.date_input("Start Date", value=pd.to_datetime("2024-01-01"))
    end_date = st.sidebar.date_input("End Date", value=pd.to_datetime("2024-11-29"))
    selected_indicators = st.sidebar.multiselect(
        "Select Technical Indicators",
        ["SMA", "EMA", "RSI", "Bollinger Bands"]
    )

    st.title("Comprehensive Stock Analysis Tool")
    st.write("Analyze stock price movements, calculate technical indicators, and visualize correlations.")

    # Validation for Date Range
    if start_date > end_date:
        st.error("Error: Start date must be before the end date.")
        st.stop()

    # Button to Run Analysis
    if st.button("Analyze"):
        # Loading spinner while processing
        with st.spinner("Fetching data and analyzing..."):
            try:
                # Fetch and Analyze Data
                tickers_list = [ticker.strip() for ticker in tickers.split(',')]
                data = {}
                for ticker in tickers_list:
                    st.write(f"Processing ticker: {ticker}...")
                    stock_data = fetch_stock_data([ticker], start_date, end_date)
                    if stock_data.empty:
                        st.warning(f"No data found for ticker: {ticker}")
                        continue
                    data[ticker] = add_indicators(stock_data, selected_indicators)

                if not data:
                    st.error("No valid data fetched for any of the entered tickers.")
                    st.stop()

                # Visualization in Tabs
                tabs = st.tabs(["Price Charts & Indicators", "Correlation Heatmap"])
                with tabs[0]:
                    for ticker, df in data.items():
                        st.subheader(f"Stock Price Movement and Indicators: {ticker}")
                        plot_price_with_indicators(df, selected_indicators)

                        # CSV Download Button
                        st.download_button(
                            label=f"Download Analyzed Data for {ticker} as CSV",
                            data=df.to_csv(index=False),
                            file_name=f"{ticker}_analyzed_data.csv",
                            mime="text/csv",
                        )

                with tabs[1]:
                    if len(data) > 1:
                        st.subheader("Correlation Heatmap")
                        # Combine data for correlation
                        combined_data = pd.concat(
                            [df['Close'].pct_change().rename(ticker) for ticker, df in data.items()],
                            axis=1
                        ).dropna()

                        if combined_data.empty:
                            st.error("No valid data to generate correlation heatmap.")
                        else:
                            try:
                                # Generate the heatmap
                                heatmap_fig = plot_correlation_heatmap(combined_data)

                                if heatmap_fig is None:
                                    st.error("Heatmap could not be generated. Please verify your data.")
                                else:
                                    st.pyplot(heatmap_fig)  # Display the heatmap in the app

                                    # Download heatmap as PNG
                                    buf = io.BytesIO()
                                    heatmap_fig.savefig(buf, format="png")
                                    buf.seek(0)
                                    st.download_button(
                                        label="Download Heatmap as PNG",
                                        data=buf,
                                        file_name="correlation_heatmap.png",
                                        mime="image/png",
                                    )
                            except Exception as e:
                                st.error(f"An error occurred while generating the heatmap: {e}")
                    else:
                        st.warning("Correlation heatmap requires at least two tickers with valid data.")

            except Exception as e:
                st.error("An unexpected error occurred while analyzing the data. Please check your inputs and try again.")
                st.write(f"Technical details: {str(e)}")  # Optional: Provide technical details for debugging.


if __name__ == "__main__":
    main()
