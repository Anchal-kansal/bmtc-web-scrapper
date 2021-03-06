from bs4 import BeautifulSoup
import requests
import json
import sqlite3
import time
import os

#database connection
conn = sqlite3.connect("bmtc.db")
c = conn.cursor()   
c.execute('CREATE TABLE IF NOT EXISTS routes(bus_id TEXT , route_id TEXT, timings TEXT, bus_stop TEXT, PRIMARY KEY (bus_id, route_id))'   )

#input valid creds 
bus=input("Please enter a valid bus_id")
route=input("Please enter a valid route_id")

#scraping
url1="https://www.mybmtc.com/route/busstops/"+bus+"/print/"+route
req1=requests.get(url1)
data1 =req1.text
soup=BeautifulSoup(data1,"html.parser")
stop=([i.text for i in soup.find_all('span',{'id':'busstop_name'})])

url2="https://www.mybmtc.com/route/schedule/"+bus
req2=requests.get(url2)
data2 =req2.text
soup=BeautifulSoup(data2,"html.parser")
timing=[litag.text for ultag in soup.find_all('ul', {'class': 'routestime'}) for litag in ultag.find_all('li')] 

#data structure to store data
data={
      "bus_id":bus,
      "route_id":route,
      "timings":timing,
      "bus_stop":stop
}

#compatibile data
timing = ','.join([str(i) for i in timing])
stop = ','.join([str(i) for i in stop]) 

#Insert data
try:
    c.execute("INSERT INTO routes (bus_id, route_id, timings, bus_stop) values (? , ? , ? , ?)",
        (bus, route, timing, stop) 
    )
except sqlite3.Error as e:
    print("Can't insert into database:",e) 

#file naming 
time.ctime()
timestr = time.strftime("%b_%d_%Y")
route="bmtc_route_scrap_"+timestr

with open(route+".json", 'w') as outfile:
    json.dump(data, outfile)
    

conn.commit()

c.close()
conn.close()



