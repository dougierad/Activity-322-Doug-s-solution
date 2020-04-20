"""
Doug's code, 13 Apr 2020

This program is intended as a tracer round for the flow of control as a user
of a social media account makes, deletes, and edits posts. For testing,
a user should be able to enter their user name, change which user name they
are currently using, add a post using their current user name, remove a post
made under their current user name, edit a post made under their current user 
name, print the contents of the list of posts, or quit the program.
"""

#This line of code tells the Python interpreter that it needs to reference the 
#post.py file in order to run the rest of the code in this file.
from CSE_322_post import Post

all_posts_archive = []
postEntry = ""

#Enter some initial posts
post1 = Post("Marie", "This is my first post!")
post2 = Post("Jimmy", "This is my Erste post!")
post3 = Post("Jacque", "This is my un post!")

all_posts_archive.append(post1)
all_posts_archive.append(post2)
all_posts_archive.append(post3)

print("Welcome to the SOCIAL MEDIA simulation!\n")
userName = input("What is your user name? ")
print ("Hello, " + userName, "!\n")

user_input = input(""" What would you like to do?
  "add"         - Add a post to the archive
  "remove"      - Remove a post from the archive
  "change user" - Change the user name associated with any future posts
  "print"       - Display the current up to date list of all posts
  "quit"        - End the program
? """)

#This while loop ensures that the program will continue executing statements
# at the next indentation level until the user types "quit" in response to the 
# prompt.
while user_input != "quit":
  
  if user_input == "print":
    print("\nHere are all the posts:")
    print("-----------------------")
    for item in all_posts_archive:
      print (item)
    print("")
    user_input = " "

  elif user_input == "change user":
    userName = input("\nWhat is the new user name? ")
    print ("Hello, " + userName+"!\n")

  elif user_input == "add":
    message = input("What would you like to say? ")
    postEntry = Post(userName, message)
    all_posts_archive.append(postEntry)
    print("\nYou just posted:")
    print("----------------")
    print(postEntry)

  elif user_input == "remove":
    item = int(input("Which post would you like to remove (first one is 0)? "))
    if (item < 0 or item > len(all_posts_archive)):
      print("Sorry, "+str(item)+" is not one of the posts.\n")
    else:
      print ("\nDELETING:")
      print("----------")
      print (all_posts_archive[item])
      sure = input ("ARE YOU SURE? (yes/no)")
      if sure == "yes":
        del all_posts_archive[item]
      else:
        print("Delete cancelled\n")
  else:
    print("\nNot a valid option.")

  #Code that will allow the user to make a new selection
  user_input = input("""\nWhat would you like to do?
  "add"         - Add a post to the archive
  "remove"      - Remove a post from the archive
  "change user" - Change the user name associated with any future posts
  "print"       - Display the current up to date list of all posts
  "quit"        - End the program
? """)
    #This code will finish the loop
print("\nGoodbye, "+userName+"!\n")