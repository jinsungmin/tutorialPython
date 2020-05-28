"""
items = 'zero one two three'
a,b,c,d = items.split()
print(b)

"""
"""
colors = ['red', 'blue', 'green', 'yellow']
result = ''.join(colors)
print(result)

result2 = '-'.join(colors)
print(result2)
"""
# result = []
# for i in range(10):
#     result.append(i)

# result1 = [i for i in range(10)]    # normal
# print(result1)
#
# result2 = [i for i in range(10) if i % 2 == 0]  # filter
# print(result2)

# word_1 = "Hello"
# word_2 = "World"
# result = [i+j for i in word_1 for j in word_2]
# print(result)

# words = "The quick brown fox jumps over the lazy dog".split()
#
# stuff = [[w.upper(), w.lower(), len(w)] for w in words]
# for i in stuff:
#     print(i)

# case_1 = ["A","B","C"]
# case_2 = ["D","E","F"]
# result = [[a+b for a in case_1] for b in case_2]
# print(result)

# for i,v in enumerate(['tic', 'tac', 'toc']):
#     print(i,v)
#
# mylist = ["a","b","c","d"]
# print(list(enumerate(mylist)))  # [(0, 'a'), (1, 'b'), (2, 'c'), (3, 'd')]
# print({i:j for i,j in enumerate('Chungang University is an academic institute located in South Korea.'.split())})

# print([sum(x) for x in zip((1,2,3), (10,20,30), (100,200,300))]) # [111, 222, 333]
#
# alist = ['a1', 'a2', 'a3']
# blist = ['b1', 'b2', 'b3']
#
# for i, (a,b) in enumerate(zip(alist, blist)):
#     print(i,a,b) # index alist[index] blist[index] 표시


# from functools import reduce
#
# def factorial(n):
#     return reduce(
#         lambda x, y:x*y, range(1,n+1))
#
# print(factorial(5))

# def asterisk_test(a, *args):
#     print(a,args)
#     print(type(args))
#
# asterisk_test(1,2,3,4,5,6)  # 1 (2, 3, 4, 5, 6)

# def asterisk_test(a, **kargs):  # 1 {'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6}
#     print(a, kargs)
#     print(type(kargs))
#
# asterisk_test(1, b=2,c=3,d=4,e=5,f=6)

# for data in zip(*([1,2],[3,4],[5,6])):  #(1, 3, 5)
#     print(data)                         #(2, 4, 6)

# from collections import OrderedDict
# d = OrderedDict()
# d['l'] = 500
# d['x'] = 100
# d['y'] = 200
# d['z'] = 300
# for k,v in OrderedDict(sorted(d.items(), key=lambda t: t[1])).items():
#     print(k,v)

# from collections import deque
# import time
#
# start_time = time.clock()
# deque_list = deque()
# # stack
# for i in range(10000):
#     for i in range(10000):
#         deque_list.append(i)
#         deque_list.pop()
# print(time.clock() - start_time, "seconds")

# matrix_a = [[3,6],[4,5]]
# matrix_b = [[5,8],[6,7]]
# result = [[sum(row) for row in zip(*t)]
#             for t in zip(matrix_a, matrix_b)]
# print(result)

# matrix_a = [[1,2,3],[4,5,6]]
# result = [[element for element in t] for t in zip(*matrix_a)]
# print(result)   # [[1, 4], [2, 5], [3, 6]] (Transpose)





