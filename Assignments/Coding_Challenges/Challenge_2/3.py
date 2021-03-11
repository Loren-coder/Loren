# 3. Given a singe phrase, count the occurrence of each word

string = 'hi dee hi how are you mr dee'

print("hi"+ " "+str(string.count("hi")))
print("dee"+ " "+str(string.count("dee")))
print("how"+" " +str(string.count("how")))
print("are"+" "+str(string.count("are")))
print("you"+" "+str(string.count("you")))
print("mr"+" "+str(string.count("mr")))

# Technically correct, but this is a lot of manual work to do. I would suggest you do this in code instead, you can
# 1. split string to list
# 2. Count occurrences of item in teh list.



string = 'hi dee hi how are you mr dee'

list=string.split(" ")

print(list)

for i in list:
    num=string.count(i)

    print(i+" " +str(num))
