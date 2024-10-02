#수치해석 5장 4번
def f(x):
    return 6*(1-x*x*1/64)**0.5

x_0=0

I_list=[]
while x_0<7:
    x_1=x_0+1
    x_2=x_0+2
    f_0=f(x_0)
    f_1=f(x_1)
    f_2=f(x_2)
    I=(f_0+4*f_1+f_2)/3
    I_list.append(I)
    x_0=x_2

print(sum(I_list))
