def outer_function(msg):
    #message = msg

    def inner_function():
        #print(message)
        print(msg)
    return inner_function

hi_fn = outer_function('hi')
hi_fn()

bye_fn = outer_function('bye')
bye_fn()

