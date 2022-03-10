## Prerequisite
You must have installed python3

## Checkout the code
```
git clone https://github.com/vuluc88/profit_trade.git
```

## Config
Open file trading_profit.py
edit `file_name` variable to the test file

## Run code
```commandline
python trading_profit.py
```

## How it's done
- Given the time-window, scan through the whole list to get the most profit one
- Do it again until can't find anymore trade

Example:
Let made the requirement simpler, instead of 30mins to 60 mins, let's narrow it down so a trade must within min 2 mins and max 4 mins  
So for example we got this list:  
[1, 2, 3, 10, 2, 1]  
First run:  
2 mins window: [0, 0, 2, 8, -1, -9]  
Above list record the profit of each time position IF I trade it in [2] mins before  
So for next we got these 2:  
3 mins window: [0, 0, 0, 9, 0, -2]  
4 mins window: [0, 0, 0, 0, 1, -1]  
  
So with all above infos, the max profit would be with the trade 0(1) and 3(10)  
Then I pick the trade, which mean that time-window is unavailable, which made the original list become:  
[0, 0, 0, 0, 2, 1]  
Looping and run the whole process again until no profit can be make