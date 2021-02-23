from bs4 import BeautifulSoup as bs
string = '<td valign="top"><b><a href="/sites/hist.phtml?station=BWI&amp;network=MD_ASOS&amp;mode=daily&amp;year=2021&amp;month=1&amp;day=01">01</a></b><br/>High: 39<br/>Low: 30<br/>Rain: 1.02<br/>Snow: 0<br/>Snow Depth: 0<br>Avg Wind: NE @ 6.1<br/>Gust:<br/> E @ 33<br/>(10:04 PM)<br>RH% Min/Max: 59-97<br>Feel Min/Max: 27 to 35</br></br></br></td>'

split1 = string.split('<br')
length = len(split1[1:])
print(length)
day = string.find('a')
#day = day.text
print(day)
cell = 1


while cell <= length:
    if 'Gust' in split1[cell]:
        cell+=1
        print(split1[cell])
    else:
        print(split1[cell])

    cell+=1
