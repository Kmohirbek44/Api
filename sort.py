# entered_list = input("Sonlarni probel bilan kiriting: ").split()
# num_set = set(map(int, entered_list))
# num_list=list(num_set)
# print("Natija:", num_list[-1]*num_list[-2]*num_list[-3])
#
# array=[
#     (10,20),
#     (30,40),
#     (70,80),
#     (90,100),
# ]
# p=[a[0]*a[1] for a in array ]
# a=filter(lambda x:x[0]*x[1]>sum(p)/len(p),array)
# print(p)
a=[1,2,3]
b=[i**2 for i  in a]
for i in b:
    print(i)
