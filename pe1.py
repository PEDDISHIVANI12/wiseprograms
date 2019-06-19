def fibbanoci(num):
    list1 = [1,2]
    while sum(list1[-2:]) < num:
        list1.append(sum(list1[-2:]))
    return sum([ i for i in list1 if i % 2 == 0])
print(fibbanoci(4000000))

