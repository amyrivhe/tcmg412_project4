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

for line in file:

    if "[" in line:
        number_of_requests_total += 1
        
        start = line.find("[") + len("[")
        end = line.find("]")
        substring = line[start:end]

        format_str = '%d/%b/%Y:%H:%M:%S %z'
        datetime_obj = datetime.datetime.strptime(substring, format_str)


        


file.close()

# output results
print("requests made in entire log period:", number_of_requests_total)
