# Header
# Amy He -UIN 726005518 -TCMG-412-500

# Imports
import datetime
import urllib.request
import os

# Main Program


# retrieve log file
if not os.path.isfile('cache.log'):
    url = 'https://s3.amazonaws.com/tcmg476/http_access_log'
    urllib.request.urlretrieve(url, 'cache.log')

# read file
file = open("cache.log", "r")


number_of_requests_total = 0
days = {"Monday": 0, "Tuesday": 0, "Wednesday": 0, "Thursday": 0, "Friday": 0, "Saturday": 0, "Sunday": 0}
weeks = {}

for line in file:

    if "[" in line:
        number_of_requests_total += 1
        
        start = line.find("[") + len("[")
        end = line.find("]")
        substring = line[start:end]

        format_str = '%d/%b/%Y:%H:%M:%S %z'
        datetime_obj = datetime.datetime.strptime(substring, format_str)
        
        weekday_name = datetime_obj.strftime("%A")
        days[weekday_name] += 1
        
        week_year = "week " + str(datetime_obj.isocalendar()[1]) + " of " + str(datetime_obj.year)
        if week_year in weeks:
            weeks[week_year] += 1
        else:
            weeks[week_year] = 1


        


file.close()

# output results
print("requests made in entire log period:", number_of_requests_total, "\n")

for weekday_name in days:
    print(weekday_name, ":", days[weekday_name])
    
print()

for week_year in weeks:
    print(week_year, ":", weeks[week_year])
