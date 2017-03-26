# -*- coding: utf-8 -*-
"""
Created on Wed Jun 01 10:12:26 2016

@author: Gunnvant
"""
import os
import pandas as pd
from pandas import DataFrame,Series
os.chdir('F:\\Work\\Jigsaw Academy\\Mini Quiz')

f=open('decatthlon.txt','r')
l=[]
for line in f:
    l.append(line)
a=DataFrame(l)

import requests
headers={'User-Agent':'Mozilla/5.0 (X11; U; Linux i686) Gecko/20071127 Firefox/2.0.0.11'}
url='https://www.goodreads.com/author/show/18541?format=xml&key=kTzR1bwhDck5ASWEv0E3jg'
con=requests.get(url,headers=headers)

os.chdir('F:\\Work\\Python\\WNS Python\\Class Excercises')
data=pd.read_csv('MMwoes.csv',skiprows=1,na_values=['NA','',' '])
data.rename(columns={'int_rate':'interest_rate'},inplace=True)