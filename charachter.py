def transformSentence(sentence):
    l=sentence.split()
    
    li=[]
    st=""
    for i in l:
        st+=i[0]
        for j in range(0,len(i)-1):
            if(i[j].lower()<i[j+1].lower()):
                st+=(i[j+1].upper())
            elif(i[j].lower()>i[j+1].lower()):
                st+=(i[j+1].lower())
            else:
                st+=i[j+1]
        li.append(st)
        st=""
    result=""
    
    for i in li:
        result=result+" "+i
    return (result.strip())
    # Write your code here


n=input()
print(transformSentence(n))