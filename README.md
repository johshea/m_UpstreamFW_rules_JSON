Simple script for converting Me
raki upstream Firewall rules from a CSV as downloaded from the Site to JSON
for use in any number of platforms /n
Download the upstream firewall rules from dashboard and name the CSV m_firewallrules and run the script, this
convert the data into a Json record

Usage python(3) convert.py

To get your Firewall CSV, you simply need to go to your meraki dashboard and select Help->Firewall Info. Once the page loads
select the download button. Once the file is downloaded place it in the same directory as the script and rename it to m_firewallrules.csv, and run the script.

