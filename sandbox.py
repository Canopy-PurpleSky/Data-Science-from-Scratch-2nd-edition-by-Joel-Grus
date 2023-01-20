import random

running = True
users = [
 { "id": 0, "name": "Hero" },
 { "id": 1, "name": "Dunn" },
 { "id": 2, "name": "Sue" },
 { "id": 3, "name": "Chi" },
 { "id": 4, "name": "Thor" },
 { "id": 5, "name": "Clive" },
 { "id": 6, "name": "Hicks" },
 { "id": 7, "name": "Devin" },
 { "id": 8, "name": "Kate" },
 { "id": 9, "name": "Klein" }
]

friendship_pairs = [(0, 1), (0, 2), (1, 2), (1, 3), (2, 3), (3, 4),
 (4, 5), (5, 6), (5, 7), (6, 8), (7, 8), (8, 9)]

friendships = {user["id"]:[] for user in users}
potential_friends = {user["id"]:[]for user in users}

for i,j in friendship_pairs:
    friendships[i].append(j)
    friendships[j].append(i)


def foaf(user):
    user_name = user["name"]
    user_ids = user["id"]
    friend_list = friendships[user_ids]
    friend_oaf = set()

    for friend in friend_list:
        foaf_id = friendships[friend]
        friend_oaf.update(friendships[friend])
        friend_oaf.discard(user_ids)
    
    for shit in friend_list:
        if shit in friend_oaf:
            friend_oaf.discard(shit)

    print(f'{user_name}({user_ids}) is potentially friends with {friend_oaf}')


while running:
    user = input("User_id: ")
    user_int = int(user)

    #getting the dictionary from the users list
    point = users[user_int]
    foaf(point)
