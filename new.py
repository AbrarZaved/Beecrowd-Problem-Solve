from collections import Counter

def stringAnagram(dictionary, query):
    dict_sorted = ["".join(sorted(word)) for word in dictionary]
    query_sorted = ["".join(sorted(word)) for word in query]
    
    result = []
    count = Counter(dict_sorted)
    
    for word in query_sorted:
        if word in count:
            result.append(count[word])
        else:
            result.append(0)

    return result

# Taking input from the user
n = int(input())
dictionary = []
query = []


for _ in range(n):
    dictionary.append(input())

a = int(input())
for _ in range(a):
    query.append(input())

# Calculate and print the results
results = stringAnagram(dictionary, query)
for res in results:
    print(res)
