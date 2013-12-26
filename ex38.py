#this line defines 6 of 10 things
ten_things = "Apples Oranges Crows Telephone Light Sugar"
#print that theres only 6 of 10 things
print "Wait there's not 10 things in that list, let's fix that."
#define stuff as a variable 
stuff = ten_things.split(' ')
#define more stuff as a variable list with 8 more items
more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl",\
 "Boy"]
#create while loop that runs until 10 items are in the stuff variable
while len(stuff) != 10:
#defines next one as more stuff+1
    next_one = more_stuff.pop()
#display next item being added
    print "Adding: ", next_one
#appends the next list item to the stuff variable
    stuff.append(next_one)
#prints how many items are currently in the len(stuff) variable
    print "There's %d items now." % len(stuff)
#prints the result of the while loop after the 10 condition has been met
print "There we go: ", stuff

print "Let's do some things with stuff."
#prints oranges, because 0 would be apples
print stuff[1]
#prints corn because that would be 1 less than 0 so it goes to the end of list
print stuff[-1] #whoa! fancy
# list.pop removes items from a list, with none defined this removed the last
# item which is corn and displays it
print stuff.pop()
#prints the entire list now, without corn because the last command removed it
#with a space in betweeen each item, joining them
print ' '.join(stuff) # what? cool!
#prints item 3 and item 4, with a pound sign separating each item 
print '#'.join(stuff[3:5]) # super stellar!
