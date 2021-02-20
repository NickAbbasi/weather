
def getting_list_of_stations():
    import requests
    from bs4 import BeautifulSoup as bs

    url = 'https://mesonet.agron.iastate.edu/sites/networks.php?network=MD_ASOS&format=html'

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

    mainlist =[]
    for r in range(len(rows)+1):
        mainlist.append([])


    x=0
    for r in rows:


        cells = r.findChildren('td')
        y = 0
        #print('*************')

        for c in cells:

            mainlist[x].append(c.text)
            #print(y)
            y+=1

        y = 0

        x+=1



    x = 0
    for stat in mainlist:
        x = 0
        for val in stat:

            x +=1
    mainlist.pop(0)
    mainlist.pop(len(mainlist)-1)
    return(mainlist)

list = getting_list_of_stations()
#print(list[0])









#print(table)
