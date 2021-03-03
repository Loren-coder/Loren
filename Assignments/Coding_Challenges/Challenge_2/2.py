# 2. List overlap

list_a = ['dog', 'cat', 'rabbit', 'hamster', 'gerbil']
list_b = ['dog', 'hamster', 'snake']

overlap=set(list_a) & set(list_b)
unique=set(list_b) ^ set(list_a)
print (overlap)
print (unique)

# Feedback - Excellent!