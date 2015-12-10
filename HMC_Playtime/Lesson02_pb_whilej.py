# Difficulty level: Beginner

# Goal #1: Write a new version of the PB&J program that uses a while loop.  Print "Making sandwich #" and the number of the sandwich until you are out of bread, peanut butter, or jelly.

# Example:
# bread = 4
# peanut_butter = 3
# jelly = 10

# Output:
# Making sandwich #1
# Making sandwich #2
# All done; only had enough bread for 2 sandwiches.

print "Goal #1 Output:"
bread=4
pb=2
jelly=3
sandwich=0

while bread>=2 and pb>=1 and jelly>=1:
	sandwich=sandwich+1
	bread=bread-2
	pb=pb-1
	jelly=jelly-1
	print "Making sandwich #{0}".format(sandwich)

limiting_ingredient=[]

if bread<2:
	limiting_ingredient.append("bread")
if pb<1:
	limiting_ingredient.append("pb")
if jelly<1:
	limiting_ingredient.append("jelly")
limiting_ingredient=" and ".join(limiting_ingredient)

if sandwich==1:
	plural=""
else:
	plural="es"

print "All done; only had enough {0} for {1} sandwich{2}.".format(limiting_ingredient,sandwich,plural)

# Goal #2: Modify that program to say how many sandwiches-worth of each ingredient remains.

# Example 2:
# bread = 10
# peanut_butter = 10
# jelly = 4

# Output:
# Making sandwich #1
# I have enough bread for 4 more sandwiches, enough peanut butter for 9 more, and enough jelly for 3 more.
# Making sandwich #2
# I have enough bread for 3 more sandwiches, enough peanut butter for 8 more, and enough jelly for 2 more.
# Making sandwich #3
# I have enough bread for 2 more sandwiches, enough peanut butter for 7 more, and enough jelly for 1 more.
# Making sandwich #4
# All done; I ran out of jelly.

print "Goal #2 Output:"

bread=2
pb=2
jelly=1
sandwich=0

while bread>=2 and pb>=1 and jelly>=1:
	sandwich=sandwich+1
	bread=bread-2
	pb=pb-1
	jelly=jelly-1
	if bread==2:
		plural=""
	else:
		plural="es"
	print """Making sandwich #{0}
	I have enough bread for {1} more sandwich{4}, enough peanut butter for {2} more, and enough jelly for {3} more. """.format(sandwich,bread/2,pb, jelly, plural)

limiting_ingredient=[]

if bread<2:
	limiting_ingredient.append("bread")
if pb<1:
	limiting_ingredient.append("pb")
if jelly<1:
	limiting_ingredient.append("jelly")

limiting_ingredient=" and ".join(limiting_ingredient)

print "All done; I ran out of {0}.".format(limiting_ingredient,sandwich)
