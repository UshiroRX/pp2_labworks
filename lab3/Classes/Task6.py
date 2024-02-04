def Primes(nums):
    def IsPrime(x):
        for i in range(2,x//2+1):
            if x%i == 0:
                return False
        return True
    
    return list(filter(lambda x : IsPrime(x), nums))


print(Primes([1,2,3,4,5,6,7,8,9,10])) #example