def fun(a):
    print(a)
    def fun2(a):
        print(a)
    fun2(a)

fun(5)