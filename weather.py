import requests
from bs4 import BeautifulSoup as bs
import pandas as pd
year ='2021'
month = '1'
url = 'https://mesonet.agron.iastate.edu/sites/hist.phtml?station=BWI&network=MD_ASOS&year=2021&month=1'

page = requests.get(url)
dict = {'day':[],
        'month':[],
        'year':[],
        'High':[],
        'Low':[],
        'Rain':[],
        'Snow':[],
        'Snow Depth':[],
        'Avg Wind':[],
        'Wind Direction':[],
        'Gust':[],
        #'Time':[],
        'RH Min/Max':[],
        'Feel':[]}
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
                dict['day'].append(str(day.text))
                dict['month'].append(str(month))
                dict['year'].append(str(year))
                split1 = str(c).split('<br')
                length = len(split1[1:])
                x = 1
                if 'Gust' not in str(c):
                    dict['Gust'].append('')
                if 'High' not in str(c):
                    dict['High'].append('')
                if 'Low' not in str(c):
                    dict['Low'].append('')
                if 'Rain' not in str(c):
                    dict['Rain'].append('')
                if 'Snow:' not in str(c):
                    dict['Snow'].append('')
                if 'Snow Depth' not in str(c):
                    dict['Snow Depth'].append( '')
                if 'Avg Wind:' not in str(c):
                    dict['Avg Wind'].append('')
                if '@' not in str(c):
                    dict['Wind Direction'].append( '')
                if 'RH' not in str(c):
                    dict['RH Min/Max'].append('')
                if 'Feel' not in str(c):
                    dict['Feel'].append('')

                while x <= length:
                    if 'Gust' in split1[x]:
                        x+=1
                        #print(split1[x])
                        dict['Gust'].append(split1[x])
                    else:
                        if 'High' in split1[x]:
                            dict['High'].append(split1[x])
                        if 'Low' in split1[x]:
                            dict['Low'].append(split1[x])
                        if 'Rain' in split1[x]:
                            dict['Rain'].append(split1[x])
                        if 'Snow:' in split1[x]:
                            dict['Snow'].append(split1[x])
                        if 'Snow Depth' in split1[x]:
                            dict['Snow Depth'].append(split1[x])
                        if 'Avg Wind:' in split1[x]:
                            dict['Avg Wind'].append(split1[x])
                        if '@' in split1[x] and 'Avg Wind:' not in split1[x] :
                            dict['Wind Direction'].append(split1[x])
                        if 'RH' in split1[x]:
                            dict['RH Min/Max'].append(split1[x])
                        if 'Feel' in split1[x]:
                            dict['Feel'].append(split1[x])
                        #print(split1[x])

                    x+=1
                #vals = c.find_all('br')
                #for v in vals:
                #    print(v.text)
                #    print('\n')



                #print('*************')
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
