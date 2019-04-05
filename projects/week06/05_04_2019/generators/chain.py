# impl 1 #
# def chain(iter1, iter2):
#     new_iter = []
#     for el in iter1:
#         new_iter.append(el)
    
#     for el in iter2:
#         new_iter.append(el)

#     return new_iter

# impl 2 #
# def chain(iter1, iter2):
#     new_iter = []
    
#     i1 = iter(iter1)
#     i2 = iter(iter2)

#     while iter1:
#         try:
#             new_iter.append(next(i1))
#         except StopIteration:
#             break
        
#     while iter2:
#         try:
#             new_iter.append(next(i2))
#         except StopIteration:
#             break

#     return new_iter

# impl 3 #
def chain(iter1, iter2):
    
    i1 = iter(iter1)
    i2 = iter(iter2)

    while iter1:
        try:
            yield next(i1)
        except StopIteration:
            break

    while iter2:
        try:
            yield next(i2)
        except StopIteration:
            break

print(list(chain(range(0, 4), range(4, 8))))
print(list(chain((1, 2), (4, 8))))
