import seaborn as sns
import matplotlib.pyplot as plt


def plot_correlation_heatmap(data, figsize=(10, 8), cmap='coolwarm'):
    """
    Generate and return a correlation heatmap for the percentage change in stock prices.

    Parameters:
        data (pd.DataFrame): DataFrame containing percentage change for each stock.
        figsize (tuple): Size of the heatmap figure.
        cmap (str): Colormap for the heatmap.

    Returns:
        plt.Figure: A matplotlib figure containing the heatmap.
    """
    try:
        # Calculate correlation matrix
        corr_matrix = data.corr()

        # Create figure for heatmap
        fig, ax = plt.subplots(figsize=figsize)
        sns.heatmap(corr_matrix, annot=True, cmap=cmap, fmt='.2f', cbar=True, ax=ax)
        ax.set_title('Stock Correlation Heatmap', fontsize=16)
        ax.set_xlabel('Stocks', fontsize=12)
        ax.set_ylabel('Stocks', fontsize=12)
        return fig
    except Exception as e:
        print(f"An error occurred while generating the heatmap: {e}")
        return None
