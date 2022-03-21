# anonymous function or lambda function
def show (x):
    print(x)

show(5)

show = lambda x,y=3:(x+y)
print(show(5))
