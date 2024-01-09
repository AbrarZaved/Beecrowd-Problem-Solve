id={
    "1":"Abrar Zaved Sharafi",
    "2":"Eirik",
    "3":"Himiko",
}

print(id.get("3","Not Valid"))

for x, values in id.items():
    print(x, values)

y=int(input())
values= (x*y for x in range (10))

for x in values:
    print(x)