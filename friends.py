import random

def clean(f):
    return open(f,'rU').read().split('\n')

def pick(l):
    return l[random.choice(range(0,len(l)))].title()

def grab(l):
    p = []
    for i in l:
        if i[-1] == 's' and i[-2] != 's':
            p.append(i)
        else:
            pass
    return p

def s1(c,v,n):
    v1 = ""
    v2 = " the "+n
    opts = [v1,v2]
    return "The One where "+c+" "+v+random.choice(opts)

def s2(c,n):
    v1 = "the "+n
    v2 = c+"'s "+n
    opts = [v1,v2]
    return "The One with "+random.choice(opts)

if __name__ == "__main__":
    characters = ['Ross','Chandler','Joey','Rachel','Monica','Phoebe']
    c = pick(characters)
    n = pick(clean('nounlist.txt'))
    v = pick(grab(clean('verblist.txt')))

    print random.choice([s1(c,v,n),s2(c,n)])
