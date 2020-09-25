# Header
# Amy He -UIN 726005518 -TCMG-412-500

# Imports
import datetime
import urllib.request
import os
import re
from collections import Counter

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
months = {}
files = {}
number_of_error = 0
number_of_redirect = 0

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
            
        month_year = datetime_obj.strftime("%B") + " " + str(datetime_obj.year)
        if month_year in months:
            months[month_year] += 1
        else:
            months[month_year] = 1
            
        if re.search("\".*\" 4..", line) is not None:
            number_of_error += 1
        
        if re.search("\".*\" 3..", line) is not None:
            number_of_redirect += 1
            
        filename = line.split(" ")[6]
        if filename in files:
            files[filename] += 1
        else:
            files[filename] = 1


        


file.close()

# output results
print("requests made in entire log period:", number_of_requests_total, "\n")

for weekday_name in days:
    print(weekday_name, ":", days[weekday_name])
    
print()

for week_year in weeks:
    print(week_year, ":", weeks[week_year])

print()

for month_year in months:
    print(month_year, ":", months[month_year])
    
print()

print("Percentage of Requests as Errors: ", round((number_of_error * 100) / number_of_requests_total, 2), "%")
print("Percentage of Requests as Redirects: ", round((number_of_redirect * 100) / number_of_requests_total, 2), "%")

print()

most_requested_file = Counter(files).most_common(1)[0][0]
least_requested_file = Counter(files).most_common()[-1][0]
print("Most requested file:", most_requested_file)
print("Least requested file:", least_requested_file)
