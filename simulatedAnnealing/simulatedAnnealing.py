import numpy as np
import tsplib95

#TSP
tsp=tsplib95.load('../TSP/att48.tsp')
node=list(tsp.get_nodes())
n=len(node)

dist=np.zeros((n,n),dtype=int)
for i in range(n):
  for j in range(n):
    if i!=j:
      dist[i][j]=tsp.get_weight(i+1,j+1)

def cost(sol):
  c=0
  for i in range(n-1):
    c+=dist[sol[i]][sol[(i+1)]]
  return c

#2-opt
def tweak1(sol):
  i,j=sorted(np.random.choice(n,2,replace=False))
  R=sol.copy()
  R[i:j+1]=sol[i:j+1][::-1]
  return R

""" #Teste tsp fake
tsp=np.array([
  [0,1],
  [4,5],
  [8,9],
  [1,0]
])
n=len(tsp)

def dist(a,b):
  return np.sqrt((np.sum((a-b)**2)))

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
  return r """

#Parametros
t=1000
min_t=0.001
a=0.9

#sol inicial
S=np.arange(n)
best=S.copy()

while(t>min_t):
  R=tweak1(S)
  d=cost(R)-cost(S)
  if (d>0) or (np.random.rand()<np.exp(d/t)):
    S=R
    if d<0:
      best=S
  t*=a #resfriamento/decrease

#teste
  print(best,cost(best),t)
