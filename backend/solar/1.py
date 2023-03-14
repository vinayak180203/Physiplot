import cv2
import matplotlib.pyplot as plt
import numpy as np

img = cv2.imread ('C:\Users\Vamsi Krishna\Downloads\solar\ff',0)
s=img.shape[0]
I=img[int(s/2) ]
m=max (I)
O=[(i/m)for i in I]
x=np.linspace(-1,1,len (O))
print(x)

plt.plot(x,O)
plt.show()


