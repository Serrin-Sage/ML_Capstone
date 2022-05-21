# -*- coding: utf-8 -*-
from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd
from sklearn.metrics.pairwise import linear_kernel
import pickle
import json
import requests

oop = pd.read_csv('otra.csv')
tfidf = TfidfVectorizer(stop_words='english')
oop.set_index(pd.Index(range(0,len(oop),1)))

tfidf_matrix = tfidf.fit_transform(oop['Description'])

cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)

indxs = pd.Series(oop.index, index = oop['Name']).drop_duplicates()

def what2read(title,cosine_sim=cosine_sim):
  #title = input("Enter book title")
  indx = indxs[title]
  similarity = []
  for e in cosine_sim[indx]:
    sum = [e]
    similarity.append(sum)
  for d in range(len(similarity)):
    similarity[d].append(d)
  similarity = sorted(similarity, key=lambda x:x[0], reverse=True)
  for f in range(len(similarity)):
    similarity[f].append(oop['Name'].iloc[similarity[f][1]])
    similarity[f].append(oop['Rating'].iloc[similarity[f][1]])
  yurr = otherfun(similarity)
  return(yurr)

def otherfun(books):
  dede = []
  for i in books:
    if (i[0]>0.05 and i[0]<0.9):
      dede.append(i)
  keke = [0, 1, 2]
  otherL = [dede[g] for g in keke]
  pogo = []
  for q in dede:
    if q!=otherL[0] and q!=otherL[1] and q!=otherL[2]:
      pogo.append(q)
  algo = sorted(pogo, key=lambda x:x[3], reverse=True)
  hehe = [0,1]
  jkjk = [algo[f] for f in hehe]
  aye = join2(otherL, jkjk)
  return(aye)

def join2(a, b):
  a.extend(b)
  shure = []
  for j in a:
    shure.append(j[2])
  return(shure)
'''
bookL = open("./TestData.json")
after = json.load(bookL)
mon = after[0]
jol = mon['title']
'''
lgID = requests.get('http://localhost:5000/api/users/loggedin')
sky = [f for f in dir(lgID)]
print(sky)
mede = lgID.json()
print(mede)
#print(mede[0]['_id'])
a = requests.get('http://localhost:5000/api/users/allusers')
#print(a)
sky = [f for f in dir(a)]
#print(sky)
dee = a.json()
print('*************')
#print(dee)
saveN = 0
gills = len(mede)
for fe in range(len(dee)):
  #print(dee[fe]['_id'])
  #print(mede[0]['_id'])
  #print('next')
  if(dee[fe]['_id']==mede[gills-1]['myID']):
    print(dee[fe]['_id'])
    print(mede[gills-1]['myID'])
    saveN = fe
    print('heeere')
print('*************')
diff = dee[saveN]
print(saveN)
fin = diff['likedBooks']
somm = len(fin)
print(fin)
print(fin[somm-1])
book = what2read(fin[somm-1])

sumfile = open("w2r.pkl","wb")
pickle.dump(book,sumfile)
sumfile.close()

sumfile2 = open("w2r.pkl","rb")
MLmodel = pickle.load(sumfile2)
sumfile2.close()
