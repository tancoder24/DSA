def print_sequence(input, output=""):
    # 1. base case and some processing
    if len(input) < 1: 
        print(output)
        return
    
    # 2. recurrsive call
    print_sequence(input[1:], output)
    print_sequence(input[1:], output+input[0])

if __name__ == "__main__":
    
    s = "abc"
    print_sequence(s)