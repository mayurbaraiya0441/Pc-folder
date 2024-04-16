# Ex-7.2
# Create a function that returns the selected filename from a path. Include the extension in your answer.


import os
path = '/home/quantumbot/Pictures/Screenshots/Screenshot from 2023-02-17 16-26-36.png'
print(path.split('/'))
print(os.path.basename(path).split('/')[-1])
