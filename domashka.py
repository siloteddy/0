import os

folder = os.getcwd() + '\data\\'
walk = os.walk(folder)

for line in walk:
    print(line)    

files = line[2]   


# проанализировать папку
# сколько файлов в папке?
# сколько файлов в папке в имени имеют цифру?
# сколько файлов в папке в имени имеют букву g?
# сколько файлов в папке в имени имеют 2 буквы g подряд?
# сколько файлов в папке в имени имеют сумму чисел больше 10?

# task 1
print(len(files))

# task 2
count = 0
for i in files:
    for j in '1234567890':
        if j in i:
            count += 1
            break
print(count)

# task 3
count = 0
for i in files:
    if 'g' in i:
        count += 1
        continue
print(count)

# task 4
count = 0
for i in files:
    if 'gg' in i:
        count += 1
        continue
print(count)

# task 5
# count = 0
# for i in files:









# import random
# alphabet = 'abcdefghijklmnopqrstuvwxyz'
# nums = '1234567890'

# for i in range(500):
#     has_nums = random.randint(1,10) > 7  

#     name = folder

#     for i in range(random.randint(5,40)):
#         name += random.choice(alphabet)
#         if has_nums and random.randint(1,10) > 7 :
#             name += random.choice(nums)   

#     name += '.txt' 
   
#     with open(name, 'w', encoding='utf8') as f:
#         f.write('lol')

