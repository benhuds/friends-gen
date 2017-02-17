import random

def getWords(f):
    return open(f,'rU').read().split('\n')

def pick(l):
    return random.choice(l).title()

def s():
    characters = ['Ross','Chandler','Joey','Rachel','Monica','Phoebe']
    c = pick(characters)
    n = pick(getWords('nounlist.txt'))
    v = pick(filter(lambda x: x[-1] == 's' and x[-2] != 's', getWords('verblist.txt')))
    return random.choice([s1(c,v,n),s2(c,n)])

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
    print s()
