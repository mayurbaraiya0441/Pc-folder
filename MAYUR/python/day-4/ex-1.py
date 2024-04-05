# Create a function that returns the amount of duplicate characters in a string. It will be case sensitive and spaces are included. If there are no duplicates, return 0.



    
str = "great responsibility  __"
duplicate_char = []
for character in str:
  
      if str.count(character) > 1:
   
         if character not in duplicate_char:
            duplicate_char.append(character)
print(*duplicate_char)