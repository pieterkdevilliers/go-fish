# Go Fish

[View the live project here.](https://go-fish-ci.herokuapp.com/)

![](https://raw.githubusercontent.com/pieterkdevilliers/go-fish/17dff123f7ca0ffd58b6cc24f609179bf81a2659/docs/images/readme_images/responsive.webp)
The image is from [Am I responsive?](http://ami.responsivedesign.is/)

Go Fish is a terminal based card game aimed at children 6 years and above.

## UX
I aimed to create a story generator game for children that is fun and is very easy to manipulate and input data.

#### The ideal client:
* Children
* English Speaking
* Children who enjoy pattern matching games

### The game will help clients to:
* Navigate easily through the terminal
* Test their short term memory skills
* Provide entertainment

## Owner Stories
1. As the owner, I want the game to be fun and simple to play.
2. As the owner, I want the game to encourage the player to return for more games.
3. As the owner, I want to show my new learned skills with Python.

### User Stories
1. As a new visitor, I want to easily navigate the terminal and play the game.
2. As a visitor, I want to challenge myself to try and beat the computer.

## The skeleton
The game consists of a single page terminal interface, generated with Python.
* The inspiration for the project came from watching my daughters playing this as a real card game in a café in Paris. The sketches / wireframes below show the initial ideas I noted down as I watched them play.
![](https://raw.githubusercontent.com/pieterkdevilliers/go-fish/313bb83a79a02dfc8d3dc4753537a5d2422c9ef4/docs/images/readme-images/list-of-items.webp)

![](https://raw.githubusercontent.com/pieterkdevilliers/go-fish/313bb83a79a02dfc8d3dc4753537a5d2422c9ef4/docs/images/readme-images/flow-diagram.webp)

## The Scope
To achieve my goal, I included the following features in my game:

### Features
1. A welcoming message asking the user to enter his/her name.
2. List of 4 stories in the library which I can keep adding to.
3. A List of words like adjectives and verbs from which the user can select and then these words are returned into the stories.
4. The user has a choice to end the game by selecting 5.

### Future features
I ran out of time to implement these changes, I will implement them in the future:
* Form validation: The input required in the "name" box.
* Save score option.
* Top 5 high scores board.

## The Design
It is a children's game therefore the graphics are very child-friendly. Each story has its own image based on the title eg. place for "taco story" (I could not find a ASCII image for a taco), Pizza for "Pizza story",Teddy bear for "About me" and a Butterfly for "Butterflies".
* I have imported 'Time' which has allowed me to put a time break on how fast the text appeares in the terminal. Eg. there is a time.sleep(10) after a story which will take 10seconds before another selection for a story is possible. Giving the user a bit of time to read. Otherwise, everything would appear at the same time in the terminal.   

## Technologies Used
* [Gitpod](https://gitpod.io/workspaces) I used this developer to write the code for this game.
* [Github](https://github.com/) Was used to host my repository and readme.
* [Heroku](https://id.heroku.com/login)To host my app and deploy here.
* [pep8online.com](http://pep8online.com/) To validate my code and check for errors

## Testing
1. As a new visitor, I want to easily navigate the terminal to play the game.
* Here the user inputs his/her name and press enter.
* Then they get a selection of stories from which they can choose by selecting a number
![](https://github.com/MiaTothova/story-vault/blob/main/images/test-1.png)

2. As a visitor, I want to be able to exit the game when I get tired of playing..
* When user selects 5 they get a exit message.
![](https://github.com/MiaTothova/story-vault/blob/main/images/test-2.png)

3. As a visitor, I want to be create and read fun stories.
* After imputing words a fun story is created.
![](https://github.com/MiaTothova/story-vault/blob/main/images/test-3.png) 

 ### Adicional Testing
* I continously used the pep8online linter to confirm my code is problem-free
* I used and tested in the gitpod terminal replaying and fixing issues until I got it right.
* Tested on the Heroku terminal as I set up automatic deployment so I was able to see exactly how the game was generated.

 ## Compatibility
To ensure that a broad range of users can successfully view/use the site, I tested it across all major browsers on both desktop and mobile.
* Chrome
* Mozila Firefox
* Edge
* Internet explorer
* Safari
Although this is a web app it is visible on a mobile and tablets, even though it is not responsive.

## Validation
![](https://github.com/MiaTothova/story-vault/blob/main/images/pep8.png)

## Deployment
This project was developed using Heroku, committed to git and pushed to GitHub using git commands. You can clone this repository [Here](https://github.com/MiaTothova/story-vault)

To deploy this page to Heroku from GitHub repository, the following steps were taken:

1. In the Heroku dashboard I selected 'New' in the top right hand corner and clicked on 'Create new app'.
2. Then I Created the App name and Choose my region as Europe. Then selected 'Create app'
4. Then I selected Settings tab, and scrolled down to 'Buildpacks'. Here I added 'Python' clicked saved changes and then selected 'Node.js' and saved my changes again.
5. On top of the page I clicked on the 'Deploy' section, and I selected Github as my deployment method.
6. Then I selected 'Connect to Github, and searched for my repository name and clicked on 'Connect' to link my Heroku app to my Github repository code.
7. Scrolling down I have selected 'Enable Automatic Deploys' and after this I selected 'Deploy Branch' to deploy my project. I had to wait for it to build.
8. After it has successfully deployed a 'view' button appeared which took me to my deployed app.

## Credits
* With this project everything seemed pretty straightforward. 
* I have used youtube and google search to look up inspirations on how to aproach a Madlib game. I have not copied or reused anyone else's code in this project. 
* I have watched the following videos for inspiration:
   1. [Mad Libs Game](https://www.youtube.com/watch?v=u7g9mRzQLYE&t=2s)
   2. [Build a Mad Libs Generator](https://www.youtube.com/watch?v=vFNZvZSOqlY&t=2s)
* [This site was used to get my templates for my stories](https://www.glowwordbooks.com/blog/category/kids-online-mad-libs/) 
* [This website was used to get ASCII code for my images](https://www.asciiart.eu/)
* My Mentor Guido Cecilio Garcia Bernal was extremely helpful in breaking all the steps down for me and answering any questions I had Especially in regards to the dictionary.
* Kasia Bogucka our Cohort Facilitator was very hepful in answering questions and providing us with information from Code Institute.
