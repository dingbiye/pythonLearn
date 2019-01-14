import pickle
with open ('a.txt', 'rb') as read:
    list = pickle.load(read)
print(list)
