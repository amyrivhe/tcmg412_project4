# Header
# Amy He -UIN 726005518 -TCMG-412-500

# Imports
import requests
import datetime

# Main Program


# download log file
log_file_full_path = "/home/usr/tcmglogfile.txt"
url = 'https://s3.amazonaws.com/tcmg476/http_access_log'
myfile = requests.get(url)
open(log_file_full_path, 'wb').write(myfile.content)

# read and parse file
file = open(log_file_full_path, "r")

number_of_requests_last_year = 0
number_of_requests_total = 0

for line in file:

    if "[" in line:
        start = line.find("[") + len("[")
        end = line.find("]")
        substring = line[start:end]

        format_str = '%d/%b/%Y:%H:%M:%S %z'
        datetime_obj = datetime.datetime.strptime(substring, format_str)

        if datetime_obj.year == 1995:
            number_of_requests_last_year += 1

        number_of_requests_total += 1


file.close()

# output results
print("requests made in last year:", number_of_requests_last_year, ",",
      "requests made in entire log period:", number_of_requests_total)
