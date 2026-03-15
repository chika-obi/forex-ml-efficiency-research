import yfinance as yf

pairs = ["EURUSD=X","GBPUSD=X","JPY=X"]

start = "2010-01-01"
end = "2026-01-01"

for pair in pairs:
    data = yf.download(pair,start=start,end=end)
    
    filename = pair.replace("=X","") + ".csv"
    
    data.to_csv(f"data/raw/{filename}")
    
    print(f"{filename} downloaded")
 
