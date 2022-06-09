# Global VS Local Variable
x = "tanmay"
y = "Gupta"

def func():
    x = "Error"
    global y,z        # to change global var value inside func
    y = "Error"
    z = "TAN"
func()

# x reamin same becoz local var
# y changes its value
# z declared inside a func is accessible outside becoz global
print(x, y, z)        
