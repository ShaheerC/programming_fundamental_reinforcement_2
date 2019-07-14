#PROGRAMMING FUNDAMENTAL REINFORCEMENT PART 2

list_train = [
{'train': "72C", 'frequency_in_minutes': 15, 'direction': "north"},
{'train': "72D", 'frequency_in_minutes': 15, 'direction': "south"},
{'train': "610", 'frequency_in_minutes': 5, 'direction': "north"},
{'train': "611", 'frequency_in_minutes': 5, 'direction': "south"},
{'train': "80A", 'frequency_in_minutes': 30, 'direction': "east"},
{'train': "80B", 'frequency_in_minutes': 30, 'direction': "west"},
{'train': "110", 'frequency_in_minutes': 15, 'direction': "north"},
{'train': "111", 'frequency_in_minutes': 15, 'direction': "south"}
]

#1
train_111_direction = list_train [7] ['direction']
print(train_111_direction)

#2
train_80b_frequency = list_train [5] ['frequency_in_minutes']
print(train_80b_frequency)

#3
train_610_direction = list_train [2] ['direction']
print(train_610_direction)

#4
empty_list = []

for y in list_train:
    if 'direction' == "north":
        empty_list.append(y)
print(empty_list)