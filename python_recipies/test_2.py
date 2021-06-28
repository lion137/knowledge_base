# tests for python 2
import various_decorators as vd



@vd.trace
@vd.meassure_time
def fibo(n):
    if n <= 1: return 1
    return fibo(n - 1) + fibo(n - 2)


print(fibo(3))