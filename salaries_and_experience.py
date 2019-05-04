import matplotlib.pyplot as plt
import operator
from collections import defaultdict, Counter

salaries_and_tenures = [(83000, 8.7), (88000, 8.1),
                        (48000, 0.7), (76000, 6),
                        (69000, 6.5), (76000, 7.5),
                        (60000, 2.5), (83000, 10),
                        (48000, 1.9), (63000, 4.2)]

salaries_and_tenures.sort(key = operator.itemgetter(1), reverse=False)

plt.scatter(x = [years for sal, years in salaries_and_tenures], y = [sal for sal, years in salaries_and_tenures])
plt.xlabel("Years Experience")
plt.ylabel("Salary")
plt.title("Salary by Years Experience")

# keys are years, values are lists of salaries for each tenure
salary_by_tenure = defaultdict(list)

for salary, tenure in salaries_and_tenures:
    salary_by_tenure[tenure].append(salary)

average_salary_by_tenure = {
    tenure: sum(salaries)/len(salaries)
    for tenure, salaries in salary_by_tenure.items() # when iterating dictionary items must be used
}

# It might be more helpful to bucket the tenures:
def tenure_bucket(tenure):
    if tenure < 2:
        return 'less than 2'
    elif tenure < 5:
        return 'between 2 and 5'
    else:
        return 'more than 5'

# keys are tenure buckets, values are lists of salaries for that bucket
salary_by_tenure_bucket = defaultdict(list)

for salary, tenure in salaries_and_tenures:
    salary_by_tenure_bucket[tenure_bucket(tenure)].append(salary)

average_salary_by_bucket = {
 tenure_bucket : sum(salaries)/len(salaries)
 for tenure_bucket, salaries in salary_by_tenure_bucket.items()
}

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

Counter(word
for user_id, user_interest in interests
for word in user_interest.lower().split()
)

Counter(user_interest.lower() for user_id, user_interest in interests)

for user_id, user_interest in interests:
    print(user_id, user_interest.split())







