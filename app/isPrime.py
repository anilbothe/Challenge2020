class myFunction:
    """check prime number"""
    @classmethod
    def isPrime(cls, num) -> bool:
        if num > 1: 
            for i in range(2, num): 
                if (num % i) == 0: 
                    # is not a prime number
                    return False
            else: 
                # is a prime number 
                return True
        else: 
            # is not a prime number
            return False

# obj = myFunction()
# print(obj.isPrime(3))