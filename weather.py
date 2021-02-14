import requests
from bs4 import BeautifulSoup as bs

url = 'https://mesonet.agron.iastate.edu/sites/hist.phtml?station=BWI&network=MD_ASOS&year=2021&month=1'

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
                print(day.text)
                vals = c.find_all('br')
                for v in vals:
                    print(v.text)
                    print('\n')



                print('*************')


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
