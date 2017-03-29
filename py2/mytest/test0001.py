def get_number():
    numberlist=[]
    numbers=open("a.txt",'r').readlines()
    for number in numbers:
        number.strip('\n')
        numberlist.append(number)
    list=[]
    i=0
    for i in xrange(len(numberlist)):
        w={'phone':numberlist[i].strip('\n')}
        list.append(w)
        i+=1
    return list
if __name__=="__main__":
    print get_number()


def get_number(n):
    numberlist=[]
    numbers=open("a.txt",'r').readlines()
    for number in numbers:
        number.strip('\n')
        numberlist.append(number)
    list=[]
    i=0
    for i in xrange(len(numberlist)):
        w={'phone':numberlist[i].strip('\n')}
        list.append(w)
        i+=1
    return list[n]
if __name__=="__main__":
    print get_number(0)
    print get_number(-1)