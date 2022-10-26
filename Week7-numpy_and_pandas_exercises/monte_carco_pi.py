#%%
import numpy as np
import matplotlib.pyplot as plt
# %%
# want points (x, y)  where x in[-1, +1]
#and y in [-1, +1]

import random
x=random.uniform(-1, 1)
y=random.uniform(-1, 1)

print(x)
print(y)
# %%
#Want to know radius of a line from the 
#origin (0,0) to the point(x, y)
xs=x**2
ys=y**2
r=np.sqrt(xs + ys)
print(x, y, r)

def random_point_and_radius():
    x=np.random.uniform(-1, 1)
    y=np.random.uniform(-1, 1)
    xs=x**2
    ys=y**2
    r=np.sqrt(xs+ys)
    return x, y, r
    
# %%
all_x=[]
all_y=[]
all_r=[]

times_run=1000

for i in range(times_run):
   x,y,r=random_point_and_radius()
   all_x.append(x)
   all_y.append(y)
   all_r.append(r)
   # %%
   all_x=np.array(all_x)
   all_y=np,array(all_y)
   all_r=np.array(all_r)
