# -*- coding:utf-8 -*-
# parserGames.py

import math
import pickle
from BeautifulSoup import BeautifulSoup
from urllib2 import urlopen, URLError

def parseUsers(address='http://kanobu.ru/accounts/?ord=d&by=rating&page=', begin = 1, end = 3):
    """
        Возвращает список всех пользователей с адресами их страничек
    """
    for i in xrange(begin, end):
        try:            
            doc = BeautifulSoup(urlopen(address + str(i)), fromEncoding="utf-8")
            #находим всех пользователей на заданной странице.
            page = doc.find('ul', attrs = {'class':'min'})                   
            list = []
            for item in page.findAll({'li' : True,}):
                path = item.find({'a' : True})["href"]
                name = "%s" % item.find("h5").contents[0]
                list.append([name, path])

            return list              
        except URLError:
            # иногда сразу страница не получается загрузить-попытаться снова
            i -= 1             
   
def parseGameByUser(address):
    """
        Возвращает словарь всех игр для пользователя
    """
    # Создаем полный путь до игр пользователя
    path = "http://kanobu.ru" + address     
     
    # Производим первоначальный анализ пользователя
    doc = BeautifulSoup(urlopen(path), fromEncoding="utf-8")
        
    # Находим количесвто игр у пользователя           
    tag = doc.findAll('a', {'href': address + 'favgames/'})            
    countOfGames = tag[1].string[7:]

    print "Обнаруженно %d игр." % int(countOfGames)

    if int(countOfGames) > 100: print "Геймер детектед!"
 
    # Находим кол-во страниц для парсинг с играми        
    countOfPages = int(countOfGames)/30.0

    countOfPages = math.ceil(countOfPages)        
    
    print "Обнаруженно %s страниц с играми." % int(countOfPages)

    path = path + "favgames/?page="
    # Создаем словарь с играми пользотеля
    games = []
    for i in xrange(1, int(countOfPages)+1):
        doc = BeautifulSoup(urlopen(path + str(i)), fromEncoding="utf-8")
        pages = doc.findAll('ul', {'class': 'tiny'})            
        for page in pages:
            for item in page.findAll("h5"):
                print item.string
                games.append(item.string)
           
    return games

def parseAllUsersGame(listUsers):
    """
        По списку пользователей составляет общий словарь с их играми
    """
    gamers = {}
    for userInfo in listUsers[:8]:
        print " "            
        print "***"
        print " "
        print userInfo[0]
        print " "
        gamers[userInfo[0]] = parseGameByUser(userInfo[1])

    return gamers

if __name__ == '__main__':
    f = open('log', 'w')  
    list = parseUsers()  
    pickle.dump(parseAllUsersGame(list), f) 
    f.close()
