# Math Quiz
Math quiz is a Python terminal game that runs in the Code Institute mock terminal on Heroku.

Basic mathematical quiz for kids and adults. 
It generates 10 random questions choosing from subtraction, addition, multiplication, and division.

Live link can be found [here](https://math-quiz-01.herokuapp.com/).

![Math quiz](/images/start.png)

## How to play

- To start the game the user needs to enter a player's name first.
- The player can choose to start the game from the menu or to look at the instructions.
- The game encourages you not to use any help to answer the questions.
- It generates 10 random questions choosing from subtraction, addition, multiplication, and division.
- After answering the game immediately shows if it was the right answer or not.
- After 10 questions the player gets a score, which is uploaded to a google sheet with the player's name and the exact time.

## User Experience 

### Features

- Name:
    - To start the game the program asks to enter a name first. There are no criteria other than to have it longer than 0 characters. 
![Main](/images/main.png)
- Menu:
    - The menu features 3 options. The player can press 1 to start the game, 2 for detailed instructions, or 3 to exit the program.
![Menu](/images/menu.png)
- Instructions:
    - Here the player can read about how to play the game and explains when the answer is not a whole number round up to 1 or 2 decimal places to get the correct answer.
![Instructions](/images/instructions.png)
- Scoreboard:
    - A google sheet is connected to the program that is uploading the score, the name, and the time when a user plays the game.
![Scoreboard](/images/scoreboard.png)

### Flowchart
I planned this project with [Lucidchart](https://www.lucidchart.com/pages/landing?utm_source=google&utm_medium=cpc&utm_campaign=_chart_en_tier1_mixed_search_brand_exact_&km_CPC_CampaignId=1490375427&km_CPC_AdGroupID=55688909257&km_CPC_Keyword=lucidchart&km_CPC_MatchType=e&km_CPC_ExtensionID=&km_CPC_Network=g&km_CPC_AdPosition=&km_CPC_Creative=442433236001&km_CPC_TargetID=aud-536921399221:kwd-33511936169&km_CPC_Country=1012365&km_CPC_Device=c&km_CPC_placement=&km_CPC_target=&gclid=CjwKCAjwlcaRBhBYEiwAK341jSFJzdwzxx-iASjR7J-Oo4KF5e2_4qGIa9Tk8RAMC1O22-GZeOswzRoCT8UQAvD_BwE).

![Lucidchart](/images/math_quiz_lucidchart.png)

## Testing

- Tested manually for invalid inputs and error messages.

![Error message](/images/error_message_1.png)
- Tested in my local terminal and Heroku terminal.
- Tested on phone and desktop.
- The code had no problem passing through the [PEP8 validator](http://pep8online.com).
![PEP8](/images/pep8.png)

## Bugs

There are no bugs present in the deployed program.
The only issue is on the phone screen the pyfiglet title is not fully visible. As of now, I am not sure if that is a fixable problem.


### Fixed bugs

- There were some issues with the player's name on the google sheet. My mentor helped me to make a global player name that is updated every time the player gives a new name.

- I wanted to have a division operator for the quiz which is not returning difficult numbers. This was also fixed with my mentor. We used float() on the evaluated numbers and round() so the whole numbers don't need .00.

## Deployment

This project was deployed using Code Institute's mock terminal for Heroku.

    -Steps for deployment:
        - Login on the Heroku website
        - Click on New, then Create new app
        - In the Settings, set two Config Vars, first add the CREDS.json file, second is to set the PORT to 8000
        - Set the buildpacks to Python and NodeJS in that order
        - In the Deploy tab connect your Github
        - Scroll to Manual deploy and click on Deploy Branch


## Language
This game was made with python as a primary language.

## Technologies and Libraries

* [Google sheet]()
* [Gspread](https://pypi.org/project/gspread/)
* [Pyfiglet](https://pypi.org/project/pyfiglet/0.7/)
* [Termcolor](https://pypi.org/project/termcolor/)
* [Gitpod](https://gitpod.io/projects)
* Paint


## Credits and acknowledgments

- [Love sandwiches project](https://github.com/Code-Institute-Solutions/love-sandwiches-p5-sourcecode/tree/master/05-deployment/01-deployment-part-1)
- To color pyfiglet [Tic Le Polard](http://tic-le-polard.blogspot.com/2015/04/python-colored-ascii-art-with-pyfiglet.html)
- Video from Youtube for a basic quiz [HowToFAQ](https://www.youtube.com/watch?v=h4n_ByFuD90)
- [Stack Owerflow](https://stackoverflow.com/)
- [Slack](https://slack.com/)
- [Computing Learner](https://computinglearner.com/how-to-create-a-menu-for-a-python-console-application/)
- Code Institute for the deployment terminal
- My mentor for reviewing and helping with the code

