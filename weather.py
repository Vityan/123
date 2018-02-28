<<<<<<< HEAD
import requests, bs4


#p5=b.select('.temperature .p5')
#pogoda3=p5[0].getText()

#p6=b.select('.temperature .p6')
#pogoda4=p6[0].getText()

#print('Утром :' + pogoda1 + ' ' + pogoda2)
#print('Днём :' + pogoda3 + ' ' + pogoda4)


#p=b.select('.rSide .description')
#pogoda=p[0].getText()

#print(pogoda.strip())

def getweather(city):
    s=requests.get('https://sinoptik.com.ru/погода-'+city)

    b=bs4.BeautifulSoup(s.text, "html.parser")

    p3=b.select('.today-time')
    pogoda1=p3[0].getText()
    
    p4=b.select('.today-temp')
    pogoda2=p4[0].getText()
    string_out='Погода в Севастополе на '+pogoda1+ ' - '+pogoda2+' (по данным sinoptik.com.ru)'
    #print(string_out)
    return string_out


=======
import requests, bs4


#p5=b.select('.temperature .p5')
#pogoda3=p5[0].getText()

#p6=b.select('.temperature .p6')
#pogoda4=p6[0].getText()

#print('Утром :' + pogoda1 + ' ' + pogoda2)
#print('Днём :' + pogoda3 + ' ' + pogoda4)


#p=b.select('.rSide .description')
#pogoda=p[0].getText()

#print(pogoda.strip())

def getweather(city):
    s=requests.get('https://sinoptik.com.ru/погода-'+city)

    b=bs4.BeautifulSoup(s.text, "html.parser")

    p3=b.select('.today-time')
    pogoda1=p3[0].getText()
    
    p4=b.select('.today-temp')
    pogoda2=p4[0].getText()
    string_out='Погода в Севастополе на '+pogoda1+ ' - '+pogoda2+' (по данным sinoptik.com.ru)'
    #print(string_out)
    return string_out


>>>>>>> 9c412eec9acc7a719ac3da271090d46536d9d241
