from sys import exit

def spielburg_entrance():
    print ("You see the entrace to the town of Spielburg.\n"
"You see an open gate, a man standing by the entrance and all the signs of"
" fall. What do you want to do?")

    input = raw_input("> ")
    if "talk" and "man" in input:
        bruno()
    elif "enter" in input or "walk" in input:
        spielburg()
    elif "quit" in input:
        exit(0)
    else:
        noentiendo("Maybe try talking to the man or walking around.")
        spielburg_entrance()

def noentiendo(why):
    print "I don't understand what you're trying to do there.", why

def bruno():
    print "The shifty looking man eyes you up and down.\n'What is your\
 business here?'"

    input = raw_input("> ")
    if "ask" in input:
        print "This is Spielburg, and I'm Bruno."
        bruno()
    elif "walk" in input:
        spielburg()
    elif "leave" in input:
        spielburg()
    elif "quit" in input:
        exit(0)
    else:
        noentiendo("Maybe try asking him something, or just leave him alone.")
        bruno()

def spielburg():
    print "You enter Spielburg and look around.\nYou see a man that appears to\
 be a Sheriff and a large looking goon."

    input = raw_input("> ")
    if "talk" in input:
        print "The goon doesn't move an inch, but the Sheriff is quick to\
 respond.\n'Hi, welcome to Spielburg. I'm the Sheriff around here, and\
 this is my assistant, Otto. The storm blocked us off from the rest of\
 the valley, but there's still a lot to see and do here. Enjoy your\
 stay while in Spielburg, and stay out of trouble!'"
        spielburg()
    elif "walk" in input or "leave" in input:
        spielburg_entrance()
    elif "quit" in input:
        exit(0)
    else:
        noentiendo("Maybe try talking or walking around.")
        spielburg()

spielburg_entrance()
