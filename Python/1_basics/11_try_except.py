# without try block program would stop and give an error
# but for now (x undefined) except code executes
# finally will executes whether there is an error or not
try:
    print(x)
except NameError:
    print( "VAR not defined" )
except:
    print( "An exception occured" )
finally:
    print("The 'try except' is finished")

print()
# else block executes if try executes without any error
# finally will executes whether there is an error or not
try:
    print("Tanmay")
except:
    print("Something went wrong")
else:
    print("ALL OK")
finally:
    print("The 'try except' is finished")

print()
# raise exception on certain condition
a = -1
if a < 0:
    raise Exception("a is below 0") and TypeError("Only + ve integers are allowed")

  
