#수치해석 2장 과제 1번
import math
import time

#Newton's Method
def x_new(a): #x 구하기
  result=a-(0.0001)*(2*math.cos(2*a)+math.sin(2*a))/(((math.e**0.0001)*(2*math.cos(2*(a+0.0001))+math.sin(2*(a+0.0001))))
  -(2*math.cos(2*a)+math.sin(2*a)))
  return result

def error_a(a,b): #근사 상대 백분율 오차
  result=math.fabs((a-b)/a*100)
  return result

n=0
e_a=1
x=1

start=time.time()
while e_a>0.000005: #Scarborough 판정법 허용 오차
  n=n+1
  x_old=x
  x=x_new(x)
  e_a=error_a(x,x_old)
  print("%s : x=%f, error_a=%f"%(n,x,e_a))

print('============================')
t=time.time()-start
print("cpu time: %f"%t)
print('============================')