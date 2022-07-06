##############################################
#Simple script for converting MEraki upstream Firewall rules from a CSV as downloaded from the Site to JSON
#for use in any number of platforms
#Download the upstream firewall rules from dashboard and name the CSV m_firewall rules and run the script, this
#convert the data into a Json record
#
#Usage python(3) convert.py
###############################################

import csv
import json

#name of the files to import and export
csvfile = open('m_firewallrules.csv', 'r')
jsonfile = open('file.json', 'w')

reader = csv.reader( csvfile, delimiter=',')
#create an empty data set
data = []

#comment out ifno header in the CSV
line_count = 0
for row in reader:
    # comment out if no header in the CSV
    if line_count > 0:
        #print(row[0])
        #Modify the below model based on the JSON KEY:value Pairs required
        data.append({
         'SourceIP': row[0],
         'DestinationIP': row[1],
         'FQDN': row[2],
         'Ports': row[3],
         'Protocol': row[4],
         'Direction': row[5]
        })
    # comment out ifno header in the CSV
    line_count += 1
#create the Json file
json.dump(data, jsonfile, indent=4)
jsonfile.write('\n')
