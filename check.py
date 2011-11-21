# -*- coding:utf-8 -*-
# parserGames.py

from analysis import sim
from analysis import topMatches
import pickle

def main(name='molly doe'):
    f = open('log', 'r')
    gamers = pickle.load(f)
    print topMatches(gamers, name, n=5, similarity=sim)
    f.close()

if __name__ == '__main__':
    main()
