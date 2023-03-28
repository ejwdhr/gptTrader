import akshare as ak
stock_zh_a_hist_df = ak.stock_zh_a_hist(symbol="002090", period="daily", start_date="20230201", end_date='20230327', adjust="")
print(type(stock_zh_a_hist_df))

print(stock_zh_a_hist_df.to_json(orient='index',force_ascii=False))

