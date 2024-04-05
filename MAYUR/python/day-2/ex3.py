# Ex-2.3
# Convert hours and Minutes into Seconds
# example format 01:22:20 => 4940


    
    
def get_sec(time_str):
    """Get seconds from time."""
    h, m, s = time_str.split(':')
    return int(h) * 3600 + int(m) * 60 + int(s)


print(get_sec('1:23:45'))
print(get_sec('0:22:15'))
print(get_sec('0:00:25'))
  