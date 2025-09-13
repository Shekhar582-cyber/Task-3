import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')

# Load dataset
file_path = "TATAMOTORS_NSE_1995-2025.csv"
df = pd.read_csv(file_path)

# Data Cleaning
df = df.drop(columns=["Unnamed: 0"], errors="ignore")
df["Date"] = pd.to_datetime(df["Date"], errors="coerce")
df["MA_20"].fillna(method="ffill", inplace=True)
df["MA_50"].fillna(method="ffill", inplace=True)
df.dropna(subset=["Open", "High", "Low", "Close", "Volume"], inplace=True)
df.reset_index(drop=True, inplace=True)

# Add Year and Decade for visualization
df["Year"] = df["Date"].dt.year
df["Decade"] = (df["Year"] // 10) * 10

# Set style
plt.style.use("seaborn-v0_8")

# Create images directory if it doesn't exist
import os
os.makedirs("images", exist_ok=True)

# 1. Line plot of Close price over time
plt.figure(figsize=(12,6))
plt.plot(df["Date"], df["Close"], label="Close Price", color="blue")
plt.title("Tata Motors Closing Price Over Time")
plt.xlabel("Date")
plt.ylabel("Close Price")
plt.legend()
plt.tight_layout()
plt.savefig("images/close_price_trend.png", dpi=300, bbox_inches='tight')
plt.close()

# 2. Distribution of Daily Returns
plt.figure(figsize=(8,5))
sns.histplot(df["Daily_Return_%"], bins=50, kde=True, color="green")
plt.title("Distribution of Daily Returns (%)")
plt.xlabel("Daily Return (%)")
plt.ylabel("Frequency")
plt.tight_layout()
plt.savefig("images/returns_distribution.png", dpi=300, bbox_inches='tight')
plt.close()

# 3. Volume traded over time
plt.figure(figsize=(12,6))
plt.plot(df["Date"], df["Volume"], color="purple")
plt.title("Trading Volume Over Time")
plt.xlabel("Date")
plt.ylabel("Volume")
plt.tight_layout()
plt.savefig("images/volume_trend.png", dpi=300, bbox_inches='tight')
plt.close()

# 4. Correlation Heatmap
plt.figure(figsize=(10,7))
corr = df[["Open","High","Low","Close","Volume","Turnover","VWAP","Daily_Return_%"]].corr()
sns.heatmap(corr, annot=True, cmap="coolwarm", fmt=".2f")
plt.title("Correlation Heatmap")
plt.tight_layout()
plt.savefig("images/correlation_heatmap.png", dpi=300, bbox_inches='tight')
plt.close()

# 5. Lineplot of Close Price with Moving Averages
plt.figure(figsize=(12,6))
sns.lineplot(x="Date", y="Close", data=df, label="Close Price", color="blue")
sns.lineplot(x="Date", y="MA_20", data=df, label="MA 20", color="red")
sns.lineplot(x="Date", y="MA_50", data=df, label="MA 50", color="green")
plt.title("Close Price with Moving Averages")
plt.xlabel("Date")
plt.ylabel("Price")
plt.legend()
plt.tight_layout()
plt.savefig("images/moving_averages.png", dpi=300, bbox_inches='tight')
plt.close()

# 6. Histogram of Trading Volume
plt.figure(figsize=(8,5))
sns.histplot(df["Volume"], bins=50, kde=True, color="purple")
plt.title("Distribution of Trading Volume")
plt.xlabel("Volume")
plt.ylabel("Frequency")
plt.tight_layout()
plt.savefig("images/volume_distribution.png", dpi=300, bbox_inches='tight')
plt.close()

# 7. Pairplot of Key Features
plt.figure(figsize=(12,10))
sns.pairplot(df[["Open","High","Low","Close","Volume"]], diag_kind="kde")
plt.suptitle("Pairplot of Key Financial Features", y=1.02)
plt.tight_layout()
plt.savefig("images/pairplot.png", dpi=300, bbox_inches='tight')
plt.close()

print("All visualizations saved successfully to the images/ folder!")
print("Generated files:")
print("- close_price_trend.png")
print("- returns_distribution.png") 
print("- volume_trend.png")
print("- correlation_heatmap.png")
print("- moving_averages.png")
print("- volume_distribution.png")
print("- pairplot.png")
