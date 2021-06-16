from functools import partial
from taskqueue import LocalTaskQueue
import portfolio_history
import portfolio_market_value
import glob

portfolio_history.main("Transaction History.csv","daily_portfolio")
portfolios = list(glob.glob("daily_portfolio/*.csv"))
tq = LocalTaskQueue(parallel=5) # use 5 processes

tasks = ( partial(portfolio_market_value.main, i, "portfolio_value", i.split("/")[-1][:-4]) for i in portfolios ) # NEW SCHOOL

tq.insert_all(tasks) # performs on-line execution (naming is historical)

# alterternative serial model
tq.insert(tasks)
tq.execute()

tq.purge() # delete all tasks
