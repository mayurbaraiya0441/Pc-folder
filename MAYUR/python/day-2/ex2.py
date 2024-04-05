# Ex-2.2
# In cricket, an over consists of six deliveries a bowler bowls from one end. Create a program that takes the number of balls bowled by a bowler and calculates the number of overs and balls bowled by him/her. Return the value as a float, in the format overs.balls.
# Example : 15 => 2.3
# 	  24 => 6.0
# 	  05 => 0.5



def calculate_overs_and_balls(balls):
    overs = balls // 6
    remaining_balls = balls % 6
    overs_bowled = overs + (remaining_balls / 10)
    return overs_bowled

# Test cases
print(calculate_overs_and_balls(15))  # Output: 2.3
print(calculate_overs_and_balls(24))  # Output: 4.0
print(calculate_overs_and_balls(5))   # Output: 0.5
