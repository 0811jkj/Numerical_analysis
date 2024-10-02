#수치해석 과제 4장 1번(c)
#Lagrange 3차 보간 다항식
import math
import time

#variables
x_0=0
x_1=0.2
x_2=0.8
x_3=1.0
f_0=0
f_1=0.1996
f_2=0.7721
f_3=0.9461

x=0.7 #independent variable
p_3_x=(((x-x_1)*(x-x_2)*(x-x_3)*f_0)/((x_0-x_1)*(x_0-x_2)*(x_0-x_3))+((x-x_0)*(x-x_2)*(x-x_3)*f_1)/((x_1-x_0)*(x_1-x_2)*(x_1-x_3))+
     ((x-x_0)*(x-x_1)*(x-x_3)*f_2)/((x_2-x_0)*(x_2-x_1)*(x_2-x_3))+((x-x_0)*(x-x_1)*(x-x_2)*f_3)/((x_3-x_0)*(x_3-x_1)*(x_3-x_2)))
print(p_3_x)
x3=(f_0/((x_0-x_1)*(x_0-x_2)*(x_0-x_3))+f_1/((x_1-x_0)*(x_1-x_2)*(x_1-x_3))+
    f_2/((x_2-x_0)*(x_2-x_1)*(x_2-x_3))+f_3/((x_3-x_0)*(x_3-x_1)*(x_3-x_2)))
x2=(-1*(x_1+x_2+x_3)*f_0/((x_0-x_1)*(x_0-x_2)*(x_0-x_3))+(-1)*(x_0+x_2+x_3)*f_1/((x_1-x_0)*(x_1-x_2)*(x_1-x_3))+
    (-1)*(x_0+x_1+x_3)*f_2/((x_2-x_0)*(x_2-x_1)*(x_2-x_3))+(-1)*(x_0+x_1+x_2)*f_3/((x_3-x_0)*(x_3-x_1)*(x_3-x_2)))
x1=((x_1*x_2+x_2*x_3+x_1*x_3)*f_0/((x_0-x_1)*(x_0-x_2)*(x_0-x_3))+(x_0*x_2+x_2*x_3+x_0*x_3)*f_1/((x_1-x_0)*(x_1-x_2)*(x_1-x_3))+
    (x_0*x_1+x_1*x_3+x_0*x_3)*f_2/((x_2-x_0)*(x_2-x_1)*(x_2-x_3))+(x_0*x_1+x_1*x_2+x_0*x_2)*f_3/((x_3-x_0)*(x_3-x_1)*(x_3-x_2)))
x0=((x_1*x_2*x_3*(-1))*f_0/((x_0-x_1)*(x_0-x_2)*(x_0-x_3))+(x_0*x_2*x_3*(-1))*f_1/((x_1-x_0)*(x_1-x_2)*(x_1-x_3))+
    (x_0*x_1*x_3*(-1))*f_2/((x_2-x_0)*(x_2-x_1)*(x_2-x_3))+(x_0*x_1*x_2*(-1))*f_3/((x_3-x_0)*(x_3-x_1)*(x_3-x_2)))
print("%f x^3+ %f x^2+ %f x+ %f"%(x3,x2,x1,x0))