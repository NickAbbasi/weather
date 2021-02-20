
import datetime
import getting_stations as gs

list = gs.getting_list_of_stations()
#print(list)
#x = 0

for vals in list:
    name = vals[0]
    network = vals[7]
    x = datetime.datetime.strptime(str(vals[5]),'%Y-%m-%d %H:%M:%S-%f')
    if len(vals[6])> 1:

        end_month =  int(datetime.datetime.strptime(str(vals[5]),'%Y-%m-%d %H:%M:%S-%f').month)
        end_year = int(datetime.datetime.strptime(str(vals[5]),'%Y-%m-%d %H:%M:%S-%f').year)
    else:
        end_month = int((datetime.datetime.today()).month)
        end_year = int((datetime.datetime.today()).year)
    beg_year = int(x.year)
    beg_month = int(x.month)

    #print(name,beg_month,beg_year, end_month ,end_year,network)

    date= datetime.datetime.strptime(str(beg_year)+'-'+str(beg_month)+'-01','%Y-%m-%d')
    end_date= datetime.datetime.strptime(str(end_year)+'-'+str(end_month)+'-01','%Y-%m-%d')
    print(date,end_date)
print(list)
