arr = input("enter the list of numbers seperated by space: ").split()
arr = [int(x) for x in arr]
target = int(input("enter the target value to search:"))

found= False

for i in range(len(arr)):
    if arr[i] == target:
        print(f"Element {target} found at index {i}")
        found = True
        break
if not found:
    print(f"target {target} not found in the array")