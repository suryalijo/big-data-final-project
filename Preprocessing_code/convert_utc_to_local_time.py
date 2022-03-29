import pandas as pd
import datetime

df = pd.read_csv("nto_to_final_no space_body.csv")

#Converting utc to local time.
utc_list = df['created_utc'].to_list()
local_time_year = []
local_time_month = []
local_time_day = []
local_time_hour = []
local_time_minute = []
local_time_seconds = []

for utc in utc_list:
    print(utc)
    lt = datetime.datetime.fromtimestamp(int(utc))
    lt_str = str(lt)    
    time_date_array = lt_str.split(' ', 2)
    date = time_date_array[0]
    time = time_date_array[1]
    date_array = date.split('-', 3)
    time_array = time.split(':', 3)
        
    local_time_year.append(date_array[0])
    local_time_month.append(date_array[1])
    local_time_day.append(date_array[2])

    local_time_hour.append(time_array[0])
    local_time_minute.append(time_array[1])
    local_time_seconds.append(time_array[2])
    

df['local_time_year'] = local_time_year
df['local_time_month'] = local_time_month
df['local_time_day'] = local_time_day
df['local_time_hour'] = local_time_hour
df['local_time_minute'] = local_time_minute
df['local_time_second'] = local_time_seconds

df.to_csv("nto_to_final_local_time.csv")
