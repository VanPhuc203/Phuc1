
class mathmethods:
    def fibonacci_recursive(self,n):
        if n<0:
            print("invalid input")
        elif n==0:
            return 0
        elif n==1 or n==2:
            return 1
        else:
            return
        self.fibonacci_recursive(n-1)+self.fibonacci_recursive(n-2)
    def fibonacci_non_recursive(self,n):
        if n<0:
            print("Invalid input")
        elif n==0:
            return 0
        elif n==1:
            return 1
        else:
            a,b=0,1
            for i in range(2,n+1):
                a,b= b,a+b
                return b
mathmethods = mathmethods()
print(mathmethods.fibonacci_recursive(1))