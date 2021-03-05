def read_into_mongodb(data):

    import pandas as pd
    from datetime import date
    from mongoengine import connect,Document, StringField, DecimalField,DateTimeField
    connect(db ='weather',host =   'localhost',port = 27017)

    #storing pw outside of directory
    #file = open('..\pw.txt')
    #pw = str(file.readline())
    #file.close()


    #here for testing purposes
    #uri = "http://mesonet.agron.iastate.edu/cgi-bin/request/asos.py?station=ADW&data=all&tz=Etc/UTC&format=onlycomma&latlon=yes&missing=empty&trace=empty&year1=2021&month1=1&day1=1&year2=2021&month2=1&day2=2"
    #data = urlopen(uri, timeout=300).read().decode("utf-8")

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

    split1 = data.split("\n")


    for row in split1[1:len(split1)-1]:
        x = 1
        #print('********')
        vals = row.split(',')
        #print(len(vals))
        for v in vals:
            #print(v)
            if v == '':
                v = None
            if x == 1:
                station1 = v
            if x == 2:
                 valid1 =(v)
            if x == 3:
                 lon1 =(v)
            if x == 4:
                 lat1 =(v)
            if x == 5:
                 tmpf1 =(v)
            if x == 6:
                 dwpf1 =(v)
            if x == 7:
                 relh1 =((v))
            if x == 8:
                drct1 =((v))
            if x == 9:
                 sknt1 =((v))
            if x == 10:
                 p01i1 =((v))
            if x == 11:
                 alti1 =((v))
            if x == 12:
                 mslp1 =((v))
            if x == 13:
                 vsby1 =((v))
            if x == 14:
                 gust1 =((v))
            if x == 15:
                 skyc11 =((v))
            if x == 16:
                 skyc21 =((v))
            if x == 17:
                 skyc31 =((v))
            if x == 18:
                 skyc41 =((v))
            if x == 19:
                 skyl11 =((v))
            if x == 20:
                 skyl21 =((v))
            if x == 21:
                 skyl31 =((v))
            if x == 22:
                 skyl41 =((v))
            if x == 23:
                 wxcodes1 =((v))
            if x == 24:
                 ice_accretion_1hr1 =((v))
            if x == 25:
                 ice_accretion_3hr1 =((v))
            if x == 26:
                 ice_accretion_6hr1 =((v))
            if x == 27:
                 peak_wind_gust1 =((v))
            if x == 28:
                 peak_wind_drct1 =((v))
            if x == 29:
                 peak_wind_time1 =((v))
            if x == 30:
                 feel1 =((v))

            if x == 31:
                 metar1 =((v))
            x+=1

    #    d['importdate'].append(date.today())
        #print(feel1)
        row = Raw_Data(
        station = station1,
        valid =  valid1,
        lon  =lon1,
        lat  = lat1  ,
        tmpf   =  tmpf1  ,
        dwpf =   dwpf1   ,
        relh    =   relh1,
        drct   =    drct1,
        sknt =  sknt1    ,
        p01i  =   p01i1  ,
        alti   =  alti1   ,
        mslp    =  mslp1   ,
        vsby     =  vsby1  ,
        gust      =  gust1,
        skyc1   = skyc11   ,
        skyc2 = skyc21     ,
        skyc3  =  skyc31    ,
        skyc4   =skyc41    ,
        skyl1    =  skyl11  ,
        skyl2     =skyl21  ,
        skyl3    = skyl31  ,
        skyl4     =    skyl41,
        wxcodes    =wxcodes1  ,
        ice_accretion_1hr  =    ice_accretion_1hr1   ,
        ice_accretion_3hr   =   ice_accretion_3hr1 ,
        ice_accretion_6hr    =  ice_accretion_6hr1 ,
        peak_wind_gust     =  peak_wind_gust1,
        peak_wind_drct    =   peak_wind_drct1,
        peak_wind_time      = peak_wind_time1,
        feel   =    feel1,
        metar= metar1,
        importdate = date.today()
        )
        #print('*****')
        #print(d['station'])
        row.save()

#from urllib.request import urlopen
#import json
#import time
#import datetime

#MAX_ATTEMPTS = 6
#def download_data(uri):
    """Fetch the data from the IEM
    The IEM download service has some protections in place to keep the number
    of inbound requests in check.  This function implements an exponential
    backoff to keep individual downloads from erroring.
    Args:
      uri (string): URL to fetch
    Returns:
      string data
    """
"""    attempt = 0
    while attempt < MAX_ATTEMPTS:
        try:
            data = urlopen(uri, timeout=300).read().decode("utf-8")
            if data is not None and not data.startswith("ERROR"):
                return data
        except Exception as exp:
            print("download_data(%s) failed with %s" % (uri, exp))
            time.sleep(5)
        attempt += 1"""

#    print("Exhausted attempts to download, returning empty data")
#    return ""






#uri = 'https://mesonet.agron.iastate.edu/cgi-bin/request/asos.py?station=MTN&data=all&year1=2000&month1=1&day1=1&year2=2021&month2=3&day2=1&tz=Etc%2FUTC&format=onlycomma&latlon=yes&elev=no&missing=empty&trace=empty&direct=no&report_type=1&report_type=2'

#data = download_data(uri)

#read_into_mongodb(data)


    #df = pd.DataFrame.from_dict(d)

    #df.replace('null',pd.NA)


    #d['ImportDate'] = date.today()

    #engine = create_engine("mysql+pymysql://{user}:{pw}@localhost/{db}"
    #               .format(user="nick",
    #                       pw=pw,
    #                       db="weather_data"))

    #print(data)
    #df.to_sql('raw_import_hourly', con = engine, if_exists = 'append',index = False ,chunksize = 1000)
