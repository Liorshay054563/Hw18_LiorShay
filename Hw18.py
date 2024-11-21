# start --- Hw18 - tuple
# 1
# a


tup: (int,) = (9,)
# b
tup1: tuple[int, int, int] = (77, 88, 99)


# c
def len_tup(x):
    """print the length of tuple"""
    x = len(x)
    return x


print(len_tup(tup1))


# d
def together_tup(x, y):
    """print the sum"""
    return x + y


print(together_tup(tup, tup1))


# e
def same_num(x, y):
    """find the same numbers in the tuples"""
    same = [i for i in x if i in y]
    return tuple(same)
    # same2 = []
    # for n in (x):
    #     if n in y:
    #         same2.append(n)
    # return same2


ex_tup = (3, 4, 5, 6)
ex_tup2 = (1, 2, 3, 4)


# f
def different_num(x, y):
    """find the different numbers in the tuples"""
    different = [i for i in x if i not in y]
    return tuple(different)


print(different_num(ex_tup, ex_tup2))


# g
def index_tuple(x, y):
    """find the value in tuple from the index"""
    if 0 <= y <= len(x):
        return x[y]
    else:
        return None


print(index_tuple((1, 2, 3, 4), 3))  # why only on number "4" is error?


# h
def revers_tup(x):
    """print reversed tuple"""
    return x[::-1]


print(revers_tup((8, 9, 10, 11)))


# i
def mul_tuple(x, y):
    """multiply the tuple be 'y'"""
    return tuple(x) * y

print(mul_tuple(ex_tup, 3))

# j
def without_num(xtuple, num):
    """create new tuple without 'num'"""
    new_tup = []
    for i in xtuple:
        if i == num:
            continue
        new_tup.append(i)
    return tuple(new_tup)

print(without_num((1, 2, 3, 4, 5), 5))

# k
def uniqe_tuple(x):
    """create new tuple that have only one from each numer"""
    # new_uniqec= [i for i in x if i not in] # i try to do comprh
    new_uniqe = []
    for i in x:
        if i not in new_uniqe:
            new_uniqe.append(i)
    return tuple(new_uniqe)

print(uniqe_tuple((4, 5, 6, 7, 7, 4)))
# j

# m
grades_t: list[int] = []
names: list[str] = []
while True:
    grade: int = int(input("enter your grade:"))
    if grade == -999:
        break
    if not 0 < grade <= 100:
        continue
    grades_t.append(grade)
while True:
    name: str = input("enter your name:")
    if name == "done":
        break
    names.append(name)
zip_t = zip(names, grades_t)
print(zip_t)

## 2
#the different about 'list' and 'tuple' is that 'tuple' you cant change
#I prefer to you in 'tuple' if i want to keep him permanently without /
# - the ability to change

##3
# it's not an error because the changes is in {dict} from the 'tuple' - Thats OK
