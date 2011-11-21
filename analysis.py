# -*- coding:utf-8 -*-
# parserGames.py
"""Методы для анализа соц. данных Канобу

sim: Выясняет, на сколько близки два человека
в своих предпочтениях
"""

def sim(prefs, person1, person2):
    """Выясняет, на сколько близки два человека
в своих предпочтениях.

    Args: 
        prefs: Список людей и их предпочтений.
        person1, person2: Два человека из списка.

    Returns:
        Количество схожих предпочтений.
    """
    # Получить список предметов, оценненых обоим
    si={}
    for item in prefs[person1]:
        if item in prefs[person2]:
            si[item] = 1
    
    return len(si)

def topMatches(prefs,person,n=5,similarity=sim):
    """Возвращает список наилучших соответствий 
    для человека из словаря prefs.
    и функция подобия - необязательные параметры.

    Args: 
        prefs: Список людей и их предпочтений.
        person: Человек, для которого составляем
            список ему подобных.
        n: Количество результатов в списке.
        similarity: Функция подобия.

    Returns:
        Возвращает список наилучших соответствий 
    для человека из словаря prefs.
    """
    scores=[(similarity(prefs,person,other),other) for other in prefs if other!=person]
        
    # Отсортировать список по убыванию оценок
    scores.sort()
    scores.reverse()
    return scores[0:n]

    
    
