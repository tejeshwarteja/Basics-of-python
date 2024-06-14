def reverse_list(l, i=0):
    if i >= len(l) // 2:
        return l
    l[i], l[-1-i] = l[-1-i], l[i]
    return reverse_list(l, i+1)

l = [2, 3, 5, 6, 7, 9, 11]
print(reverse_list(l)) 










