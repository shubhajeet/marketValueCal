# MarketValueCal

This project was created as a project work for cloud computing by Sujit Maharjan (076MSCSK19). The program takes transaction statement of meroshare and generate the portfolio of the stocks in specified day range and create task to calcuate the market value for portfolio at each date/day.

# Method of Running and Result

``` bash
sujit@NP-SMA-MBP-01:~/cloud|⇒  time python sequential.py 
python sequential.py  54.92s user 7.44s system 66% cpu 1:34.34 total

sujit@NP-SMA-MBP-01:~/cloud|⇒  time python parallel.py  
Tasks: 100%|███████████████████████████████████████████████████████████████████████| 1495/1495 [00:19<00:00, 75.44it/s]
Tasks: 0it [00:00, ?it/s]
python parallel.py  69.98s user 8.18s system 228% cpu 34.193 total
```

