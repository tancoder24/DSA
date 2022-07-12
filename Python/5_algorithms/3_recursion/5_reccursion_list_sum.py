def list_sum(arr, total=0):

    for a in arr:
        if type(a)  == type([]):
            total += list_sum(a)
        else:
            total += a

    return total

if __name__ == "__main__":
    
    arr = [1, 2, [3,4], [5,6]]
    
    ans = list_sum(arr)

    print(ans)