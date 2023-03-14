import cv2
import matplotlib.pyplot as plt
import numpy as np

img = cv2.imread ('12141630.jpg',0)
I=img[128]
m=max (I)
O=[(i/m)for i in I]
x=np.linspace(-1,1,len (O))
print(x)

plt.plot(x,O)
plt.show()


