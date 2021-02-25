import requests
from urllib.request import urlopen
import json
import time
import datetime
import pandas as pd
import reading_csv_files_into_db as rs
from sqlalchemy import create_engine
import read_dirinto_df as rd

#import api_getting_stations as gs
import getting_stations as g
MAX_ATTEMPTS = 6
def download_data(uri):
    """Fetch the data from the IEM
    The IEM download service has some protections in place to keep the number
    of inbound requests in check.  This function implements an exponential
    backoff to keep individual downloads from erroring.
    Args:
      uri (string): URL to fetch
    Returns:
      string data
    """
    attempt = 0
    while attempt < MAX_ATTEMPTS:
        try:
            data = urlopen(uri, timeout=300).read().decode("utf-8")
            if data is not None and not data.startswith("ERROR"):
                return data
        except Exception as exp:
            print("download_data(%s) failed with %s" % (uri, exp))
            time.sleep(5)
        attempt += 1

    print("Exhausted attempts to download, returning empty data")
    return ""

#creating db engine to pass into read_into_db
file = open('..\pw.txt')
pw = str(file.readline())
file.close()
engine = create_engine("mysql+pymysql://{user}:{pw}@localhost/{db}"
                   .format(user="nick",
                           pw=pw,
                           db="weather_data"))
#can only return 1 day at a time, so need to loop through

filelist =[]
list1 = g.getting_list_of_stations() #gs.get_stations_from_networks('y')
list = list1[0:1]
print(list)
for l in list:
    #getting date readings started for a station
    start_date = datetime.datetime.strptime(str(l[5]),'%Y-%m-%d %H:%M:%S-%f')
    start_month = int(start_date.month)
    start_year = int(start_date.year)
    start_day = int(start_date.day)
    #getting end date of readings if applicable
    if len(l[6])> 1:

        end_month =  int(datetime.datetime.strptime(str(l[5]),'%Y-%m-%d %H:%M:%S-%f').month)
        end_year = int(datetime.datetime.strptime(str(l[5]),'%Y-%m-%d %H:%M:%S-%f').year)
        end_day = int(datetime.datetime.strptime(str(l[5]),'%Y-%m-%d %H:%M:%S-%f').day)
    else:
        end_month = int((datetime.datetime.today()).month)
        end_year = int((datetime.datetime.today()).year)
        end_day = int((datetime.datetime.today()).day)
    SERVICE = "http://mesonet.agron.iastate.edu/cgi-bin/request/asos.py?"
    startts = datetime.datetime(2011, 1, 1)
    endts = datetime.datetime(2011, 6, 30)
    interval = datetime.timedelta(hours=24)
    now = startts
    while now < endts:
        service = SERVICE + "station={}&data=all&tz=Etc/UTC&format=onlycomma&latlon=yes&missing=empty&trace=empty&".format(l[0])

        service += now.strftime("year1=%Y&month1=%m&day1=%d&")

        service += (now + interval).strftime("year2=%Y&month2=%m&day2=%d&")
        #uri = "%s&station=%s" % (service, 'AXA')
        uri = service
        data = download_data(uri)
        rd.read_into_db(data,engine)
        #will use new function here
        #outfn = "..\%s%s.csv" % (l[0],now.strftime("%Y%m%d"),)
        #filelist.append("..\%s%s.csv" % (l[0],now.strftime("%Y%m%d"),))
        #with open(outfn, "w") as fh:
        #            fh.write(data)
        now += interval
        print(now)

#print(uri)
#print(filelist)

#this function required the files to be written as csvs and then read back.
#rs.writing_results(filelist)
