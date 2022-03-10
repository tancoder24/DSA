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

def bubble_sort_dict(dictionary, key):
    size = len(dictionary)
    
    for i in range(size-1):
        swapped = False
        for j in range(size-1):
            if dictionary[j][key] > dictionary[j+1][key]:
                dictionary[j], dictionary[j+1] = dictionary[j+1], dictionary[j]
                swapped = True
        if not swapped: 
            break
    return dictionary

if __name__ == "__main__":
    # 1st case
    elements = [1,2,4,3,5]
    elements = bubble_sort(elements)
    print(elements)

    # python also sort alphabets
    dictionary = ["zab", "zza", "aba", "aab"]
    dictionary = bubble_sort(dictionary)
    print(dictionary)

    # dictionary sort
    elements = [
        { 'name': 'mona',   'transaction_amount': 1000, 'device': 'iphone-10'},
        { 'name': 'dhaval', 'transaction_amount': 400,  'device': 'google pixel'},
        { 'name': 'kathy',  'transaction_amount': 200,  'device': 'vivo'},
        { 'name': 'aamir',  'transaction_amount': 800,  'device': 'iphone-8'},
    ]

    print( bubble_sort_dict(elements,key='transaction_amount') )
    print( bubble_sort_dict(elements,key='name') )
    print( bubble_sort_dict(elements,key='device') )
