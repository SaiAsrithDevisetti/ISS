list = []
n=10
for i in range(n):
    element = input("Enter the name: ")
    list.append(element)

validator = input("Enter the sorting type: ")
if validator == "ascending":
    print("Sorted in ascending order")
    list.sort()
    for i in range(n):
        print(list[i])
if validator == "descending":
    print("Sorted in descending order")
    list.sort(reverse=True)
    for i in range(n):
        print(list[i])

extra = input("Enter the extra name to the list: ")
list.append(extra)
if validator == "ascending":
    print("Sorted in ascending order")
    list.sort()
    for i in range(n + 1):
        print(list[i])
if validator == "descending":
    print("Sorted in descending order")
    list.sort(reverse=True)
    for i in range(n + 1):
        print(list[i])