#Slope of a line
#Description 
#This program computes the slope by taking the x and y coordinates as input and the slope formula = (y2 - y1) / (x2 - x1)

 
 



x1, y1 = map(float, input("Enter the coordinates of the first point: ").split())

#By using the input function and specifying float we are taking user input in the float data type
#Map function maps the user input to x1 and y1
#The comma after float creates a list
#The split() method splits a string into a list

x2, y2 = map(float, input("Enter the coordinates of the second point: ").split())

#By using the input function and specifying float we are taking user input in the float data type
#Map function maps the user input to x2 and y2
#The comma after float creates a list
#The split() method splits a string into a list

pair1 = (x1, y1)

#x1 and y1 is the first coordinate pair

pair2 = (x2, y2)

#x2 and y2 is the second coordinate pair

slope = (y2 - y1) / (x2 - x1)

#slope is calculated by the formula above

print("The slope of the line that connects two points" , pair1, pair2, "is" , slope)

#the output of the program is generated
