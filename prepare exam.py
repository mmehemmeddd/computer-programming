import random
old_list=[1,2,3,4,5,6,7,8]
# a=[ number for number  in old_list if number%2==1]
# print(a)
print([i*i for i in old_list if i%2==0])
print([number for number in old_list if number>4 and number<9])
new_list=[2,4,3,7,12,21]
print([i*i for i in old_list if i not in new_list])
r = [1, 2]
h = ['a', 'b']
res = [(x, y) for x in r for y in h]
# res siyahısının bütün elementlərini yazın
print(res)
m = [[1], [2, 3]]
flat = [item for sub in m for item in sub]
# flat-ın son halı necədir?
print(flat)
num=[1,2,3,4]
let="abcd"
com=[(number,letter) for number in num for letter in let]
print(com)
list=["Ag","qara","Cehrayi"]
random.sample(list,2)
print(list)
import
def kub_are(a)
return a**3