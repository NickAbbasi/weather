import pandas as pd
from urllib.request import urlopen
from sqlalchemy import create_engine
from datetime import date

file = open('..\pw.txt')
pw = str(file.readline())
file.close()



uri = "http://mesonet.agron.iastate.edu/cgi-bin/request/asos.py?station=ADW&data=all&tz=Etc/UTC&format=onlycomma&latlon=yes&missing=empty&trace=empty&year1=2021&month1=1&day1=1&year2=2021&month2=1&day2=2"
data = urlopen(uri, timeout=300).read().decode("utf-8")




split1 = data.split("\n")
#firstrow = split1[0]

#columns = firstrow.split(",")
#print(len(columns))


d = {'station':  [],
'valid': [],
'lon':   [],
'lat':    [],
'tmpf':    [],
'dwpf':    [],
'relh':    [],
'drct':    [],
'sknt':    [],
'p01i':    [],
'alti':    [],
'mslp':    [],
'vsby':    [],
'gust':    [],
'skyc1':    [],
'skyc2':    [],
'skyc3':    [],
'skyc4':    [],
'skyl1':    [],
'skyl2':    [],
'skyl3':    [],
'skyl4':    [],
'wxcodes':    [],
'ice_accretion_1hr':    [],
'ice_accretion_3hr':    [],
'ice_accretion_6hr':    [],
'peak_wind_gust':    [],
'peak_wind_drct':    [],
'peak_wind_time':    [],
'feel':    [],
'metar':    []       }


#station = []
#valid= []
#lon= []
#lat= []
#tmpf= []
#dwpf= []
#relh= []
#drct= []
#sknt= []
#p01i= []
#alti= []
#mslp= []
#vsby= []
#gust= []
#skyc1= []
#skyc2= []
#skyc3= []
#skyc4= []
#skyl1= []
#skyl2= []
#skyl3= []
#skyl4= []
#wxcodes= []
#ice_accretion_1hr= []
#ice_accretion_3hr= []
#ice_accretion_6hr= []
#peak_wind_gust= []
#peak_wind_drct= []
#peak_wind_time= []
#feel= []
#metar = []
#
for row in split1[1:len(split1)-1]:
    x = 1
    #print('********')
    vals = row.split(',')
    #print('**************')
    for v in vals:
       # print(v)
        if v == '':
            v = None

        if x == 1:
            d['station'].append(v)
        if x == 2:
            d['valid'].append(v)
        if x == 3:
            d['lon'].append(v)
        if x == 4:
            d['lat'].append(v)
        if x == 5:
            d['tmpf'].append(v)
        if x == 6:
            d['dwpf'].append(v)
        if x == 7:
            d['relh'].append((v))
        if x == 8:
           d['drct'].append((v))
        if x == 9:
            d['sknt'].append((v))
        if x == 10:
            d['p01i'].append((v))
        if x == 11:
            d['alti'].append((v))
        if x == 12:
            d['mslp'].append((v))
        if x == 13:
            d['vsby'].append((v))
        if x == 14:
            d['gust'].append((v))
        if x == 15:
            d['skyc1'].append((v))
        if x == 16:
            d['skyc2'].append((v))
        if x == 17:
            d['skyc3'].append((v))
        if x == 18:
            d['skyc4'].append((v))
        if x == 19:
            d['skyl1'].append((v))
        if x == 20:
            d['skyl2'].append((v))
        if x == 21:
            d['skyl3'].append((v))
        if x == 22:
            d['skyl4'].append((v))
        if x == 23:
            d['wxcodes'].append((v))
        if x == 24:
            d['ice_accretion_1hr'].append((v))
        if x == 25:
            d['ice_accretion_3hr'].append((v))
        if x == 26:
            d['ice_accretion_6hr'].append((v))
        if x == 27:
            d['peak_wind_gust'].append((v))
        if x == 28:
            d['peak_wind_drct'].append((v))
        if x == 29:
            d['peak_wind_time'].append((v))
        if x == 30:
            d['feel'].append((v))
        if x == 31:
            d['metar'].append((v))
        x+=1



#print(split1)



#columns = split2[0:29]




#print(len(split))
#print(split[30:57])


#

df = pd.DataFrame.from_dict(d)

df.replace('null',pd.NA)


df['ImportDate'] = date.today()

engine = create_engine("mysql+pymysql://{user}:{pw}@localhost/{db}"
                   .format(user="nick",
                           pw=pw,
                           db="weather_data"))

#print(data)
df.to_sql('raw_import_hourly', con = engine, if_exists = 'append',index = False ,chunksize = 1000)
#df.to_excel('test.xlsx', 'sheet1')
#print(col_names)
#print(df.head())

#df = pd.DataFrame
#for c in columns:
   # df.columns[c]
print(df)
#df.columns[split[0:28]]
#print(d)
