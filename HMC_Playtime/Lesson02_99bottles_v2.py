beer_first=99
beer_second=beer_first-1
beer_store=beer_first

def plural(x):
	if x==1:
		return ""
	else:
		return "s"

while beer_second>-2:
	if beer_second>-1:
		print """{0} bottle{2} of beer on the wall, {0} bottle{2} of beer!
		Take one down, pass it around, {1} bottle{3} of beer on the wall!""".format(beer_first,beer_second,plural(beer_first),plural(beer_second))
	else:
		print """{0} bottle{2} of beer on the wall, {0} bottle{2} of beer!
		Let's go to the store and buy some more, {1} bottle{3} of beer on the wall!""".format(beer_first,beer_store,plural(beer_first),plural(beer_store))
	beer_first-=1
	beer_second-=1
