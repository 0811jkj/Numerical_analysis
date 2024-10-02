#수치해석 5장 3번
import math
import time
e=0.001

def f(x):
    return math.e**(-10*x*x)

IP=0
IPlist=[]
x_list=[]
x_0=0.0
h=1

while sum(x_list)<2:
    x_1=x_0+h
    x_2=x_0+2*h
    f_0=f(x_0)
    f_1=f(x_1)
    f_2=f(x_2)
    IP_new=(h/3)*(f_0+4*f_1+f_2)
    if abs(IP-IP_new)<0.001: 
        IPlist.append(IP_new)
        IP=IP_new
        x=x_2-x_0
        x_list.append(x)
        x_0=x_2
    else: h=h/2
 


print(sum(IPlist))