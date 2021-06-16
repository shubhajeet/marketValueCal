import pandas as pd
import argparse
from taskqueue import queueable

price_his = pd.read_csv("price_history.csv")
price_his.AsOfDate = pd.to_datetime(price_his.AsOfDate)

def calculate_market_value(input_file,date):
    daily_port = pd.read_csv(input_file)
    daily_port.date = pd.to_datetime(date)
    dt = daily_port.merge(price_his,right_on=["StockSymbol","AsOfDate"],left_on=["Scrip","date"])
    dt["Amount"] = dt["Balance After Transaction"] * dt["ClosingPrice"]
    return dt.groupby(["date"])[["Amount"]].sum()

@queueable    
def main(input_file,output_dir,date):
    calculate_market_value(input_file,date).to_csv(output_dir+"/"+date+".csv")
    
if __name__ == "__main__": 
    parser = argparse.ArgumentParser(description="Calculates the daily portfolio market value")
    parser.add_argument("portfolio",type=argparse.FileType('r'))
    parser.add_argument("date",help="date in %Y-%m-%d format")
    parser.add_argument("--output",help="output dir",default=".")
    parser.add_argument("--price_his",help="price history csv",default="price_history.csv")
    args = parser.parse_args()
    price_his = pd.read_csv(args.price_his)
    price_his.AsOfDate = pd.to_datetime(price_his.AsOfDate)
    main(args.portfolio,args.output,args.date)
