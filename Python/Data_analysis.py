import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

# Open csv
df = pd.read_csv("clean_data.csv")

# Quick check
print(df.head())
print(df.shape)

# Check amount of stock tickers (7161)
unique_count = len(df['symbol'].unique())
print(unique_count)

# Grouping tickers
symbol_stats = df.groupby('symbol').agg(
    sum_volume=('volume', 'sum')
).reset_index()

# Top 20
top_20 = symbol_stats.sort_values('sum_volume', ascending=False).head(20)
top_20 = top_20.reset_index(drop=True)

# Tickers List
top_symbols = top_20["symbol"].tolist()
print(top_symbols)

# Ticker Filtration
df_top = df[df["symbol"].isin(top_symbols)]
df_top["date"] = pd.to_datetime(df_top["date"])


# Daily Return
df_top = df_top.sort_values(["symbol","date"])
df_top["daily_return"] = df_top.groupby("symbol")["close"].pct_change()


#----------------------------------------------------------------------
# Volatility
#----------------------------------------------------------------------
vol_10 = (
    df_top.groupby("symbol")
    .tail(10)
    .groupby("symbol")["daily_return"]
    .std()
)
vol_30 = (
    df_top.groupby("symbol")
    .tail(30)
    .groupby("symbol")["daily_return"]
    .std()
)
vol_90 = (
    df_top.groupby("symbol")
    .tail(90)
    .groupby("symbol")["daily_return"]
    .std()
)
vol = pd.concat( [vol_10, vol_30, vol_90] , axis=1)

vol.columns = [
    "Volatility_10_days",
    "Volatility_30_days",
    "Volatility_90_days"
]
print(vol)

#Volatility Rank
volatility_rank = vol["Volatility_30_days"].sort_values(ascending=False)
print(volatility_rank)

#----------------------------------------------------------------------
# Average volume
#----------------------------------------------------------------------
avg_10 = (
    df_top.groupby("symbol").tail(10).groupby("symbol")['volume'].mean()
)
avg_30 = (
    df_top.groupby("symbol").tail(30).groupby("symbol")['volume'].mean()
)
avg_90 = (
    df_top.groupby("symbol").tail(90).groupby("symbol")['volume'].mean()
)
avg = pd.concat(
    [avg_10,avg_30,avg_90], axis= 1)
avg.columns = [
    "Average_volume_10",
    "Average_volume_30",
    "Average_volume_90"
]
print(avg)


#----------------------------------------------------------------------
# Correlation Matrix
#----------------------------------------------------------------------
returns_table = df_top.pivot(index="date", columns="symbol", values="daily_return")
correlation = returns_table.corr()

plt.figure(figsize=(12, 8))
sns.heatmap(correlation, annot=True, cmap='coolwarm')
plt.title("Top 20 Stocks Correlation Matrix (Last 90 Days)")
plt.savefig("correlation_heatmap.png")



