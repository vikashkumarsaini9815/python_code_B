def disp (st):
    def show ():
        return"show function"
    result= show() + st + " disp function"
    return result

print(disp("vicky"))    
