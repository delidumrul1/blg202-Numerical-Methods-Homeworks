import numpy as np
import matplotlib.pyplot as plt

#constroction and evaluation functions are taken from our textbook.
def construction(xs):
    w=np.ones(len(xs))
    for j in range(len(xs)):
        for i in range(len(xs)):
            if(i!=j):
                w[j]*=1/(xs[j]-xs[i])
    return w

def evaluation(x,xs,ys,w):
    sum1=0
    sum2=0
    for k in range(len(xs)):
        if(xs[k]==x):
            return ys[k]
    for i in range(len(xs)):
        sum1+=w[i]*ys[i]/(x-xs[i])
    for j in range(len(xs)):
        sum2+=w[j]/(x-xs[j])
    return sum1/sum2



lst1 = []
lst2 = []
n = int(input("Enter number of elements: "))
print("Enter the x values: ")
for i in range(0, n):
    element = float(input())
    lst1.append(element)
print("\nEnter the y values: ")
for j in range(0, n):
    element = float(input())
    lst2.append(element)

print("Which x shall the polynomial guess? ")
guess=float(input())
x = np.array(lst1)
y = np.array(lst2)




w=construction(x)
print("\nLagrange interpolation polynomial guessed like this: p({})={}\n".format(guess,evaluation(guess,x,y,w)))

#By creating x_sss I get 20 new points to plot.

x_sss = np.linspace(np.min(x),np.max(x),20)
x_sss=np.sort(np.concatenate((x,x_sss)))
prec_y=np.zeros_like(x_sss)
for i in range(len(x_sss)):
    prec_y[i]=evaluation(x_sss[i],x,y,w)


x_dif=(max(x_sss)-min(x_sss))/10
y_dif=(max(prec_y)-min(prec_y))/10

fig=plt.figure(1)
fig.set_size_inches(18.5, 10.5)
ax = plt.axes()
ax.scatter(x, y)
ax.plot(x_sss, prec_y)
plt.xticks(np.arange(min(x_sss), max(x_sss)+1, x_dif))
plt.yticks(np.arange(min(prec_y), max(prec_y)+1, y_dif))
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.axis('tight')
fig.suptitle('Lagrange interpolation polynomial', fontsize=16)
plt.show()




















"""
.: ⡴⠑⡄⠀⠀⠀⠀⠀⠀⠀⣀⣀⣤⣤⣤⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀ 
⠸⡇⠀⠿⡀⠀⠀⠀⣀⡴⢿⣿⣿⣿⣿⣿⣿⣿⣷⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀ 
⠀⠀⠀⠀⠑⢄⣠⠾⠁⣀⣄⡈⠙⣿⣿⣿⣿⣿⣿⣿⣿⣆⠀⠀⠀⠀⠀⠀⠀⠀ 
⠀⠀⠀⠀⢀⡀⠁⠀⠀⠈⠙⠛⠂⠈⣿⣿⣿⣿⣿⠿⡿⢿⣆⠀⠀⠀⠀⠀⠀⠀ 
⠀⠀⠀⢀⡾⣁⣀⠀⠴⠂⠙⣗⡀⠀⢻⣿⣿⠭⢤⣴⣦⣤⣹⠀⠀⠀⢀⢴⣶⣆ 
⠀⠀⢀⣾⣿⣿⣿⣷⣮⣽⣾⣿⣥⣴⣿⣿⡿⢂⠔⢚⡿⢿⣿⣦⣴⣾⠁⠸⣼⡿ 
⠀⢀⡞⠁⠙⠻⠿⠟⠉⠀⠛⢹⣿⣿⣿⣿⣿⣌⢤⣼⣿⣾⣿⡟⠉⠀⠀⠀⠀⠀ 
⠀⣾⣷⣶⠇⠀⠀⣤⣄⣀⡀⠈⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀ 
⠀⠉⠈⠉⠀⠀⢦⡈⢻⣿⣿⣿⣶⣶⣶⣶⣤⣽⡹⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀ 
⠀⠀⠀⠀⠀⠀⠀⠉⠲⣽⡻⢿⣿⣿⣿⣿⣿⣿⣷⣜⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀ 
⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣷⣶⣮⣭⣽⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀ 
⠀⠀⠀⠀⠀⠀⣀⣀⣈⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠇⠀⠀⠀⠀⠀⠀⠀ 
⠀⠀⠀⠀⠀⠀⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀ 
⠀⠀⠀⠀⠀⠀⠀⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀ 
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠛⠻⠿⠿⠿⠿⠛⠉
"""