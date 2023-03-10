import cv2
import matplotlib.pyplot as plt
import numpy as np
img = cv2.imread('12141630.jpg',flags = cv2.IMREAD_GRAYSCALE)
print(img.shape)
print(img[128])

a=0
b= max(img[128])
print(b)
l=list(img[128])
for i in l :
    k= min(l)
    if k>=10 :
        a=k
    else:
        l.remove(k)    

print(a,b)        

alpha = a/b 
beta = 1 - (alpha )

img = cv2.imread ('12141630.jpg',0)
I=img[128]
m=max (I)
O=[(i/m)**(0.25) for i in I]
x=np.linspace(-1,1,len (O))
print(x)

q=[(w-alpha/beta) for w in O]
plt.plot(O,q)
plt.show()