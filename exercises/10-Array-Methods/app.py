names = ['John', 'Kenny', 'Tom', 'Bob', 'Dilan']
## CREATE YOUR FUNCTION HERE
def sort_names(arr):
    return sorted(arr,key=str.lower)

print(sort_names(names))
