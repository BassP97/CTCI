"""
Write a program in your language of choice that prints the numbers from 1 to 100. But for multiples of three print “right” instead of the number and for the multiples of five print “point”. For numbers which are multiples of both three and five print “rightpoint”.*
"""

def rightPoint():
    for i in range(1,101):
        output = ""
        if (i%3==0):
            output = output+"right"
        if (i%5==0):
            output = output+"point"
        if output == "":
            print (i)
        else:
            print(output)
rightPoint()