from tabnanny import check


def bubble_sort(elements):
    size = len(elements)

    for i in range( size-1 ):
        swapped = False
        for j in range( size - i - 1 ):
            if elements[j] > elements[j+1]:
                elements[j], elements[j+1] = elements[j+1], elements[j]
                swapped = True
        if not swapped : 
            break
        
    return elements

if __name__ == "__main__":
    elements = [1,2,4,3,5]
    elements = bubble_sort(elements)
    print(elements)

    # python also sort alphabets
    dictiionary = ["zab", "zza", "aba", "aab"]
    dictiionary = bubble_sort(dictiionary)
    print(dictiionary)

