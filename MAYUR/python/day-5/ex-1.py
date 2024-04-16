# Ex-5.1
# Create a function that takes an angle in radians and returns the corresponding angle in degrees rounded to one decimal place.


# Python code to convert radian to degree


def Convert(radian):
	pi = 3.1415
	degree = radian * (180/pi)
	return degree

radian = 5
print("degree =",(Convert(radian)))


