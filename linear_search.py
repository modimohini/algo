
def linear_search(listt, target):
    """ return the index position of target if found else return none"""
    for i in range (0, len(listt)):
        if listt[i] ==  target:
            return i
        return None 

def verify(index):
    if index is not None:
        print("target found at index: ", index)
    else:
        print("target not found in list")

numbers = [1,2,3,4,5,6]

result = linear_search(numbers,2)
verify(result)

result = linear_search(numbers,12)
verify(result)