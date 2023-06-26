import numpy as np
import matplotlib.pyplot as plt

#All the code here are taken from our textbook. The code in the
#textbook was in MATLAB, main differences was with the array indices
#but I managed to tailored it for numpy arrays.
def evalnewt(x, xi, coef):
    np1=len(xi);
    p=coef[np1-1]
    for i in range(np1-2,-1,-1):
        p = p*(x - xi[i]) + coef[i];


    return p


def divdif(xi, yi):
    np1 = len(xi)
    n = np1 - 1
    table = np.zeros((np1, np1))
    table[:, 0] = yi
    
    for k in range(1, np1):
        table[k:, k]=(table[k:,k-1] - table[k-1:n,k-1]) / (xi[k:] - xi[:np1-k])
    
    coef = np.diag(table)
    
    return coef, table






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


x = np.array(lst1)
y = np.array(lst2)







coff,tabb=divdif(x,y)
prec=evalnewt(4.2, x, coff)
print("Divided difference table : \n{}".format(tabb))
print("Our polynomial's coefficients : \n{}".format(coff))
print("Our polynomial's predicted value at x=4.2 : {}".format(prec))

#By creating x_sss I get 20 new points to plot.

x_sss = np.linspace(np.min(x),np.max(x),20)
x_sss=np.sort(np.concatenate((x,x_sss)))
prec_y=np.zeros_like(x_sss)
for i in range(len(x_sss)):
    prec_y[i]=evalnewt(x_sss[i],x,coff)


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
fig.suptitle('Newton’s interpolation polynomial', fontsize=16)
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