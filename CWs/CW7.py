def pos_fun(i, f, st):
    su1 = i + f
    st1 = st.upper()
    return su1, st1


out1, out2 = pos_fun(5, 6.53, "Adil")
print(out1, out2)

out3 = pos_fun(10, 12.5, "Cool")  # Return as tuple
print(out3)

# Keyword argument

out_lst1 = pos_fun(i=10, f=12.53, st="Adil")
print(out_lst1)
out_lst2 = pos_fun(i=10, st="Adil", f=13.56)
print(out_lst2)

out1, out2 = pos_fun(10, f=12.5, st="Adil")
print(out1, out2)
# out1,out2 = pos_fun(i=12,10.5,st = 'Adil') # Does not work
# print(out1,out2)

# Variable Positional


def var_args(*args):
    for var in args:
        print(var, type(var))


var_args("Adil", 1, 5)
var_args(12.5, 5, "Lidar")


def kwvar_args(**kwargs):  # Takes it as dict
    for k, v in kwargs.items():
        print(k, v)


kwvar_args(i=10)
kwvar_args(i=10, j=12.5)
kwvar_args(st1="Adil", i=12, j=34.5)


def pvkv(i, j, *args, k, **kwargs):
    print(i, j)
    for var in args:
        print(var)
    print(k)
    for k, v in kwargs.items():
        print(k, v)


pvkv(10, 52, 5, "Adil", "Mohammed", k=567, l=43, m=56.67)
# Recursive Functions


def PrintNum(N):
    if N > 0:
        print(N)
        PrintNum(N - 1)


def PrintNumOpp(N):
    if N > 0:
        PrintNumOpp(N - 1)
        print(N)


PrintNum(3)
print("PrintOPP")
PrintNumOpp(3)


def avg(a, b):
    return (a + b) / 2


print(avg(2, 4))

dc1 = {"oil": 3, "stud": 2, "abc": 1}
dc2 = sorted(dc1.items(), key=lambda kv1: kv1[1])  # Sort according to values
print(dc2)

# Functions as first class values


def f():
    return 10


def sum1(a, b, f):
    return print("Sum: ", a + b + f())


f1 = sum1  # Takes it as pointer
print(f1)
f1(10, 20, f)
