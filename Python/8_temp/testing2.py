no_of_forces = input()

initial_force, initial_direction = input().split()

initial_force = int(initial_force)

forces =  list(map(int, input().split()))

for i in forces:
    if initial_force > 0:
        initial_force -= i
        if initial_force == 0:
            print("Possible", end="")
            break
    elif initial_force < 0:
        initial_force += i
        if initial_force == 0:
            print("Possible", end="")
            break
else:
    print("Not Possible", end="")
    