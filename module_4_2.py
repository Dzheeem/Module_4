def test_function():
    def inner_function():
        print('Я в области видимости функции test_function')
    inner_function()    #В консоли ничего не происходит, так как test_function не вызывалась
inner_function()    #Выдает ошибку, так как в глобальной области видимости этой функции нету
