students = [
    ("Abrar Zaved Sharafi",10),
    ("Eirik",5),
    ("Himiko",1),
]
def sort_item(item):
    return item[1]

students.sort(key=sort_item)
print(students)

x=list(filter(lambda students: students[1]>=10,students))
print(x)