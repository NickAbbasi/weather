import getting_stations as g
from datetime import date
from mongoengine import connect,Document, StringField, DecimalField,DateTimeField


connect(db ='weather',host =   'localhost',port = 27017)
list1 = g.getting_list_of_stations()



class Stations(Document):
    station = StringField(required=True)
    station_name = StringField(required=True)
    lat = StringField(required=False)
    lon = StringField(required=False)
    ele = DecimalField(required=False)
    beg = DateTimeField(required=False)
    end = DateTimeField(required=False)
    IEM = StringField(required=True)




for l in list1:
    x = 0
    for val in l:
        if val == '':
            val = None
        if x== 0:
            station = val
        if x== 1:
            station_name = val
        if x== 2:
            lat = val
        if x== 3:
            lon = val
        if x== 4:
            ele = val
        if x== 5:
            beg = val
        if x== 6:
            end = val
        if x== 7:
            IEM = val
        x +=1

    row = Stations(
        station = station,
        station_name = station_name,
        lat = lon,
        lon = lat,
        ele = ele,
        beg = beg,
        end = end,
        IEM = IEM
    )

    row.save()
