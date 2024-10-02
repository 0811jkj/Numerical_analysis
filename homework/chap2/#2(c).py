#수치해석 2장 과제 2번 (c)
import math
import time

#Muller's Method

#three initial values
x0=0.45
x1=0.4
x2=0.5

#given function
def f(x):
  result=(10*math.e**(-1*x))*math.sin(2*math.pi*x)-2
  return result

def h1(x0,x1): #h_1
  result=x0-x1
  return result

def h2(x2,x0): #h_1
  result=x2-x0
  return result

def r(h1,h2): #γ
  result=h2/h1
  return result

def a(r,h1,f0,f1,f2): #a
  result=(r*f1-f0*(1+r)+f2)/(r*(h1**2)*(1+r))
  return result

def b(a,h1,f0,f1): #b
  result=(a*(h1**2)+f0-f1)/h1
  return result

def x3(x0,a,b,c): #x_3
  if b>=0:
    result=x0-(2*c)/(b+(b**2-4*a*c)**0.5)
  else:
    result=x0-(2*c)/(b-(b**2-4*a*c)**0.5)
  return result

def error_a(a,b): #근사 상대 백분율 오차
  result=math.fabs((a-b)/a*100)
  return result

e_a=1
n=0
start=time.time()
while e_a>0.0005:  #Scarborough 판정법 허용 오차
  n=n+1
  x0_old=x0
  f0=f(x0)
  f1=f(x1)
  f2=f(x2)
  h_1=h1(x0,x1)
  h_2=h2(x2,x0)
  r_=r(h_1,h_2)
  a_=a(r_,h_1,f0,f1,f2)
  b_=b(a_,h_1,f0,f1)
  c=f0
  x_3=x3(x0,a_,b_,c)
  f3=f(x_3)
  e_a=error_a(x_3,x0)
  print("%s: x0=%f(f(x0)=%f), x1=%f(f(x1)=%f), x2=%f,(f(x2)=%f), x3=%f(f(x3)=%f), e_a=%f"%(n,x0,f0,x1,f1,x2,f2,x_3,f3,e_a))
  if x_3>x0:
    x0=x_3
    x1=x0_old
    x2=x2
  else:
    x0=x_3
    x1=x1
    x2=x0_old

print('============================')
t=time.time()-start
print("cpu time: %f"%t)
print('============================')