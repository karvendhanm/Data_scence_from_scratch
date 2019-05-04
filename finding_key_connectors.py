import operator

# all available users
users = [
    {"id": 0, "name": "Hero"},
    {"id": 1, "name": "Dunn"},
    {"id": 2, "name": "Sue"},
    {"id": 3, "name": "Chi"},
    {"id": 4, "name": "Thor"},
    {"id": 5, "name": "Clive"},
    {"id": 6, "name": "Hicks"},
    {"id": 7, "name": "Devin"},
    {"id": 8, "name": "Kate"},
    {"id": 9, "name": "Klein"}
]

# friendship network
friendships = [(0, 1), (0, 2), (1, 2), (1, 3), (2, 3), (3, 4),
               (4, 5), (5, 6), (5, 7), (6, 8), (7, 8), (8, 9)]

# let us add another feature called "freinds" to every user
for user in users:
    user["friends"] = []

for i, j in friendships:
    users[i]["friends"].append(users[j])  # All j is added as i friend
    users[j]["friends"].append(users[i])  # All i is added as j friend

# Goal: to find the average number of freinds for each user
## function to provide number of friends if a user is given to it
def num_of_friends(user):
    '''
    this function takes in an user an returns the number of friends that particular user has
    :param user: Format dict with a feature called "friends".
    :return: number of friends
    '''
    return len(user["friends"])

## bulid a list of tuples with id and number of friends for each user.
num_friends_by_id = [(user["id"], num_of_friends(user)) for user in users]

## Now assign users in descending order deoending upon their number of friends.
num_friends_by_id.sort(key = operator.itemgetter(1), reverse=True)

# Total number of friends for all users
total_num_of_users = sum([num_of_friends(user) for user in users])
avg_num_of_friends = total_num_of_users / len(users)

# Data Scientists You May Know
def friends_of_friend_ids_bad(user):
    # return the ids of friends of a friend
    return [foaf['id']
            for friend in user['friends']  # for each of user's friends
            for foaf in friend['friends']]  # get each of _their_ friends


friends_of_friend_ids_bad(users[0])
