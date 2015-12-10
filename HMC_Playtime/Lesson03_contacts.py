# Challenge Level: Beginner

# NOTE: Please don't use anyone's *real* contact information during these exercises, especially if you're putting it up on Github!

# Background: You have a dictionary with people's contact information.  You want to display that information as an HTML table.

contacts = {
	'Shannon': {'phone': '202-555-1234', 'twitter': '@svt827', 'github': '@shannonturner' },
	'Beyonce': {'phone': '303-404-9876', 'twitter': '@beyonce', 'github': '@bey'},
	'Tegan and Sara': {'phone': '301-777-3313', 'twitter': '@teganandsara', 'github': '@heartthrob'}
}

# Goal 1: Loop through that dictionary to print out everyone's contact information.

# Sample output:

# Shannon's contact information is:
#   Phone: 202-555-1234
#   Twitter: @svt827
#   Github: @shannonturner

# Beyonce's contact information is:
#   Phone: 303-404-9876
#   Twitter: @beyonce
#   Github: @bey

print "Goal #1 Output:"

for each in contacts:
	print """{0}'s contact information is:
	Phone: {1}
	Twitter: {2}
	Github: {3}""".format(each, contacts[each]['phone'], contacts[each]['twitter'],contacts[each]['github'])

# Goal 2:  Display that information as an HTML table.

# Sample output:

# <table border="1">
# <tr>
# <td colspan="2"> Shannon </td>
# </tr>
# <tr>
# <td> Phone: 202-555-1234 </td>
# <td> Twitter: @svt827 </td>
# <td> Github: @shannonturner </td>
# </tr>
# </table>

# ...

print "Goal #2 Output:"

for each in contacts:
	print """<table border="1">
<tr>
<td colspan="2"> {0} </td>
</tr>
<tr>
<td> Phone: {1} </td>
<td> Twitter: {2} </td>
<td> Github: {3} </td>
</tr>
</table>""".format(each, contacts[each]['phone'], contacts[each]['twitter'],contacts[each]['github'])

# Goal 3: Write all of the HTML out to a file called contacts.html and open it in your browser.

# Goal 4: Instead of reading in the contacts from the dictionary above, read them in from contacts.csv, which you can find in lesson_07_(files).

print "Goal #4 Output:"

#file must be saved in same folder for relative path to work
with open("Playtime_lesson03_contacts.csv", "r") as contacts_file:
	contacts=contacts_file.read()

rows=contacts.split("\r")
row_list=[]

for row in rows:
	row_clean=row[1:-1]
	row_list.append(row_clean.split(","))

# remove row of column headers
row_list=row_list[1:]

for each in row_list:
	print """{0}'s contact information is:
	Phone: {1}
	Twitter: {2}
	Github: {3}""".format(each[0], each[1], each[2], each[3])
