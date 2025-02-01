"""
This program is intended as a tracer round for the flow of control as 
a user of a social media account makes, deletes, and edits posts. For 
testing, a user should be able to enter their user name, change which 
user name they are currently using, add a post using their current user 
name, remove a post made under their current user name, edit a post 
made under their current user name, print the contents of the list of 
posts, or quit the program.
"""

# This line of code tells the Python interpreter that it needs to 
# reference the post.py file in order to run the rest of the code 
# in this file.
from Post import Post
#this imports the entire file
#from filename import class does specific classes

# How will you save the posts you will create? Review the for loop 
# near the end of this code for an answer.
all_posts_archive=[]    #all posts will be saved in this list
# What is the user name they want to use?

# Welcome user to the program 
print("Welcome to the Banana Grahams! ")
username=input("What is your username? ")
# Store initial user input in a variable identified by user_input
user_input = input(""" What would you like to do?
"add" - Add a post to the archive
"remove" - Remove a post from the archive
"change user" - Change the user name associated with any future posts
"print" - Display the current up to date list of all posts
"quit" - End the program

""")

# This while loop ensures that the program will continue executing 
# statements at the next indentation level until the user types "quit" 
# in response to the prompt.
while user_input != "quit":

    # code for adding a post here
    if (user_input == "add"):
        #to creat a post i need, username and message
        message=input("What is your message? ")
        #create the object of out post class
        theObjectPost = Post(username,message)
        all_posts_archive.append(theObjectPost)

    elif (user_input == "edit"):
        #figure out which post
        indexindex=input("What is that post id to edit? ")
        #ask for the new message
        theNewPostMessage=input("What is the new post")
        #reset that post item in the master list to the new message
        all_posts_archive[int(index)].set_message(theNewPostMessage)



    # code for removing a post here
    elif (user_input == "remove"):
        index=input("What is that post id to remove? ")
        del all_posts_archive[int(index)]

    # code for changing the current user here
    elif (user_input == "change user"):
        username=input("what is the new user? ")

    # code to display all posts, you can use the code in comments below
    elif (user_input == "print"):
        for Post in all_posts_archive:
            print (Post)
    
    # code to inform the user that their input was not valid here
    else:
        print("Invaid command.....")
    # code that will allow the user to make a new selection
    # This code will finish the loop
    user_input = input(""" What would you like to do?
    "add" - Add a post to the archive
    "edit" - Edit a post in the archive
    "remove" - Remove a post from the archive
    "change user" - Change the user name associated with any future posts
    "print" - Display the current up to date list of all posts
    "quit" - End the program

    """)