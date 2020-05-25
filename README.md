
# SPEEDERIOS TYPERINOS
#### By: Claudia Koh 1004679 F08

### What is it? 
It is a game that challenges your typing speed. Type as manycharacters as you can in the time limit of 60 seconds. 


Before the game starts, you can select how hard the game is for you. 
Customise the number of lifelines you get (minimum 1-9 maximum)
In addition, there are multiple level of difficulties in this game (easy, medium, difficult). That determines how difficult the words are. Easy is as easy as 123, but hard can be really difficult with the longest word in the English Dictionary!!


RULES: 
1. you are not allowed to use backspace. 
2. Type the word you see on the screen into the text box, followed by pressing ENTER to confirm your input.



Your mission is to type more characters than the average person, within 60 seconds.
> Easy level: type more than 80 characters

> Medium level: 100 characters

> Hard level: 130 characters.


Good luck! Have fun!
Images sourced from Minecraft & Google!

### How to play your game: 
Choose the number of lifelines you have and select the difficulty level. 
Select confirm when you are done!
Start the game by DOUBLE clicking the textbox that says 'type here'.
The time starts now!! You have 60 seconds to type as many characters as you can.

### Describe your code:
Mainly built on Kivy Library with use of State Machines


Comprises of: 
#### global variables:
1. easy_dic 
    - a list of words that will be randomized on the  difficulty level (easy)
2. medium_dic 
    - a list of words that will be randomized on the  difficulty level (medium), which includes those words in easy_dic as well
3. hard_dic 
    - a list of words that will be randomized on the  difficulty level (hard), exclusive of medium and easy words
4. life
    - dictionary with key is 'hearts', value is the number of lifelines player gets
    - default value is set at 3
5. difficulty 
    - dictionary with keys as numbers (0,1,2) that correspond to respective names of difficulty levels (easy, medium, hard) as values 
    - additional key is 'choice' , with the value of the respective difficulty chosen by player
6. dictionaries 
    - dictionary with keys of name of difficulty levels (easy, medium, hard), corresponding to their respective dictionaries 
7. sm
    - this sm indicates screen manager, which is set to be a global variable 
    - allows for the screen to access and change widgets of other screens
    
    
#### Classes (excluding screens): 
1. Custom SM class 
    - mostly similar to the SM class we used in class 
    - difference is in the step function 
        - step function takes in an additional argument (disp), which is the displayed word on the screen 
        - allows for disp to be input into get_next_values of SM
2. Typing_sm 
    - parent class is self-define SM class 
    - start state is 'norm' 
    - if user typed the correct word, state remains as 'norm 
    - if user typed wrongly, state changes to 'wrong' 
3. menuButtons
    - parent class is kivy Button 
    - sets the common font size and background of the buttons ('start' and 'quit') in MenuScreen 
4. HeartButtons 
    - parent class is kivy Button 
    - sets the size and heart background of the button in the GameScreen 
    - displays existing lifelines in graphic form 
5. MyInput 
    - parent class is kivy TextInput 
    - sets the size, font size and multiline of text input where users type in GameScreen 
6. CountDown 
    - parent class is label 
    - Property of the time limit before game ends (60 seconds)  
    - functions: 
        - start: starts the animation of the countdown from 60 s to 1s 
        - final_win: change of screen from GameScreen to SuccessScreen
        - final_fail: change of screen from GameScreen to FailureScreen 
        - finish: checks whether player wins or loses the game and calls the corresponding function(final_win/final_fail)
        - on_time: changes the property of CountDown, such that textof the label changes every 0.1 seconds


#### Upon Initialization of the App (TypingGame):
1. 5 Screens are initialized: MenuScreen, LevelScreen, GamesScreen, SuccessScreen, FailureScreen
    - starting with the MenuScreen 
2. MenuScreen consists of 2 Buttons 
    - Start Button: starts the process, changes to LevelScreen 
    - Quit Button: Quits the app 
3. In the LevelScreen, player can choose their difficulty level and number of lifelines they get. 
    - using the '+' Button, lifelines they get will increase, updating the variable Life(dictionary)
    - using the '-' Button, lifelines they get will decrease, updating the variable Life(dictionary)
    - number of the lifelines is displayed in a label and when the player changes the number, the label is updated by the +/- Buttons
    - the +/- Buttons also update the number of lifelines in the GameScreen (which is initialized with the default number of 3)
    - using the '>' Button, the difficulty levels will increase, updating the variable difficulty['choices']
    - using the '<' Button, the difficulty levels will decrease, updating the variable difficulty['choices'] 
    - when clicking > past the hard level, the difficulty level will loop back to easy, vice versa
    <font_color=red>When player is done deciding, they click the confirm button, which updates the number of heart buttons (using a separate Floatlayout) and difficulty level in GameScreen, and changes the screen to GamesScreen </font_color=red>
4. GamesScreen: 
    - when it is initialized in step 1: 
        - the window is binded to the keyboard function(key_down), taking in the input arguments of every key pressed down
        - state machine Typing_sm is initialised and start (start_state = 'norm') 
    - player have to double tap the text input to start the countdown
        - default event on text input (on_double_tap) is binded to the start of the countdown 
    - player types the words into the text input
        - key_down function is triggered whenever player types anything, hence is used to initialise the dictionary of words of specified difficulty level
        - key_down function checks for input key 'ENTER', taking the user text input only after the ENTER key is pressed
        - state machine takes the user text input and checks if it is the same as the displayed word, getting the next state as a result 
        - if the word is correct, state remains as 'norm'
        - if the word is wrong, state changes to 'wrong' 
        - key_down function checks if there are still lifelines left
    - if player gets the word wrong and there are still lifelines left:
        - these are performed by the key_down function
        - state machine will return to 'norm' state
        - number of lifelines will deduct one and update the variable Life 
        - all the hearts displayed will be removed by removing layout containing it, and the new number of hearts will be added
    - if player gets the word wrong and there is no lifelines left: 
        - key_down function will change the screen to FailureScreen
    - if player runs out of time:
        - the function 'finish' within the Countdown class checks if the player achieved the number of characters required
        - if the player did not type enough characters, the screen changes to FailureScreen 
        - if the player typed enough characters, the screen changes to SuccessScreen
5. FailureScreen/SuccessScreen 
    - the format of both screen are the same 
        - Label with 'MISSION FAILED/SUCCESS'
        - Label that tells the player how many characters they typed 
        - Button to quit app
