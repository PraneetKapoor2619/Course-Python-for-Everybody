#test function
def func() :
    print("Sample function!")
    return 0

#main body of the program
print("Now I will try to call a simple function!")
func()
print("See? I can call a function!!\n Now let's see what value it can return.")
rvalue = func()
print("The function returned:", rvalue)