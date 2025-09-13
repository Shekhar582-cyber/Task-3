# BlockseBlock Labs - Financial Data Analysis

## Overview
This project is a comprehensive financial data analysis of Tata Motors (TATAMOTORS) stock data from 1995 to 2025. The analysis includes data cleaning, visualization, and exploratory data analysis using Python's data science libraries.

## Dataset
- **Source**: TATAMOTORS_NSE_1995-2025.csv
- **Time Period**: 1995-2025 (30 years of historical data)
- **Exchange**: National Stock Exchange (NSE)
- **Symbol**: TATAMOTORS

### Dataset Features
- **Date**: Trading date
- **Symbol**: Stock symbol (TATAMOTORS)
- **OHLC Data**: Open, High, Low, Close prices
- **Volume**: Trading volume
- **Turnover**: Total turnover
- **VWAP**: Volume Weighted Average Price
- **Trades**: Number of trades
- **Daily_Return_%**: Daily percentage returns
- **MA_20**: 20-day Moving Average
- **MA_50**: 50-day Moving Average

## Features

### Data Cleaning & Preprocessing
- Removal of unnecessary columns
- Date format conversion and validation
- Missing value handling using forward fill for moving averages
- Data type optimization and index reset

### Data Visualization
The project includes comprehensive visualizations using both Matplotlib and Seaborn:

#### Basic Visualizations
1. **Line Plot**: Close price trends over time
2. **Histogram**: Distribution of daily returns
3. **Box Plot**: Yearly distribution of closing prices
4. **Volume Analysis**: Trading volume over time
5. **Correlation Heatmap**: Relationships between financial metrics

#### Advanced Seaborn Visualizations
1. **Moving Averages**: Close price with 20-day and 50-day moving averages
2. **Volume Distribution**: Histogram with KDE of trading volume
3. **Scatter Plot**: Close price vs Volume (colored by year)
4. **Violin Plot**: Daily returns distribution by decade
5. **Pair Plot**: Correlation matrix of key financial features

### Key Insights
- **Long-term Trends**: Analysis of stock performance over 30 years
- **Volatility Analysis**: Daily returns distribution and patterns
- **Volume-Price Relationship**: Correlation between trading volume and price movements
- **Decade-wise Performance**: Comparative analysis across different market periods
- **Technical Indicators**: Moving average analysis for trend identification

## Requirements

### Python Libraries
```python
pandas>=1.3.0
matplotlib>=3.5.0
seaborn>=0.11.0
numpy>=1.21.0
```

### Installation
```bash
pip install pandas matplotlib seaborn numpy
```

## Usage

1. **Clone or Download** the project files
2. **Ensure** the dataset `TATAMOTORS_NSE_1995-2025.csv` is in the same directory
3. **Run** the Jupyter notebook `Blockseblock-labs.ipynb`
4. **Execute** cells sequentially to perform the analysis

## Project Structure
```
BlockseBlock-labs/
├── Blockseblock-labs.ipynb          # Main analysis notebook
├── TATAMOTORS_NSE_1995-2025.csv     # Stock data dataset
├── README.md                        # Project documentation
└── data/                           # Additional data files
    └── MNIST/                      # MNIST dataset (if used)
```

## Analysis Highlights

### Data Quality
- **30 years** of historical stock data
- **7,796+ trading days** analyzed
- **Comprehensive cleaning** of missing values and outliers
- **Feature engineering** with moving averages and returns

### Visualization Techniques
- **Time Series Analysis**: Long-term price trends
- **Statistical Distributions**: Return patterns and volatility
- **Comparative Analysis**: Year-over-year and decade-wise comparisons
- **Correlation Analysis**: Multi-dimensional relationships
- **Technical Analysis**: Moving average crossovers and trends

## Key Visualizations

### Stock Price Analysis
![Tata Motors Closing Price Over Time](https://github.com/Shekhar582-cyber/Task-3/blob/main/images/close_price_trend.png)
*Historical closing price showing significant volatility and multiple boom-bust cycles over 30 years*

![Close Price with Moving Averages](https://github.com/Shekhar582-cyber/Task-3/blob/main/images/moving_averages.png)
*Price trends with 20-day and 50-day moving averages for technical analysis*

### Trading Volume Analysis
![Trading Volume Over Time](https://github.com/Shekhar582-cyber/Task-3/blob/main/images/volume_trend.png)
*Trading volume evolution showing dramatic increase in activity, especially post-2016*

![Distribution of Trading Volume](https://github.com/Shekhar582-cyber/Task-3/blob/main/images/volume_distribution.png)
*Volume distribution showing heavy concentration at lower volumes with occasional spikes*

### Risk and Return Analysis
![Distribution of Daily Returns](https://github.com/Shekhar582-cyber/Task-3/blob/main/images/returns_distribution.png)
*Daily returns distribution showing right-skewed pattern with heavy negative tail*

### Correlation Analysis
![Correlation Heatmap](https://github.com/Shekhar582-cyber/Task-3/blob/main/images/correlation_heatmap.png)
*Correlation matrix showing relationships between different financial metrics*

### Multi-dimensional Analysis
![Pairplot of Key Financial Features](https://github.com/Shekhar582-cyber/Task-3/blob/main/images/pairplot.png)
*Comprehensive pairplot showing relationships between Open, High, Low, Close prices and Volume*

## Future Enhancements
- [ ] Machine learning models for price prediction
- [ ] Risk analysis and portfolio optimization
- [ ] Comparative analysis with market indices
- [ ] Real-time data integration
- [ ] Interactive dashboards using Plotly/Dash

## Contributing
This is an educational project for learning financial data analysis. Feel free to fork, modify, and enhance the analysis.

## License
This project is for educational purposes. Please ensure compliance with data usage policies when working with financial datasets.

## Contact
For questions or suggestions regarding this analysis, please open an issue in the repository.

---
*Last updated: 2024*