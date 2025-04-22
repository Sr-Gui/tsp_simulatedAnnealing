import numpy as np

#TSP

#Teste tsp fake
tsp=np.array([
  [0,1],
  [4,5],
  [8,9],
  [1,0]
])
n=len(tsp)

def dist(a,b):
  return np.sqrt((np.sum((a-b)**2))) #distancia pseudo-euclidiana? ATT

def cost(sol):
  c=0
  for i in range(n-1):
    c+=dist(tsp[sol[i]],tsp[sol[i+1]])
  c+=dist(tsp[sol[-1]],tsp[sol[0]])
  return c

def tweak(s):
  r=s.copy()
  i,j=np.random.choice(n,2)
  r[i],r[j]=r[j],r[i]
  return r

#Parametros
t=1000
min_t=0.001
a=0.9

#sol inicial
S=np.arange(n)
best=S.copy()

while(t>min_t):
  R=tweak(S)
  d=cost(R)-cost(S)
  if (d>0) or (np.random.rand()<np.exp(d/t)):
    S=R
    if d<0:
      best=S
  t*=a #resfriamento/decrease

#teste
  print(best,cost(best),t)
