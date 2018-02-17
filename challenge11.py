def fruit_labeler(thing):

    if type(thing) == str:
        return 'apples'

    elif type(thing) == int:
        return 'orange'

    else:
        return 'banana'

print (fruit_labeler(4.5))
