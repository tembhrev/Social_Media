def func(a, b=5, c=10):
    print("a:", a)
    print("b:", b)
    print("c:", c)
    
func(3, 7)
print("===========")
func(25, c=24)
print("===========")
func(c=50, a=100)