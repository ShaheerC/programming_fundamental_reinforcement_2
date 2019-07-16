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
new_trains = []

for x in list_train:
    if x ['direction'] == "north":
        new_trains.append(x['train'])
print(new_trains)

#5
east_trains = []
for x in list_train:
    if x ['direction'] == "east":
        east_trains.append(x['train'])
print(east_trains)

#6
def train_by_direction(direction): 
    train_direct_list = []

    for y in list_train:
        if (y['direction'] == direction):
            train_direct_list.append(y)
    return train_direct_list

print(train_by_direction('north'))
print(train_by_direction('east'))

#7
list_train[1]['first_departure_time'] = 6
print(list_train[1])

#8
trains = [
{'train': "72C", 'frequency_in_minutes': 15, 'direction': "north"},
{'train': "72D", 'frequency_in_minutes': 15, 'direction': "south"},
{'train': "610", 'frequency_in_minutes': 5, 'direction': "north"},
{'train': "611", 'frequency_in_minutes': 5, 'direction': "south"},
{'train': "80A", 'frequency_in_minutes': 30, 'direction': "east"},
{'train': "80B", 'frequency_in_minutes': 30, 'direction': "west"},
{'train': "110", 'frequency_in_minutes': 15, 'direction': "north"},
{'train': "111", 'frequency_in_minutes': 15, 'direction': "south"}
]

trains_by_frequency = {}
for train in trains:
    freq = train['frequency_in_minutes']
    name = train['train']
    if freq in trains_by_frequency:
        trains_by_frequency[freq].append(name)
    else:
        trains_by_frequency[freq] = [name]
print(trains_by_frequency)