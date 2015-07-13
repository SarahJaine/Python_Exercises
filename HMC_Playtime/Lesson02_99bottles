### Goal: Make Python print out the song for 99 bottles of beer on the wall.

beer=99

while beer>0:
    if beer > 2:
        print """{0} bottles of beer on the wall, {0} bottles of beer...
        Take one down and pass it around, {1} bottles of beer on the wall.""".format(beer,beer-1)
        beer = beer - 1
    elif beer == 2:
        print """{0} bottles of beer on the wall, {0} bottles of beer...
        Take one down and pass it around, {1} bottle of beer on the wall.""".format(beer,beer-1)
        beer = beer - 1
    elif beer == 1:
        print """{0} bottle of beer on the wall, {0} bottle of beer...
        Take it down and pass it around, no more bottles of beer on the wall.""".format(beer,beer-1)
        print """No more bottles of beer on the wall, no more bottles of beer.
        Go to the store and buy some more, 99 bottles of beer on the wall."""
        break
