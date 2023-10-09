sentence = "This is a common interview question"
new = [*sentence]
max=0
for x in new:
    c=new.count(x)
    if c>max:
        max=c

for x in new:
    if max==new.count(x):
        print(x,"is the most frequent letter with",max,"times")
        break
