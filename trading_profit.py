import csv
import os

# data_folder = 'data'
# file_name = 'data_17.csv'
# time_limit_low = 2
# time_limit_high = 4
data_folder = 'data'
file_name = 'data_3600.csv'
time_limit_low = 30
time_limit_high = 60


def get_max_profit_by_time_window(data, limit_low, limit_high):
    '''
    Finding the maximum profit with the given time windows
    '''
    # print(data)
    max_profit = 0
    return_trade = {}
    for i in range(limit_low, limit_high+1):
        for j in range(i, len(data)):
            # data[j-i] = 0 meaning that time is within a time-window of saved trade of last run
            if data[j-i] != 0:
                tmp_profit = round(data[j]-data[j-i], 5)
                if tmp_profit > max_profit:
                    max_profit = tmp_profit
                    return_trade = {
                        'start': j-i,
                        'end': j,
                        'start_value': data[j-i],
                        'end_value': data[j],
                        'profit': tmp_profit
                    }
    # print('trade:', return_trade)
    # print('profit:', max_profit)
    # Marking the time-window of the trade to be unavailable for next time run
    if return_trade:
        for i in range(return_trade['start'], return_trade['end']+1):
            data[i] = 0
    return max_profit, return_trade


with open(os.path.join(data_folder, file_name), 'r') as file:
    csvreader = csv.reader(file)
    # First line is headers
    headers = []
    headers = next(csvreader)
    rows = []
    for row in csvreader:
        rows.append(float(row[1]))

total_profit = 0
profit = -1
trades = []
while profit != 0:
    profit, trade = get_max_profit_by_time_window(rows, time_limit_low, time_limit_high)
    if trade:
        trades.append(trade)
        total_profit += profit

sorted_trades = sorted(trades, key=lambda d: d['start'])

print('-'*20)
for trade in sorted_trades:
    print(f'Open at {trade["start"]} ({trade["start_value"]}), close {trade["end"]} ({trade["end_value"]}) for profit'
          f' {trade["profit"]}')
print(f'Total profit {total_profit}')
