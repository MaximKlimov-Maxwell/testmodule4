#1 решение
# def strcounter(s): #O(2*N) ~ O(N)
#     adict = {}
#     for i in s:
#         adict[i] = adict.get(i, 0) + 1
#     for j in adict:
#         print(j, adict[j])
# 
# strcounter('abcda')

#2 решение

# def strcounter(s): #O(N**2)
#     for sym in s:
#         count = 0
#         for sub_sym in s:
#             if sub_sym == sym:
#                 count += 1
#         print(sym, count)

def strcounter(s): #O(N*M)
    for sym in set(s):
        count = 0
        for sub_sym in s:
            if sub_sym == sym:
                count += 1
        print(sym, count)

strcounter('abcccd')



    