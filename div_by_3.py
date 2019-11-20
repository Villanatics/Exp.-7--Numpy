import numpy as np
b=np.arange(1,101).reshape(10,10)
A=b*b
c=b[b%3==0]
print('The 10x10 squares matrix: ', A)
print('The elements that are divisible by 3: ',c)
np.save('div_by_3',A,c)