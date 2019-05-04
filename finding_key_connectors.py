import operator
import numpy as np
from collections import Counter, defaultdict

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
# User's friends of friend can be suggested as a potential friend to the user
def not_same_person(user, other_user):
    # We need to avoid suggesting the same person as potential friend to himself
    return (user["id"] != other_user["id"])  # returns true if user and the other_user id is not the same


def is_direct_friend(user, other_user):
    return all(not_same_person(friend, other_user) for friend in user['friends'])


def friends_of_friend_ids(user):
    return Counter(foaf['id']
     for friend in user["friends"]
     for foaf in friend["friends"]  # foaf denotes friends of a friend
     if  not_same_person(user, foaf) and is_direct_friend(user, foaf))


friends_of_friend_ids(users[3])

# Data Scientists Interests
interests = [
    (0, "Hadoop"), (0, "Big Data"), (0, "HBase"), (0, "Java"),
    (0, "Spark"), (0, "Storm"),  (0, "Cassandra"),
    (1, "NoSQL"), (1, "MongoDB"), (1, "Cassandra"), (1, "HBase"),
    (1, "Postgres"), (2, "Python"), (2, "scikit-learn"), (2, "scipy"),
    (2, "numpy"), (2, "statsmodels"), (2, "pandas"), (3, "R"), (3, "Python"),
    (3, "statistics"), (3, "regression"), (3, "probability"),
    (4, "machine learning"), (4, "regression"), (4, "decision trees"),
    (4, "libsvm"), (5, "Python"), (5, "R"), (5, "Java"), (5, "C++"),
    (5, "Haskell"), (5, "programming languages"), (6, "statistics"),
    (6, "probability"), (6, "mathematics"), (6, "theory"),
    (7, "machine learning"), (7, "scikit-learn"), (7, "Mahout"),
    (7, "neural networks"), (8, "neural networks"), (8, "deep learning"),
    (8, "Big Data"), (8, "artificial intelligence"), (9, "Hadoop"),
    (9, "Java"), (9, "MapReduce"), (9, "Big Data")
]

def data_scientists_who_like(target_interest):
    # same logic as before, however brief and easy to understand
    return [user_id for user_id, user_interest in interests if user_interest == target_interest]

data_scientists_who_like("Python")

# keys are interests, values are list of user_ids with that interest
user_ids_by_interest = defaultdict(list)

for user_id, user_interest in interests:
    user_ids_by_interest[user_interest].append(user_id)  # since the value is a list, we just append

# And another from users to interests
interests_by_user_id = defaultdict(list)

for user_id, user_interest in interests:
    interests_by_user_id[user_id].append(user_interest)

# Who has most interests in common with the given user
def most_common_interests_with(user):
    return Counter(user_ids
                    for interests in interests_by_user_id[user['id']]
                    for user_ids in user_ids_by_interest[interests]
                    if (user_ids != user['id']))













