import requests
from urllib.request import urlopen
import json
import time
import datetime
import pandas as pd
#import reading_csv_files_into_db as rs
import sqlalchemy as sa
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
engine = sa.create_engine("mysql+pymysql://{user}:{pw}@localhost/{db}"
                   .format(user="nick",
                           pw=pw,
                           db="weather_data"))

connection = engine.connect()
metadata = sa.MetaData()
raw_import_hourly = sa.Table('raw_import_hourly', metadata, autoload=True, autoload_with=engine)


#can only return 1 day at a time, so need to loop through

filelist =[]
#this function is just web scrping to to get md stations. will be set up to get entire us in future
list1 = g.getting_list_of_stations() #gs.get_stations_from_networks('y')
list = list1[0:3]
print(list)
for l in list:
    row_count_q = sa.select([sa.func.count(raw_import_hourly.columns.valid)]).where(raw_import_hourly.columns.station == l[0])

    x = connection.execute(row_count_q).scalar()


    #getting date readings started for a station
    if x > 1:
        max_date_q = sa.select([sa.func.max(raw_import_hourly.columns.valid)]).where(raw_import_hourly.columns.station == l[0])
        last_date = connection.execute(max_date_q).scalar()
        last_date += datetime.timedelta(hours=24)
        start_month = int((last_date).month)
        start_year = int((last_date).year)
        start_day = int((last_date).day)

    else:

        start_date = datetime.datetime.strptime(str(l[5]),'%Y-%m-%d %H:%M:%S-%f')
        start_month = int(start_date.month)
        start_year = int(start_date.year)
        start_day = int(start_date.day)
    #getting end date of readings if applicable
    if len(l[6])> 1:
        end_date = datetime.datetime.strptime(str(l[6]),'%Y-%m-%d %H:%M:%S-%f') + datetime.timedelta(hours=24)
        end_month =  int((end_date).month)
        end_year = int((end_date).year)
        end_day = int((end_date).day)
    else:

        end_date = datetime.datetime.today()
        end_month = int((end_date).month)
        end_year = int((end_date).year)
        end_day = int((end_date).day)
    SERVICE = "http://mesonet.agron.iastate.edu/cgi-bin/request/asos.py?"
    startts = datetime.datetime(start_year, start_month, start_day)
    endts = datetime.datetime(end_year, end_month, end_day)
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
        print(now)
        now += interval


#print(uri)
#print(filelist)

#this function required the files to be written as csvs and then read back.
#rs.writing_results(filelist)
