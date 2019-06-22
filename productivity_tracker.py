import datetime
import time
now = datetime.datetime.now()
currentdate = now.strftime("%Y-%m-%d")
print(currentdate)
import csv
import pandas as pd
from plyer import notification
new_focus = True
import matplotlib.pyplot as plt

csv_source = 'productivity.csv'
activities = pd.read_csv(csv_source)
category = ""
print(activities.head())
print(activities.iloc[0,0])
print(activities.iloc[0,1])

graph_functions = ""
graph_functions = input("Do you wish to graph your productivity stats? y/n")
if graph_functions == "y":
    g_activities = pd.read_csv(csv_source, parse_dates=True, index_col = 1)
    #print(g_activities.head())
    #activities.set_index('Date', inplace=True) # Date index needed for x axis
    # set up graph, index for x axis, columns for stacked categories,values as y axis
    pivot_activities = activities.pivot(index='Date', columns='Category', values='Time')
    pivot_activities.plot.bar(stacked=True)
    plt.xticks(rotation=45)
    plt.show()
category = input("Enter the activity you're working on.")

elapsed_minutes = 0
stop = False
while not stop:
    notification.notify(
        title='Study Time',
        message='Ten minutes focused work.',
        app_name='Work Flow',

    )

    time.sleep(6)
    elapsed_minutes += 10
    #if the last entry does not have the current date, or the current category, create new row
    if activities.empty:
        activities.loc[0] = [category, currentdate, elapsed_minutes]
        activities.to_csv('productivity.csv', index=False)

    for index, row in activities.iterrows():
        if (row["Date"] == currentdate) and row["Category"] == category:
            activities.loc[index, "Time"] += 10
            activities.to_csv('productivity.csv', index=False)
            print('Same date and activity found, time added to activity')
            new_focus = False
            break

    if new_focus:
        activities.loc[len(activities)+1] = [category, currentdate, elapsed_minutes]
        print('New entry made')
        activities.to_csv('productivity.csv', index=False)

#category = index 0 and currentdate = index 1






    
    notification.notify(
        title='Break Time',
        message='You completed your sprint',
        app_name='Work Flow',

    )

    print(f'Minutes studied:{elapsed_minutes}')
    time.sleep(3)
