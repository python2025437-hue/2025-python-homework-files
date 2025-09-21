'''One cause for speeding is the desire to shorten the time spent traveling.
Create a program that calculates the amount of time saved if you are traveling with an average
speed that is above the speed-limit as compared to traveling with an average speed exactly at the speed-limit.
As the user for the average speed in miles per hour, speed limit in miles per hour and distance travelled in
miles. THE TIME SAVED SHOULD BE REPORTED IN MINUTES. Create a screenshot of output where your average speed
is 80 mph, speed limit is 60 mph and distance travelled is 100 miles.
Your answer should indicate that you saved 25 minutes, '''


currentspeed = int(input('Your current speed = '))
speedlimit = int(input('The current speed limit = '))
distance = int(input('Distance to be traveled = '))


time = distance / speedlimit

speedingtime = distance / currentspeed


MinutesInHour = 60


speedingmins = speedingtime * MinutesInHour

limitmins = time * MinutesInHour


if speedingmins < limitmins:
    savedtime = limitmins - speedingmins
    print(savedtime)
    print('You saved ' + str(savedtime) + ' mins!')
else:
    print('No time saved.')



