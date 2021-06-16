import pandas as pd
import datetime
import argparse

def generate_daily_portfolio(file):
    transaction_his = pd.read_csv(file,parse_dates=[2])
    start_date = min(transaction_his["Transaction Date"])
    stop_date = pd.to_datetime("today") 
    day = start_date + datetime.timedelta(1)
    current_portfolio = transaction_his[transaction_his["Transaction Date"]==start_date][["Scrip","Balance After Transaction"]]
    history = current_portfolio
    history["date"] = start_date
    while day < stop_date: 
        today_portfolio = transaction_his[transaction_his["Transaction Date"]==day][["Scrip","Balance After Transaction"]]
        today_portfolio = pd.concat([current_portfolio,today_portfolio])
        today_portfolio = today_portfolio.drop_duplicates(subset=["Scrip"],keep="last")
        current_portfolio = today_portfolio
        today_portfolio["date"] = day
        yield today_portfolio, day
        history = pd.concat([history,today_portfolio])
        day = day + datetime.timedelta(1)
        
def main(input_file,output_dir):
    for daily_port, date in generate_daily_portfolio(input_file):
        daily_port.to_csv(output_dir+"/"+date.strftime("%Y-%m-%d")+".csv")
        
if __name__ == "__main__": 
    parser = argparse.ArgumentParser(description="Generates daily portfolio from transaction statement")
    parser.add_argument("transaction_file",type=argparse.FileType('r'))
    parser.add_argument("--output",help="output dir",default=".")
    args = parser.parse_args()
    main(args.transaction_file,args.output)
