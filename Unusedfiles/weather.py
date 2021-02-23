import requests
from bs4 import BeautifulSoup as bs
import datetime
import pandas as pd








dict = {'day':[],
        'month':[],
        'year':[],
        'High':[],
        'Low':[],
        'Rain':[],
        'Snow':[],
        'Snow Depth':[],
        'Avg Wind':[],
        #'Wind Direction':[],
        #'Gust':[],
        #'Time':[],
        #'RH Min/Max':[],
        'Feel':[]
        #,
       #'Network':[],
       #'Name':[]
        }

import datetime
import getting_stations as gs

#list = gs.getting_list_of_stations()
list = [['GAI', 'Gaithersburg', '39.16833', '-77.166', '164.3', '2007-10-31 23:15:00-05', '', 'MD_ASOS']]
#print(list)
#x = 0

#print (list)

for vals in list:
    #print(vals)
    name = (vals[0]).strip()
    network = (vals[7]).strip()
    #getting date readings statred
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


    year = beg_year
    date= datetime.datetime.strptime(str(beg_year)+'-'+str(beg_month)+'-01','%Y-%m-%d')
    end_date= datetime.datetime.strptime(str(end_year)+'-'+str(end_month)+'-01','%Y-%m-%d')
    getbeg = 0
    #year = 2007
    #beg_month = 1
    while int(year) <= end_year and date <= end_date:

    #try:
        print(year)
        if getbeg == 0:
            month = beg_month
            getbeg+=1
        else:
            month = 1
        while int(month)<=12 and date <= end_date:
            print(month)
            url = 'https://mesonet.agron.iastate.edu/sites/hist.phtml?station={}&network={}&year={}&month={}'.format((str(name)),(str(network)),str(year),str(month))
            print(url)
            page = requests.get(url)

            soup = bs(page.content, 'html.parser')
            #print(soup.text)
            table = soup.findChildren('table')
            for t in table:
                rows = t.findChildren('tr')
                for r in rows[2:]:
                    cells = r.findChildren('td')

                    for c in cells:
                        #fin = c.find_all("bgcolor" != '#EEEEEE')
                        if 'href' in str(c):
                            #print(c)

                            day = c.find('a')
                            split1 = str(c).split('<br')
                            length = len(split1[1:])
                            if 'High:' in str(split1[1:]) or 'Low:' in str(split1[1:])or 'Rain:' in str(split1[1:])or 'Snow:' in str(split1[1:]) or 'Snow Depth'  in str(split1[1:]) or'Avg Wind:' in str(split1[1:]):

                                dict['day'].append(str(day.text))
                                dict['month'].append(str(month))
                                dict['year'].append(str(year))
                                #dict['Name'].append(name)
                            #    dict['Network'].append(network)
                                #split1 = str(c).split('<br')
                                #length = len(split1[1:])
                                x = 1
                            #    if 'Gust' not in str(c):
                                #    dict['Gust'].append('')
                                if 'High:' not in str(split1[1:]):
                                    dict['High'].append('na')
                                if 'Low:' not in str(split1[1:]):
                                    dict['Low'].append('na')
                                if 'Rain:' not in str(split1[1:]):
                                    dict['Rain'].append('na')
                                if 'Snow:' not in str(split1[1:]):
                                    dict['Snow'].append('na')
                                if 'Snow Depth' not in str(split1[1:]):
                                    dict['Snow Depth'].append( 'na')
                                if 'Avg Wind:' not in str(split1[1:]):
                                    dict['Avg Wind'].append('na')
                                #if '@' not in str(c):
                                #    dict['Wind Direction'].append( '')
                                #if 'RH' not in str(split1[1:]):
                                #    dict['RH Min/Max'].append('')
                                if 'Feel' not in str(split1[1:]):
                                    dict['Feel'].append('na')

                                while x <= length:
                                    #if 'Gust' in split1[x]:
                                    #    x+=1
                                        #print(split1[x])
                                    #    dict['Gust'].append(split1[x].replace('/>',''))
                                    #else:
                                    #dict['Gust'].append('')
                                    if 'High:' in split1[x]:
                                        dict['High'].append((split1[x]))#.split(':'))[1].replace("'",''))
                                    if 'Low:' in split1[x]:
                                        dict['Low'].append((split1[x]))#.split(':'))[1].replace("'",''))
                                    if 'Rain:' in split1[x]:
                                        dict['Rain'].append((split1[x]))#.split(':'))[1].replace("'",''))
                                    if 'Snow:' in split1[x]:
                                        dict['Snow'].append((split1[x]))#.split(':'))[1].replace("'",''))
                                    if 'Snow Depth' in split1[x]:
                                        dict['Snow Depth'].append((split1[x]))#.split(':'))[1].replace("'",''))
                                    if 'Avg Wind:' in split1[x]:
                                        dict['Avg Wind'].append((split1[x]))#.split(':'))[1].replace("'",'').replace('/>',''))
                                    #if '@' in split1[x] and 'Avg Wind:' not in split1[x] :
                                    #    dict['Wind Direction'].append(split1[x])
                                    #if 'RH' in split1[x]:
                                    #    dict['RH Min/Max'].append((split1[x].split(':'))[1].replace("'",'').replace('</br>','').replace('</td',''))
                                    if 'Feel' in split1[x]:
                                        dict['Feel'].append((split1[x].split(':'))[1].replace("'",'').split('<')[0].replace('</br>','').replace('</td',''))
                                        #print(split1[x])

                                    x+=1
                            #vals = c.find_all('br')
                            #for v in vals:
                            #    print(v.text)
                            #    print('\n')

            date= datetime.datetime.strptime(str(year)+'-'+str(month)+'-01','%Y-%m-%d')
            month+=1
        year+=1
        #except:
        #    month+=1
        #    year+=1
        #    print('hi')
        #    continue


                #print('*************')
print(dict)
df = pd.DataFrame.from_dict(dict)
df.to_excel('..\weather.xlsx')
print(df)


                #print(string.text)



            #print(len(c))
                #print('**********')
#print(len(cells))

        #    fin = c.findChildren('br')
            #for f in fin:
                #print(f)
            #print(c)

    #print(rows[3:])
    #for r in rows:


    #    print(r.text)
