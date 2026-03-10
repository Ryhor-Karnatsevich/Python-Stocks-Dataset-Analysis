SELECT date, open, close, low, high, volume, symbol
FROM stock_prices 
WHERE date >= (SELECT MAX(date) FROM stock_prices) - INTERVAL '90 days';
