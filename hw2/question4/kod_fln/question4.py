import numpy as np
import matplotlib.pyplot as plt

x=np.matrix([0.5,1,1.5,2,2.5,3,3.5,4,4.5,5,5.5,6,6.5,7,7.5,8,8.5,9,9.5,10,])
x=np.transpose(x)
y=np.matrix([0.72,1.63,1.88,3.39,4.02,3.89,4.25,3.99,4.68,5.03,5.27,4.82,5.67,5.95,5.72,6.01,5.5,6.41,5.83,6.33])
y=np.transpose(y)


print("x is our input")
print(x)
print("y is our output")
print(y)


"""Here, we built our A matrix for linear function l(x) = a + bx that
was asked us to find in section a) ."""
A_a=np.concatenate((np.power(x,0),np.power(x,1)),axis=1)
print("Here is our matrix A_a:")
print(A_a)
A_a_t=np.transpose(A_a)

"""Here, we solved the linear system: 
(A.transpose * A) * w = A.transpose * y 
I hope you do not expect me to solve this linear system by hand :D"""
w_a=np.linalg.solve(np.dot(A_a_t,A_a) , np.dot(A_a_t,y))
print("Here is our weight for the function l(x) = a = bx, a and b:")
print(w_a)


new_x=np.linspace(0.1,10,100)
nx=np.reshape(new_x,(100,1))
"""A*w is our predictions. We made these to draw our function l(x)."""
predictions_a=np.dot(np.concatenate((np.power(nx,0),np.power(nx,1)),axis=1),w_a)






"""Here is our matrix A_b for function p(x) = e + d*x + c*x^2"""
A_b=np.concatenate((np.power(x,0),np.power(x,1),np.power(x,2)),axis=1)
A_b_t=np.transpose(A_b)
print("Here is our matrix A_b:")
print(A_b)

"""Again, here we are solving for weight w. By the end of this we will get
the coeffections of e, d and c for function p(x)."""
w_b=np.linalg.solve(np.dot(A_b_t,A_b) , np.dot(A_b_t,y))
print("Here is our weights w_b that contains e,d and c for function p(x):")
print(w_b)

"""This part is just for drawing the function p(x)."""
predictions_b=np.dot(np.concatenate((np.power(nx,0),np.power(nx,1),np.power(nx,2)),axis=1),w_b)





"""Here is our matrix A_c for function f(x) = k + mln(x)"""
A_c=np.concatenate((np.power(x,0),np.log(x)),axis=1)
A_c_t=np.transpose(A_c)
print("Here is our matrix A_c:")
print(A_c)


"""We are solving linear system:
(A.transpose * A) * w = A.transpose * y 
to find weights of k and m for the function f(x)."""
w_c=np.linalg.solve(np.dot(A_c_t,A_c) , np.dot(A_c_t,y))
print("Here is our weights w_c, k and m, for function f(x):")
print(w_c)

predictions_c=np.dot(np.concatenate((np.power(nx,0),np.log(nx)),axis=1),w_c)












fig=plt.figure(1)
fig.set_size_inches(18.5, 10.5)
ax = plt.axes()
ax.scatter([x[:,0]], [y[:,0]])
ax.plot(new_x, predictions_a[:,0])
plt.xticks(np.arange(min(new_x), max(new_x)+1, 0.3))
plt.yticks(np.arange(min(new_x), max(new_x)+1, 0.3))
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.axis('tight')
fig.suptitle('l(x) = a + bx', fontsize=16)

fig=plt.figure(2)
fig.set_size_inches(18.5, 10.5)
ax = plt.axes()
ax.scatter([x[:,0]], [y[:,0]])
ax.plot(new_x, predictions_b[:,0])
plt.xticks(np.arange(min(new_x), max(new_x)+1, 0.3))
plt.yticks(np.arange(min(new_x), max(new_x)+1, 0.3))
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.axis('tight')
fig.suptitle('p(x) = cx2 + dx + e', fontsize=16)

fig=plt.figure(3)
fig.set_size_inches(18.5, 10.5)
ax = plt.axes()
ax.scatter([x[:,0]], [y[:,0]])
ax.plot(new_x, predictions_c[:,0])
plt.xticks(np.arange(min(new_x), max(new_x)+1, 0.3))
plt.yticks(np.arange(min(new_x), max(new_x)+1, 0.3))
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.axis('tight')
fig.suptitle('f(x) = k + mln(x)', fontsize=16)

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