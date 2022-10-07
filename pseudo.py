def store(text, prefix, n, k):
    arr = []
    def perm(text, prefix, n, k):
        if k == 0: 
            if (count(list(prefix), "1") > count(list(prefix), "2")):
                arr.append(prefix)
            return  
        for i in range(n): 
            new_prefix = prefix + text[i] 
            perm(text, new_prefix, n, k-1)
    perm(text, prefix, n, k)
    print(len(arr))

def count(list, x):
    return list.count(x)

def permutation_repeat(text, k):
    store(text, "", len(text), k)
permutation_repeat("012", 3)