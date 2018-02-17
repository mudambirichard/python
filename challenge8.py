def abbreviator(string):
   if len( string) < 5:
      return string
    
   else:
     return string[0:4] + "."
 
print (abbreviator("Trinket"))
print (abbreviator("Arg"))                  
