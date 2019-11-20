import numpy as np
x=np.random.random((5,5))
xmean=np.mean(x)
standarddeviation=np.std(x)
Z=(x-xmean)/standarddeviation
print(Z)
np.save('X_normalized', Z)