# Math Quiz
Math quiz is a Python terminal game which runs in the Code Institute mock terminal on Heroku.

Basic mathematical quiz for kids and adults. 
It generates 10 random questions choosing from subtraction, addition, multiplication and division.

Live link can be found here.

## How to play

- To start the game the user needs to enter a player name first.
- The player can choose to start te game from the menu, or to look at the instuctions.
- The game encurages you not to use any help to answer the questions.
- It generates 10 random questions choosing from subtraction, addition, multiplication and division.
- After answering the game immediately shows if it was the right answer or not.
- After 10 questions the player gets a score, that is uploading to a google sheet with the players name and the exact time.

## User Experience 

### Features

- Name:
    - To start the game the program ask to enter a name first. There is no criteria other than to have it longer than 0 character. 
- Menu:
    - The menu features 3 options. The player can press 1 to start the game, 2 for detailed instructions, or 3 to exit the program.
- Instructions:
    - Here the player can read about how to play the game and explains when the answer is not a whole number round up to 1 or 2 decimal places to get the correct answer.
- Scoreboard:
    - A google sheet is connected to the program that is uploading the score, the name, and the time when a user plays the game.

### Flowchart
I planned this project with [Lucidchart](https://www.lucidchart.com/pages/landing?utm_source=google&utm_medium=cpc&utm_campaign=_chart_en_tier1_mixed_search_brand_exact_&km_CPC_CampaignId=1490375427&km_CPC_AdGroupID=55688909257&km_CPC_Keyword=lucidchart&km_CPC_MatchType=e&km_CPC_ExtensionID=&km_CPC_Network=g&km_CPC_AdPosition=&km_CPC_Creative=442433236001&km_CPC_TargetID=aud-536921399221:kwd-33511936169&km_CPC_Country=1012365&km_CPC_Device=c&km_CPC_placement=&km_CPC_target=&gclid=CjwKCAjwlcaRBhBYEiwAK341jSFJzdwzxx-iASjR7J-Oo4KF5e2_4qGIa9Tk8RAMC1O22-GZeOswzRoCT8UQAvD_BwE).

![Lucidchart](/images/math_quiz_lucidchart.png)

## Testing

- Tested maually for invalid inputs and error messages.
- Tested in my local terminal and Heroku terminal.
- The code had no problem passing through the [PEP8 validator](http://pep8online.com/checkresult#).

![PEP8](/images/pep8.png)

## Bugs

There are no bugs present in the deployed program.


## Deployment

This project was deployed using Code Institute's mock terminal for Heroku.

    -Steps for deployment:
        - Fork or clone this repository
        - Create a new Heroku app
        - Set the buildbacks to Python and NodeJS in that order
        - Link the Heroku app to the repository
        - Click on Deploy


## Language
This game was made with python as a primary language.

## Technologies and Libraries

* [Google sheet]()
* [Gspread](https://pypi.org/project/gspread/)
* [Pyfiglet](https://pypi.org/project/pyfiglet/0.7/)
* [Termcolor](https://pypi.org/project/termcolor/)
* [Gitpod](https://gitpod.io/projects)
* Paint


## Credits and aknowledgements

- To color pyfiglet[Tic Le Polard](http://tic-le-polard.blogspot.com/2015/04/python-colored-ascii-art-with-pyfiglet.html)
- Video from Youtube for a basic quiz [HowToFAQ](https://www.youtube.com/watch?v=h4n_ByFuD90)
- [Stack Owerflow](https://stackoverflow.com/)
- [Slack](https://slack.com/)
- [Computing Learner](https://computinglearner.com/how-to-create-a-menu-for-a-python-console-application/)
- Code Institute for the deployment terminal
- My mentor for reviewing and helping with the code

