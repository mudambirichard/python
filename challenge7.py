def how_many(the_list):
    
    if the_list[0]==1:
        return "There is " + str(the_list[0]) + "" + the_list[1]
    
    else:
         return "There are " +  str(the_list[0]) + "" + the_list[1] + "s."

print (how_many([5, "trinket"]))
print (how_many([1, "king"]))

    
