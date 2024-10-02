#수치해석 2장 과제 4번
import math
import time

#Secant's Method
#initial values
x_1=1.4
x_2=1.5

def f(x): #given function
  result=30976-9800*(x**2)*(3-x)
  return result

def x3(x_1,x_2,f_1,f_2): 
  result=x_2-f_2*(x_2-x_1)/(f_2-f_1)
  return result

def error_a(a,b): #근사 상대 백분율 오차
  result=math.fabs((a-b)/a*100)
  return result

e_a=1
n=0
x_3=0
start=time.time()
while e_a>0.000005: #Scarborough 판정법 허용 오차
  n=n+1
  f_1=f(x_1)
  f_2=f(x_2)
  x_3_old=x_3
  x_3=x3(x_1,x_2,f_1,f_2)
  f_3=f(x_3)
  e_a=error_a(x_3,x_3_old)
  print("%s: x_1=%f(f(x_1)=%f), x_2=%f(f(x_2)=%f, x_3=%f(f(x_3)=%f, e_a=%f"%(n,x_1,f_1,x_2,f_2,x_3,f_3,e_a))
  x_1=x_2
  x_2=x_3

print('============================')
t=time.time()-start
print("cpu time: %f"%t)
print('============================')