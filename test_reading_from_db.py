#def getting_last_date(station)

import sqlalchemy as sa
import time
import datetime


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

row_count_q = sa.select([sa.func.count(raw_import_hourly.columns.valid)]).where(raw_import_hourly.columns.station == 'ADW')

x = connection.execute(row_count_q).scalar()

if x > 1:
    max_date_q = sa.select([sa.func.max(raw_import_hourly.columns.valid)]).where(raw_import_hourly.columns.station == 'ADW')
    last_date = connection.execute(max_date_q).scalar()
    month = int((last_date).month)
    year = int((last_date).year)
    day = int((last_date).day)
    start = datetime.datetime(year, month, day)
    interval = datetime.timedelta(hours=24)
    next = start + interval
import getting_stations as g

list1 = g.getting_list_of_stations()
print(list1)
