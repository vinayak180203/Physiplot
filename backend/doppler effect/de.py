# inputs
# freequency emitted  (number)
# freequency  observed (list) (40 entries)
# time (list)  ( 40 entries)

# outputs
# velocity vs time ( table  ) and graph 
# freequency observed vs time (graph) table 

#x= freequency input observed

#y= freequency input emitted

#z = velocity 

for i in range (len(x)):
    a=x[i]
    b=((y/a)-1)*y
    z.append(b)

for j in range(0,40):
    print(z[j])
print(z)    

# t = time input 


import matplotlib.pyplot as plt

# x-axis values
y= freequency obvserved 
x= time
# plotting points as a scatter plot
plt.plot(x, y)
plt.scatter(x, y, label= "data points", color= "green", 
            marker= ".", s=30)

# x-axis label
plt.xlabel('time')
# frequency label
plt.ylabel('freequency observed')
# plot title
plt.title('freequency observed  vs time graph')
# showing legend
plt.legend()

# function to show the plot
plt.show()


# x-axis values
y= velocity 
x= time
# plotting points as a scatter plot
plt.plot(x, y)
plt.scatter(x, y, label= "data points", color= "green", 
            marker= ".", s=30)

# x-axis label
plt.xlabel('time')
# frequency label
plt.ylabel('velcoity observed')
# plot title
plt.title('velocity   vs time graph')
# showing legend
plt.legend()

# function to show the plot
plt.show()
