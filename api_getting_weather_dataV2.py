import requests
from urllib.request import urlopen
import json
import time
import datetime
#import pandas as pd
#import reading_csv_files_into_db as rs
#import sqlalchemy as sa
#import read_dirinto_df as rd
import read_dirinto_mongodb as mo
#import api_getting_stations as gs
import getting_stations as g
from pymongo import MongoClient
from mongoengine import connect ,Document, StringField, DecimalField,DateTimeField


#connect(db ='weather',host =   'localhost',port = 27017)
client = MongoClient('localhost', 27017)
database = client["weather"]
collection = database["raw__data"]



class Raw_Data(Document):
    station = StringField(required=True)
    valid = DateTimeField(required=True)
    lon = StringField(required=False)
    lat = StringField(required=False)
    tmpf = DecimalField(required=False)
    dwpf = DecimalField(required=False)
    relh = DecimalField(required=False)
    drct = DecimalField(required=False)
    sknt  = DecimalField(required=False)
    p01i  = DecimalField(required=False)
    alti  = DecimalField(required=False)
    mslp  = DecimalField(required=False)
    vsby  = DecimalField(required=False)
    gust  = DecimalField(required=False)
    skyc1  = StringField(required=False)
    skyc2 = StringField(required=False)
    skyc3 = StringField(required=False)
    skyc4 = StringField(required=False)
    skyl1  = DecimalField(required=False)
    skyl2  = DecimalField(required=False)
    skyl4  = DecimalField(required=False)
    skyl3  = DecimalField(required=False)
    wxcodes = StringField(required=False)
    ice_accretion_1hr   = StringField(required=False)
    ice_accretion_3hr  = StringField(required=False)
    ice_accretion_6hr   = StringField(required=False)
    peak_wind_gust    = DecimalField(required=False)
    peak_wind_drct   = StringField(required=False)
    peak_wind_time    = StringField(required=False)
    feel     = DecimalField(required=False)
    metar    = StringField(required=False)
    importdate = DateTimeField(required=False)



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




filelist =[]
#this function is just web scrping to to get md stations. will be set up to get entire us in future
list1 = g.getting_list_of_stations() #gs.get_stations_from_networks('y')
list = list1[0:3]
print(list)
for l in list:
    #row_count_q = sa.select([sa.func.count(raw_import_hourly.columns.valid)]).where(raw_import_hourly.columns.station == l[0])
    connect(db ='weather',host =   'localhost',port = 27017)
    x = Raw_Data.objects(station = l[0]).count()


    #getting date readings started for a station
    if x > 1:
        #max_date_q = sa.select([sa.func.max(raw_import_hourly.columns.valid)]).where(raw_import_hourly.columns.station == l[0])
        last_date  = collection.find_one(sort=[("valid", -1)])["valid"]
        last_date += datetime.timedelta(hours=24)
        start_month = int((last_date).month)
        start_year = int((last_date).year)
        start_day = int((last_date).day)
    #getting end date of readings if applicable
        if len(l[6])> 1:
            end_date = datetime.datetime.strptime(str(l[6]),'%Y-%m-%d %H:%M:%S-%f')
            end_month =  int((end_date).month)
            end_year = int((end_date).year)
            end_day = int((end_date).day)
        else:

            end_date = datetime.datetime.today() - datetime.timedelta(hours=24)
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
            mo.read_into_mongodb(data)
            #will use new function here
            #outfn = "..\%s%s.csv" % (l[0],now.strftime("%Y%m%d"),)
            #filelist.append("..\%s%s.csv" % (l[0],now.strftime("%Y%m%d"),))
            #with open(outfn, "w") as fh:
            #            fh.write(data)
            print(now)
            now += interval

    else:

        start_date = datetime.datetime.strptime(str(l[5]),'%Y-%m-%d %H:%M:%S-%f')
        start_month = int(start_date.month)
        start_year = int(start_date.year)
        start_day = int(start_date.day)

        if len(l[6])> 1:
            end_date = datetime.datetime.strptime(str(l[6]),'%Y-%m-%d %H:%M:%S-%f') + datetime.timedelta(hours=24)
            end_month =  int((end_date).month)
            end_year = int((end_date).year)
            end_day = int((end_date).day)
        else:

            end_date = datetime.datetime.today() -datetime.timedelta(hours=24)
            end_month = int((end_date).month)
            end_year = int((end_date).year)
            end_day = int((end_date).day)


        SERVICE = "http://mesonet.agron.iastate.edu/cgi-bin/request/asos.py?"
        startts = datetime.datetime(start_year, start_month, start_day)
        endts = datetime.datetime(end_year, end_month, end_day)
        #interval = datetime.timedelta(hours=24)
        year_var = start_year
        while year_var  < end_year:
            service = SERVICE + "station={}&data=all&tz=Etc/UTC&format=onlycomma&latlon=yes&missing=empty&trace=empty&".format(l[0])

            service += ("year1={}&month1={}&day1={}&").format(year_var,1,1)

            service += ("year2={}&month2={}&day2={}&").format(year_var,12,31)
            #uri = "%s&station=%s" % (service, 'AXA')
            uri = service
            data = download_data(uri)
            mo.read_into_mongodb(data)
            #will use new function here
            #outfn = "..\%s%s.csv" % (l[0],now.strftime("%Y%m%d"),)
            #filelist.append("..\%s%s.csv" % (l[0],now.strftime("%Y%m%d"),))
            #with open(outfn, "w") as fh:
            #            fh.write(data)
            #print(now)
            #now += interval
            year_var +=1
            print(year_var)
        SERVICE = "http://mesonet.agron.iastate.edu/cgi-bin/request/asos.py?"
        service = SERVICE + "station={}&data=all&tz=Etc/UTC&format=onlycomma&latlon=yes&missing=empty&trace=empty&".format(l[0])
        service += ("year1={}&month1={}&day1={}&").format(year_var,1,1)

        service += ("year2={}&month2={}&day2={}&").format(end_year,end_month,end_day)
        #uri = "%s&station=%s" % (service, 'AXA')
        uri = service
        data = download_data(uri)
        mo.read_into_mongodb(data)
#print(uri)
#print(filelist)

#this function required the files to be written as csvs and then read back.
#rs.writing_results(filelist)
