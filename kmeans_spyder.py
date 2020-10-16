# -*- coding: utf-8 -*-
"""
Created on Sat May 30 10:42:28 2020

@author: LeLimier
"""

import numpy as np    # si pas encore fait
from sklearn.utils import shuffle

# génération 100 points 3D suivant loi normale centrée
# chaque groupe est translaté d'un vecteur [3,3,3]
d1 = np.random.randn(100,3) + [3,3,3]
d2 = np.random.randn(100,3) + [-3,-3,-3]
d3 = np.random.randn(100,3) + [-3,3,3]
d4 = np.random.randn(100,3) + [-3,-3,3]
d5 = np.random.randn(100,3) + [3,3,-3]

# génération des étiquettes de chaque groupe
c1 = np.ones(100)
c2 = 2 * np.ones(100)
c3 = 3 * np.ones(100)
c4 = 4 * np.ones(100)
c5 = 5 * np.ones(100)

# concaténation des données dans une matrice
data = np.concatenate((d1,d2,d3,d4,d5))
labels = np.concatenate((c1, c2, c3, c4, c5))
print(data.shape)
# permutation aléatoire des lignes de la matrice data
data, labels = shuffle(data, labels)
"""
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
# La couleur des points dépend de leur étiquette (label)
ax.scatter(data[:,0], data[:,1], data[:,2], c=labels)
plt.show()

from sklearn.cluster import KMeans

kmeans = KMeans(n_clusters=5, n_init=1).fit(data)
clu_cent=kmeans.cluster_centers_

def index_centre (clu_cent,data):
    print("ok")
    indice_centre=[]
    for center in clu_cent:
        for dta in data:
            
            if center==dta:
                indice_centre.append(dta.index)
    return indice_centre           
 
   

"""   
tab1=[5,3,4.2] 
tab2=[5,3,4.5] 
if tab1==tab2:
    print("yes") 
    