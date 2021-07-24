# Milestone Project 3 - Battleship in Python
![Start page](https://github.com/renatalantos/Battleship-in-Python/blob/main/documents/screenshots/Screenshot%20start%20page%20Idle.JPG)
![Game over](https://github.com/renatalantos/Battleship-in-Python/blob/main/documents/screenshots/game%20over%20Idle.JPG)

## Table of Contents

* Introduction
* UX
 
  * Owner Goals
  * User Goals

* Layout
 
  
 * Features

* Structure
  * FLowchart
  * General logic
  * Discrepancies with original ideas
  

* Technologies

* Testing

* Bugs, Issues

* Deployment

* Acknowledgements

# Introduction
The product (Battleship game in Python) is a logic game based on the well known boardgame, where two players play against each other. Each player has two grids, one with different sizes of battleships on it, and the other oneis to mark off the guesses they made about the other players battleships. Battleships are represented by intersections of rows and columns. They can be only vertical or horizontal, not diagonal. Ships can touch each other, though. 

The players are not allowed to see the other player's grids. 

The players take turns making guesses by calling out row and column intersections. If a player calls out a row and column intersection with no battleship, he crosses it off with an X and the other player does it, too on their own grid. Hits are marked differently. The player, who guesses all the other player's battleship first, wins the game.

In this project the user plays against the computer. The computer generates a random row and column number, and the intersection represents a ship. 

This game has multiple one-sized ships. The ships can be next to each other, though. It is more for the showcasing of programming logic, putting together code components and user input validation. In future, I would like to implement more ships of different sizes in the game, to make it more challenging and enjoyable for users andto improve my Python skills.


# UX

* Owner goals

The owners of the product is the programmer who would like to showcase her skills for users, fellow programmers and prospective employers. 


* User goals

Potential users would like to achieve the following:

* Play a logic based game
* Play the game on different difficuly levels
* Be instructed about the rules
* Be instructed about various steps
* Be informed about their progress
* Restart the game

The game uses a very basic logic of elimination: once you guessed something and it was wrong, you shouldn't guess that again but move onto a next guess. However, as it is possible that the program generates identical random numbers, this is not always achieved. Users are informed about this in the inital welcome message. The welcome messages describes the general flow of the game.

Users are instructed before and after each steps about what to do next. They are also informed about when the game ends. They are also informed about when they enter wrong input and they are prompted to try again. These are achieved by messages in the command line. 

Users are also provided feedback about whether their guess was correct or incorrect, how many ships are remaining and the number of guesses remaining. These are also achived by messages in the command line.

Different diffuculty levels are achieved by the different grid sizes.
Possible grid sizes are 4 x 4, 6 x 6, 8 x 8, 10 x 10. They can be set by the initial user input.

Restarting the game can be achieved if user clicks on the Restart Program button.


# Layout

My battleship is a very simple console based game. Only the mere instructions, user feedbacks and the grid at the different stages of the game is displayed.

[Battleship running in Heroku](https://github.com/renatalantos/Battleship-in-Python/blob/main/documents/screenshots/user_loses.JPG)
[Battleship running in IDLE](https://github.com/renatalantos/Battleship-in-Python/blob/main/documents/screenshots/run_in_pyhton_idle.JPG) 



# Features
The game includes the following features:

* Welcome graphics
* Welcome message
* Instructions for user
* Feedback messages to user
* Grid in various sizes
* Grid elements O, X, H
* Game over message


The original grid is composed of O characters,
which are updated either to X or H, depending on whether user hit or missed.
* Updated messages to inform user where they are in the game.

### Instructions for user
The user instructions prompt user to provide input within various critera. The input expected is numbers thoughout the whole programme. The numbers are entered as strings and validated inside try statements of while loops as integers. Depending whether I expect certain numbers or numbers within a range, I validate the numbers with raising and excepting ValueError or IndexError. Also, I made sure that input cannot be non-alphanumerical character.   
 

Error message for user [Error message for non-alphanumerical input](https://github.com/renatalantos/Battleship-in-Python/blob/main/documents/screenshots/error_message_non_alphanumerical.JPG) 

### Feedback messages for user

The feedback messages are displayed after validation, let validation be successful or not. They reconfirm what input is wanted or whether input has been accepted.

Error message for user [Error message for input out of range](https://github.com/renatalantos/Battleship-in-Python/blob/main/documents/screenshots/error_message_not_in_range.JPG)

Confirmation for user [Ok to play](https://github.com/renatalantos/Battleship-in-Python/blob/main/documents/screenshots/ok%20to%20play.JPG)

### Grid in various sizes

The grid can be set to sizes 4 x 4, 6 x 6, 8 x 8 and 10 x 10. To do that, I take and validate user input with the board_size variable. To do that, I use the def validate_board_size(board_size) function and a while loop in the main body of the code. The loop runs until user input is validated and then builds the board. This is done by the build_board(board_size) and print_board(board) functions.

### Grid elements O, X, H

These are the elements of the grid. The grid is first displayed as a number of lists of O characters, which have been stripped of ' 's and []s by *b in the print_board(board) function.

The while loop inside the make_guesses() function runs the validated user input for guess rows and guess columns (By while loop in the make_guesses() function). The first if statment inside the while loop checks whether the guess row and guess column provided by the user is identical with the random ship row and ship column numbers generated earlier by the def random_row(board) and def random(col) functions. If so, the intersection of the identical rows and columns updates to H on the board and the game ends with the user's win.

If after checking the first if statement the programme will proceed to the else statement if the above condition wasn't met. The the next possibility is that the user already guessed the row and column and was not successful. This is mapped out in the first if statement inside the else. If the previous guess row and column, which are represented as indices updated board[] list have already been guessed, the board element O was updated to X. If guess row and guess column intersection equal to this, then that intersection was already guessed.

The second else inside the else will do the final check, with the only remaining possibility that the intersection of guess row and guess column is an X. If the remaining guesses run out (they are set in the while loop and decrement with only incorrect guess) and their number is 0, the user loses and the game ends.

### Updated messages to inform user where they are in the game

Updating user is achieved by informing them about the remaining number of guesses and ships, which are decremented with every incorrect guess. 
The message with the number of remaining guess will display every time user enters validated input. Guesses that have already been made are not penalized.


## Future features

Also, I would like to add more ships with different sizes.

I would also like to add a restart game option.



# Structure

As this game has more of a logical structure than anything else, I think displaying the flowchart is sufficient here. This maps out the basic logic of the game.

1. User is prompted to enter input.
1. Input is validated.
2. It is either valid or not.
3. If it is valid, user can start playing.
4. If it invalid, user is prompted for input again until correct input is entered.
5. User enters another input.
6. It is either valid or not.
7. If it is invalid, user is prompted for input again until correct input is entered. (step 6)
8. If it is valid, user either hits or misses.
9. If input is not valid, user is prmpted again. (step 6)
9. If user hits and this is the last remaining ship, user wins.
10. If user hits and this is not the last remaining ship user is prompted to play on.
12. If user misses and there are ships left, user is prompted to guess again. 
13. If this is the last hit and user runs out of guesses, user loses and the game is over.

## Flowchart

[Flowchart](https://github.com/renatalantos/Battleship-in-Python/blob/main/documents/screenshots/Battleship%20Flowchart.pdf)

## Discrepancies with original ideas


* I meant to implement ships of different sizes, number of ships would have been half of the board_size variable. Sizes would have been 1 to 5. Unfortunately, i only have ships of size of 1 x 1. 

* My make_guesses() function is quite big as I use both a while and a for loop inside it. I meant to use small and neat functions but unfortunatley my validation only works this way. It is one of my goals to perfect my function skills.

* There is a while loop in the main body of the function, which was meant to be in a function, instead it calls two other functions.



  

# Technologies

### The following technologies and platforms were used to create the site:

* **Python** for structure, text, grid display and grid updates

* **Gitpod** to create files and assets

* **Github** to store created files and assets

* **Idle** for testing and screenshots

* **Heroku** for site deployment and to store created files

* **Lucidchart** for flowchart


# Testing 

 ## Validation 

  The run.py file passed the PEP8 validator with 5 warning messages about trailing white spaces. (I could not delete these) Previously the errors mostly related to the length of the lines which I resolved by using \ Also common errors and warnings were too many blank lines and indentation. However, in GitPod and Heroku, this adds extra empty spaces within the lines, whereas in Idle there is no difference to the format. I resolved this creating shorter senetnces for user prompts.
  Editor: Rulers in GitPod settings to check line length.

  [Display line in Python after using \ to shorten row](https://github.com/renatalantos/Battleship-in-Python/blob/main/documents/screenshots/guessed_already.JPG)

  [Display line in Idle after using \ to shorten row](https://github.com/renatalantos/Battleship-in-Python/blob/main/documents/screenshots/run_in_pyhton_idle.JPG)



  I used Idle as well, but as its error messages are not detailed when it comes to syntax errors, I mainly used GitPod. I ran python3 in the command line and checked the error messages. I found GitPod good for highlighting errors in the code.



  [PEP8 Warning messages after first validation](https://github.com/renatalantos/Battleship-in-Python/blob/main/documents/screenshots/PEP8%20screenshot%20after%20first%20validation.JPG)




  [PEP8 Warning messages after second validation](https://github.com/renatalantos/Battleship-in-Python/blob/main/documents/screenshots/PEP8%20screenshot%20after%20second%20validation.JPG)


  [PEP8 Warning messages after third validation](https://github.com/renatalantos/Battleship-in-Python/blob/main/documents/screenshots/PEP8%20screenshot%20after%20third%20validation.JPG)

  
  [PEP8 Warning messages after fourth validation](https://github.com/renatalantos/Battleship-in-Python/blob/main/documents/screenshots/PEP8%20screenshot%20after%20fourth%20validation.JPG)

  [PEP8 Warning messages after fourth validation](https://github.com/renatalantos/Battleship-in-Python/blob/main/documents/screenshots/PEP8%20screenshot%20after%20fifth%20validation.JPG)



## Bugs, Issues

* There is a while loop in the main body of the function, which was meant to be in a function, instead it calls two other functions.
My make_guesses() function is quite big as I use both a while and a for loop inside it. I meant to use small and neat functions but my validation only works this way.


* As the code is quite simple, my main issue was with validating user input. 
It took my a while to understand what try, raise ValueError, except ValueError does. Setting up conditions for valuerrors meant battling with syntax and logical errors as well. I raise both ValueErrors and IndexErrors in the code for two separate inputs, too. Catching them inside one block and putting this code inside my while loop in the making_guesses() function was the hardest part of my project I think. It still doesn't work 100% efficiently, unfortunately.
You probably notice that I use fairly generic error messages when I validate user input for guess row and guess column. The reason for that is that I tried to return the actual input in a print statement, in the block of code on lines 163 and 175 the first if statement's ValueError message showed in the second one and it is the same between if statements on line 153 and 163 - first one showed in the second.

Inside the same code, starting on the if statements, there is a GitPod error message shown: Unreachable code. However, this didn't show in PEP8 and the code worked.

I resolved this by taking out the if statements from the from the ValueErrors.

[Unreachable code](https://github.com/renatalantos/Battleship-in-Python/blob/main/documents/screenshots/unreachable%20code.JPG)



* As I have multiple 1 x 1 ships and I get their coordinates by generating random in numbers in the range of 1 and the board size, it is possible that sometimes two identical numbers for rows and columns are generated. I tried to write code to catch this when it happens so that I can inform the user by decrementing the number of ships so that user is not mislead into thinking that they got all ships wnen there are duplicates. I probably got off the wrong track altogether as my point was the the ships_to_hit list, to which the randomly gnerated row and column numbers (for ship) are added, has indexes from pairs of these numbers. For example ship_to_hit[1] could be [2,3], 2 for row and 3 for column. It is possible so that ship_to_hit looks like this: ship_to_hit[[2,3], [2,3]]
I tried to use a for loop to iterate throgh the indices of ships_to_hit and eliminate duplicates or to restart by putting the function inside itself, inside an if statement, however this didn't work. The former ended in the error message: unhashable type list and the letter in a RecursionError.

To at least inform the user of the possibility of duplicate ships, I explain this in the Welcome message.

[Error: Unhashable Type List](https://github.com/renatalantos/Battleship-in-Python/blob/main/documents/screenshots/Error%20unhashable%20type%20list.JPG)
[Error: RecursionError](https://github.com/renatalantos/Battleship-in-Python/blob/main/documents/screenshots/recalc.JPG)
 


# Deployment

The site was deployed to Heroku. The steps to deploy are as follows:
As I didn't add any dependencies, I didn't need to update the requirements.txt file and didn't need to add a Configvar in Heroku.

1. In the GitPod Workspace I made sure that everything is saved.
2. In the Terminal window I added all my files by using git add . .
3. In the Terminal window I queued my files using git commit -m "Meaningful, descriptive note"
4. I used git push to push my files into GitHub.
5. I created a Heroku account on the Heroku.com site. 
6. In Heroku, I clicked on Create a New App option.
7. I named my app and typed it in lowercase, separating the words with dashes (-). I made sure that it is not taken by someone else and is unique. I entered the region and ignored the Add to pipeline option.
8. I clicked on Create App.
9. On the next page, from the Settings section in the toolbar, I clicked on Add buildpacks on the right to add further dependencies.
10. From Buildpack, I selected python first and clicked on Add.
11. I clicked on Add buildpacks again and selected nodejs and clicked on Add.
12. I made sure that python is displayed on top and nodejs underneath and not the other way around.
13. Next I selected the Deploy section from the toolbar.
14. From the options, which application to connect to, I selected GitHub. Other options were Heroku Git and Container Registry.
15. Next I clicked on Connect to GithHub. This prompted me to search for a Repository Name in GitHub.
16. I selected my current project, Battleship-in-Python.
17. When it was found, I clicked on Connect.
18. I scrolled down the page and saw two options: Enable Automatic Deploys and Deploy Branch. 
19. First I selected Enable Automatic Deploys so that my GitHub changes are transferred to Heroku. I knew this worked because the button faded out and displayed 'Disable Automatic Deploys'
20. Next I clicked on Deploy Branch to initialize deployment.
21. The app was being built by installing the necessary files and dependencies. 
22. Finally, a message was displayed: 'Your app was successfully deployed.'
23. I clicked on View underneath the message.
24. This brought up the console in Heroku and my code was running straight away without my prompting it to do so.
25. My program was running fine, handling valid and invalid user inpt.
26. I restarted it by clicking on Run Program.
27. It was working as expected, handling valid and invalid user inpt.
28. My live site was deployed a few minutes later under [Heroku link:](https://battleship-in-python.herokuapp.com/)

Also, the link to my GitHub repository is [GitHub link](https://github.com/renatalantos/Battleship-in-Python) 




# Acknowledgements 

I used various resources to create the program.

## Code

For the original flowchart, I used the following chart: [Original Flowchart](https://github.com/farhathfaisal/battleship) . However, I later recreated it by my own logic.

I used this site to get the idea how to print the board:
[Board printing](https://bigmonty12.github.io/battleship)

To make sure I know how battleship is played I used the following video: [Battleship video idea](https://www.youtube.com/watch?v=hkKw-7aOjj8)

I used this codecademy video to build up the basic sructure: [Codecamedy video for design](
https://www.youtube.com/watch?v=7Ki_2gr0rsE&t=300s
)

I got the idea how to decrement guesses from this video:
[Hangman video](https://www.youtube.com/watch?v=m4nEnsavl6w) 
Before, I used a for loop i to decrement them but they guesses decremented at every step, so I didn't go with it.

This StackOverFlow thread helped me resolve my validation issues:
[StackOverFlow: Validation Explined](https://stackoverflow.com/questions/23294658/asking-the-user-for-input-until-they-give-a-valid-response)

For validation, I also looked up the Love Sandwiches walkthrough project by CI.

This StackOverFlow thread helped me shorten my lines for PEP8 validation:
[StackOverFlow: Line Too Long](https://stackoverflow.com/questions/53162/how-can-i-do-a-line-break-line-continuation)

I looked up this site when I had trouble decrementing my ship numbers
[Decrement ship numbers](https://discuss.codecademy.com/t/excellent-battleship-game-written-in-python/430605)

For the graphics I used the following site: 
[Graphics](http://patorjk.com/software/taag/#p=display&h=0&v=3&f=Slide&t=Battleship%0A graphics)
Copyright info is Slide.flf (C) 1994 by Victor Parada (vparada@inf.utfsm.cl) 94/08/18.




# Special Acknowledgements

* To Kasia for all her help and hard work.
* To my classmates who helped and advised.
* To my mentor Seun for her guidance.

And last but not least my family for putting up with me when I'm Out of Order and my cat for forgiving me for forgetting to feed her while I'm coding.
Thanks!!!

Thanks for reading.































  










    
  




































  










    
  






