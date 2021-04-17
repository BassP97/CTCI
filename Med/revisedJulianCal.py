#Problem from reddit daily programming:
    #https://old.reddit.com/r/dailyprogrammer/comments/b0nuoh/20190313_challenge_376_intermediate_the_revised/

#Background:
    #The Revised Julian Calendar is a calendar system very similar to the familiar Gregorian Calendar,
    #but slightly more accurate in terms of average year length. The Revised Julian Calendar has a
    #leap day on Feb 29th of leap years as follows:

        #Years that are evenly divisible by 4 are leap years.
        #Exception: Years that are evenly divisible by 100 are not leap years.
        #Exception to the exception: Years for which the remainder when divided by 900 is either 200
            #or 600 are leap years.

#Challenge:
    #Given two positive year numbers (with the second one greater than or equal to the first), find
    #out how many leap days (Feb 29ths) appear between Jan 1 of the first year, and Jan 1 of the second
    #year in the Revised Julian Calendar. This is equivalent to asking how many leap years there are in the
    #interval between the two years, including the first but excluding the second.

    #For this challenge, you must handle very large years efficiently, much faster than
    #checking each year in the range.

def leaps(startYear, endYear):
    leapYears = 0
    yearDiff = endYear-startYear

    #Rule 1 - gives us the number of naive leap years - years divisible by 4
    if(yearDiff <= 3):
        for i in range(startYear, endYear):
            if i%4 == 0:
                leapYears+=1
    else:
        leapYears = yearDiff//4

    #rule 2 - slightly less naive number of leap years - years divisible by 4 minus
                #years divisible by 100
    if (yearDiff>=100):
        leapYears -= yearDiff//100
    elif(startYear%100==0):
        leapYears -= 1

    #Gets us to the first year divisible by 100
    if(startYear%100 != 0):
        firstHundred = startYear//100
        firstHundred = firstHundred + 1
        firstHundred = firstHundred * 100
    else:
        firstHundred = startYear

    #Rule 3 - if a year divided by 900 has remainder 200 or 600 then we add it back in
        #as a leap year
    if(firstHundred < endYear):
        for i in range(firstHundred, endYear, 100):
            if (i%900 == 200 or i%900 == 600):
                leapYears += 1
    return leapYears


def main():
    assert(leaps(2016, 2017) == 1), "test 1 failed"
    assert(leaps(2019, 2020) == 0), "test 2 failed"
    assert(leaps(1900, 1901) == 0), "test 3 failed"
    assert(leaps(2000, 2001) == 1), "test 4 failed"
    assert(leaps(2800, 2801) == 0), "test 5 failed"
    assert(leaps(123456, 123456) == 0), "test 6 failed"
    assert(leaps(1234, 5678) == 1077), "test 7 failed"
    assert(leaps(123456, 7891011) == 1881475), "test 8 failed"

    print("All tests passed! Good Job!")

main()
