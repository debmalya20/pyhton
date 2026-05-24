def factoril(n):
    if(n==0 or n==1):
        return 1
    else:
        return n* factoril(n-1)
    
print(factoril(5))