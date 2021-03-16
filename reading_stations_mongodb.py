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

x = Stations.objects(station = 'ADW').count()

print(x)
