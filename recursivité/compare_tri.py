import random
import time as t

L = [random.randint(0,100) for i in range(10000)]


def fusion_it(t1,t2):
    i1, i2, n1, n2 = 0, 0, len(t1), len(t2)
    t=[]
    while i1 < n1 and i2 < n2:
        if t1[i1] < t2[i2]:
            t.append(t1[i1])
            i1 += 1
        else:
            t.append(t2[i2])
            i2 += 1
    if i1 == n1:
        t.extend(t2[i2:])
    else:
        t.extend(t1[i1:])
    return t

#########################################################################################################
                                    #FONCTIONS DE TRI#
#########################################################################################################


def tri_separe(L):
    if len(L) < 2:
        return L
    m = len(L) // 2
    return fusion_it(tri_separe(L[:m]),tri_separe(L[m:]))


t1 = t.time()
L2 = tri_separe(L)
t2 = t.time()
print("tri separe =", t2-t1)
random.shuffle(L)


def bubble_sort(l):
    for i in range(len(l)):
        for j in range(len(l)-1-i):
            if l[j] > l[j+1]:
                l[j], l[j+1] = l[j+1], l[j]
    return l


t3 = t.time()
bubble_sort(L)
t4 = t.time()

print("tri bulle =", t4-t3)
random.shuffle(L)


def selection_sort(l):
    for i in range(len(l)):
        min_index = i
        for j in range(i+1, len(l)):
            if l[j] < l[min_index]:
                min_index = j
        l[i], l[min_index] = l[min_index], l[i]
    return l


t5 = t.time()
selection_sort(L)
t6 = t.time()

print("tri selection =", t6-t5)
random.shuffle(L)


def insertion_sort(l):
    for i in range(1, len(l)):
        j = i
        while j > 0 and l[j] < l[j-1]:
            l[j], l[j-1] = l[j-1], l[j]
            j -= 1
    return l


t7 = t.time()
insertion_sort(L)
t8 = t.time()

print ("tri insertion =",t6-t5)







