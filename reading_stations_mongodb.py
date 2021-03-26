def getting_stations_from_db():
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

    x = Stations.objects().count()
    mainlist = []
    z = 0
    while z < x:
        mainlist.append([])
        z+=1

    x = 0
    for s in Stations.objects:
        mainlist[x].append(s.station)
        mainlist[x].append(s.station_name)
        mainlist[x].append(s.lat)
        mainlist[x].append(s.lon)
        mainlist[x].append(s.beg)
        if s.end is None:
            mainlist[x].append('')
        else:
            mainlist[x].append(s.end)
        mainlist[x].append(s.IEM)
        x+=1
    return mainlist
x = getting_stations_from_db()
print(x[0])
