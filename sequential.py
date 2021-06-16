from functools import partial
import portfolio_history
import portfolio_market_value
import glob

portfolio_history.main("Transaction History.csv","daily_portfolio")
portfolios = list(glob.glob("daily_portfolio/*.csv"))

tasks = ( partial(portfolio_market_value.main, i, "portfolio_value", i.split("/")[-1][:-4]) for i in portfolios ) # NEW SCHOOL

for task in tasks:
    task()
