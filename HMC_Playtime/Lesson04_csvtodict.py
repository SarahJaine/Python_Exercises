# Challenge Level: Advanced

# Scenario: Your organization has put on three events and you have a CSV with details about those events
#           You have the event's date, a brief description, its location, how many attended, how much it cost, and some brief notes
#           File: https://github.com/shannonturner/python-lessons/blob/master/section_09_(functions)/events.csv

# Goal: Read this CSV into a dictionary.

# Your function should return a dictionary that looks something like this. 
# Bear in mind dictionaries have no order, so yours might look a little different!
# Note that I 'faked' the order of my dictionary by using the row numbers as my keys.

# {0: 
#     {'attendees': '12', 
#     'description': 'Film Screening', 
#     'notes': 'Panel afterwards', 
#     'cost': '$10 suggested', 
#     'location': 'In-office', 
#     'date': '1/11/2014'}, 

# 1: 
#     {'attendees': '12', 
#     'description': 'Happy Hour', 
#     'notes': 'Too loud', 
#     'cost': '0', 
#     'location': 'That bar with the drinks', 
#     'date': '2/22/2014'}, 
# 2: 
#     {'attendees': '200', 
#     'description': 'Panel Discussion', 
#     'notes': 'Full capacity and 30 on waitlist', 
#     'cost': '0', 
#     'location': 'Partner Organization', 
#     'date': '3/31/2014'}
# }

#relative path will only work if file is saved in same folder
with open('Playtime_lesson04_group_csvtodict.csv') as events_file:
	events=events_file.read()

rows=events.split("\r")
row_list=[]

#removing extra ""
for row in rows:
	row_clean=row[1:-1]
	row_list.append(row_clean.split(","))

row_header=row_list[:1]
row_data=row_list[1:]
events_dict={}
index=0

for each in range(0,len(row_data)):
	events_dict.update({each:{
		row_header[0][0]:row_data[index][0],
		row_header[0][1]:row_data[index][1],
		row_header[0][2]:row_data[index][2],
		row_header[0][3]:row_data[index][3],
		row_header[0][4]:row_data[index][4],
		row_header[0][5]:row_data[index][5],
 		}})
	index=index+1

for each in events_dict:
	print each,": \t",events_dict[each],"\n"
