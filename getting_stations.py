import requests
from bs4 import BeautifulSoup as bs

url = 'https://mesonet.agron.iastate.edu/sites/networks.php?network=MD_ASOS&format=html'

#dict = {'ID':[],
#        'Name':[],
#        'lat':[],
#        'log':[],
#        'elev':[],
#        'beg':[],
    #    'end':[],
    #    'net':[]}

#mainlist = []
temp =['ID',
        'Name',
        'lat',
        'log',
        'elev',
        'beg',
        'end',
        'net']


page = requests.get(url)

soup = bs(page.content, 'html.parser')

table = soup.findChildren('table')
rows = table[1].findChildren('tr')

mainlist =[[] for _ in range(len(rows)+1)]
#print (mainlist)
#print(len(rows))

x=0
for r in rows:


    cells = r.findChildren('td')
    y = 0
    #print('*************')

    for c in cells:
        #print(c.text)
        #dict[list[y]].append(c.text)
        mainlist[x][y] = c.text

        #print(y)
        y+=1
    #print(temp)
    #print(temp)
    #mainlist.extend()
    mainlist[x]=(temp)
        #temp[y] = c.text
    y = 0
    #print(list)
    x+=1

    #x+=1

x = 0
for stat in mainlist:
    x = 0
    for val in stat:
        #print(y)
        #if y == 5 or y ==6:
        #print(y, '   ',val)
        x +=1
#list1.pop(0)
print(mainlist)




#print(table)
