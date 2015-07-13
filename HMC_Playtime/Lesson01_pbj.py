#### Peanut Butter Jelly Time!

print "Oh, would you look at that?  It's Peanut Butter Jelly Time!\nLet's look in the kitchen and see what we have..."
try:
        bread=int(raw_input("How many slices of bread do we have? "))
        pb=int(raw_input("How many ounces of peanut butter do we have? "))
        jelly=int(raw_input("How many ounces of jelly do we have? "))


        # First Goal: Create a program that can tell you whether or not you can make a peanut butter and jelly sandwich

        print "\nFor First Goal: Create a program that can tell you whether or not you can make a peanut butter and jelly sandwich..."

        if bread >= 2 and pb >= 1 and jelly >=1:
                print "We can make a PB&J sandwich."
        else:
                print "Sorry, no PB&J today."

        # Second Goal: Modify that program to tell you: if you can make a sandwich, how many you can make

        print "\nFor Second Goal: Modify that program to tell you: if you can make a sandwich, how many you can make..."

        if bread >= 2 and pb >= 1 and jelly >=1:
                bread_sandwiches = bread / 2
                sandwiches = min(bread_sandwiches,jelly,pb)
                if sandwiches > 1:
                        ending = "es."
                else:
                        ending ="."
                print "We can make {0} PB&J sandwich{1}".format(sandwiches,ending)
        else:
                print "Sorry, no PB&J today."


        # Third Goal: Modify that program to allow you to make open-face sandwiches if you have an odd number of slices of bread ( )

        print "\nFor Third Goal: Modify that program to allow you to make open-face sandwiches if you have an odd number of slices of bread..."

        def ending(x):
                if x > 1 or x == 0:
                        return "es"
                else:
                        return ""
        if pb >= 1 and jelly >=1:
                if bread >= 2:
                        bread_sandwiches = bread / 2
                        sandwiches = min(bread_sandwiches,jelly,pb)
                        print "We can make:\n\t{0} PB&J sandwich{1}".format(sandwiches,ending(sandwiches))
                        if bread%2 > 0 and bread_sandwiches < pb and bread_sandwiches < jelly: #I've never heard of an open face pb&j but let's just go with it
                                print "\tWe can also make 1 open-faced PB&J"
                elif bread == 1:
                        print "We can only make 1 open-faced PB&J."
                else:
                        print "Sorry, no PB&J today."
                        
        else:
                print "Sorry, no PB&J today."

        # Fourth Goal: Modify that program to tell you: if you're missing ingredients, which ones you need to be able to make your sandwiches

        print "\nFor Fourth Goal: Modify that program to tell you: if you're missing ingredients, which ones you need to be able to make your sandwiches..."

        shopping_list=[]

        if jelly == 0:
                shopping_list.append("jelly")
        if pb == 0:
                shopping_list.append("peanut butter")
        if bread < 2:
                shopping_list.append("bread")
        if len(shopping_list) > 0:
                print "It looks like we have some grocery shopping to do.  Here's our shopping list:"
                for each in shopping_list:
                        print "\t",each
        else:
                print "We have all the ingedients we need for Peanut Butter Jelly Time!"



        # Fifth Goal: Modify that program to tell you: if you have enough bread and peanut butter but no jelly, that you can make a peanut butter sandwich but you should take a hard, honest look at your life. Wow, your program is kinda judgy.

        print "\nFor Fifth Goal: Modify that program to tell you: if you have enough bread and peanut butter but no jelly, that you can make a peanut butter sandwich..."


        sandwiches=0
        bread_dual= bread/2

        if bread>0 and pb >0:
                print "We can make:"
                while bread >=2 and pb>=1 and jelly>=1:
                        sandwiches = sandwiches + 1
                        bread_dual = bread_dual - 1
                        bread = bread - 2
                        pb = pb - 1
                        jelly = jelly -1
                if sandwiches > 0:
                        print "\t{0} PB&J sandwich{1}".format(sandwiches,ending(sandwiches))
                if pb > 0: #Unlike goal #4, I'm not giving the option to make open pb&j's, just open pb sandwiches
                        if bread_dual > 0: #if we have 2+ bread, then make some pb sandwiches
                                pb_sandwiches = min(bread_dual,pb)
                                print "\t{0} peanut butter sandwich{1}".format(pb_sandwiches,ending(pb_sandwiches))
                                pb = pb - pb_sandwiches
                                bread = bread - (pb_sandwiches*2)
                        if bread > 0: #if we have any bread leftover, then make some open-face pb sandwiches
                                open_pb_sandwiches = min(bread,pb)
                                print "\t{0} open-faced peanut butter sandwich{1}".format(open_pb_sandwiches,ending(open_pb_sandwiches))
                                bread = bread - open_pb_sandwiches
                                pb = pb - open_pb_sandwiches
        else:
                print "Sorry, no sandwiches today."

except ValueError:
        print "It looks like you didn't enter a number. Please run the program again and use only integers."
        pass
        

