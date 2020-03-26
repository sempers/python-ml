import os
import re
import numpy as np
import scipy.spatial as spa

f = open('sentences.txt', 'r')
lines = [l.lower() for l in f.readlines()]
tokens = set()
tokenized_lines = [list(filter(lambda x: len(x)>0, re.split('[^a-z]',l))) for l in lines]
token_set = set()
for tl in tokenized_lines:
    for t in tl:
        token_set.add(t)
m = []
for tl in tokenized_lines:
    ml = [(1 if t in tl else 0) for t in list(token_set)]
    m.append(ml)
#npm = np.array(m)
#print(npm.shape)
cosine_distances = [(i, spa.distance.cosine(m[0], m[i])) for i in range(0,len(m))]
cosine_distances.sort(key=lambda x: x[1])
print(cosine_distances)


