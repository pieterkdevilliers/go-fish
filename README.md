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
The includes the following features:

### Features
1. A welcome message explaining the rules of the game.
2. Simple in-game notifications confirming who's run it is, what cards are held and requested.
3. In-game score report, showing the status of each player's Four Of A Kind table.
4. The user can easily play another game by clicking the `Run Program` button in the interface.

### Future features
In the future I would like to add the following features:
* Multi-player - ability to have more than one player against the computer.
* Improved deck / hand display, although this might be limited by the terminal output.

## The Design
As this is a childrens game, the interface and the game format is kept simple.
* I imported `time` to allow for a slowed-down display of the terminal message, to help with keeping track of where the game is up to.

## Technologies Used
* [Gitpod](https://gitpod.io/workspaces) - Used for writing the code and git management.
* [Github](https://github.com/) - Used to host the repository.
* [Heroku](https://id.heroku.com/login) - Used to host the live game.
* [pep8online.com](http://pep8online.com/) To validate my code and check for errors

## Testing
1. As a new visitor, I want to easily navigate the terminal to play the game.
* Once the user has read the rules, they only need to press `Enter` in order to start the game.
* The user then receives a notice that the cards are being dealt, as well as a list of the cards they now hold in their hand.

![](https://raw.githubusercontent.com/pieterkdevilliers/go-fish/ee4d6a689fa2f92590f4253900d059ebf3f559e5/docs/images/readme-images/card-dealing.webp)

2. As a visitor, I want to challenge myself to try and beat the computer.
* The player does not know what cards the Computer holds, but because the computer and the player can only request a card to a value of at least one of the cards they already hold, the player can infer what cards the computer has, based on past requests from the computer.

![](https://raw.githubusercontent.com/pieterkdevilliers/go-fish/ee4d6a689fa2f92590f4253900d059ebf3f559e5/docs/images/readme-images/infer-computer-cards.webp)

 ### Additional Testing
* I used the pep8online linter to review my code and highlight issues.
* I carried out a lot of game testing as I wrote the game, confirming behaviour and outcomes with temporary print statements.
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
