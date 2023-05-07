# Let's Bake!

A baking blog.

[Link to Hangman game]()

![Game shown on a range of devices](docs/amiresponsive.png)

* [User Experience (UX)](#User-Experience-(UX))
  * [Initial Discussion](#Initial-Discussion)
  * [Agile Methodology](#Agile-Methodology)
  * [Epics & User Stories](#Epics-&-User-Stories)

* [Design](#Design)
  * [Colour Scheme](#Colour-Scheme)
  * [Fonts](#Fonts)
  * [Imagery](#Imagery)
  * [Wireframes](#Wireframes)
  * [Database Model](#Database-Model)

* [Features](#Features)
  * [Future features](#Future-features)

* [Security Features & Defensive Design](#Security-Features-&-Defensive-Design)

* [Technologies Used](#Technologies-Used)
  * [Languages Used](#Languages-Used)
  * [Frameworks, Libraries & Programs Used](#Frameworks,-Libraries-&-Programs-Used)

* [Testing](#Testing)
  * [Solved Bugs](#Solved-Bugs)
  * [Known Bugs](#Known-Bugs)
  * [PEP8](#PEP8)
  * [Manual Testing](#Manual-Testing)

* [Deployment](#Deployment)
  * [Local Deployment](#Local-Deployment)
  * [Remote Deployment](#Remote-Deployment)
  * [Deploy project to Heroku](#Deploy-project-to-Heroku)
  
* [Credits](#Credits)
  * [Code](#Code)
  * [Content](#Content)
  * [Acknowledgements](#Acknowledgements)

- - -

## User Experience (UX)

### Initial Discussion


#### Key information:
* 
* 
* 

### Agile Methodology


### Epics & User Stories

#### Epic 1

##### User Story

* Task: 

#### Epic 2

##### User Story

* Task: 

#### Epic 3

##### User Story

* Task:

- - -

## Design

### Colour Scheme
The termcolor module was used to print colored text.

Bright and bold colors were used throughout the game to draw the users attention for a specific purpose or engagement.

Color consistancy is used in the below instances:
* Cyan is used largely when requesting user input.
* Magenta is used largely when the user's chosen name is called alongside text to draw their attention.
* Red is used largely when error messages are raised for invalid input.

### Fonts

### Imagery

### Wireframes


### Database Model


![Database Model](docs/databasemodel.png)

- - -

## Features
Below are the main features the user will come across 

1. 

![First feature](docs/features/)

   User input is validated 

![First user input validation](docs/features/)

2. 

![Second feature](docs/features/)

   User input is validated 

![Second user input validation](docs/features/)

3. 

![Third feature](docs/features/)

   User input is validated 

![Third user input validation](docs/features/)

4. 

![Fourth feature](docs/features/)

   User input is validated 

![Fourth user input validation](docs/features/)

5. 

![Fifth feature](docs/features/)

6. 

![Sixth feature](docs/features/)

7. 

![Seventh feature](docs/features/)

8. 

![Eighth feature](docs/features/)

9. 

![Ninth feature](docs/features/)

10. 

![Tenth feature](docs/features/)

### Future features
* 
* 
* 

### Security Features and Defensive Design

#### User Authentication

#### Form Validation

#### Database Security

- - -

## Technologies Used

### Languages Used


### Frameworks, Libraries & Programs Used
* [Am I responsive?](https://ui.dev/amiresponsive) - to show game across a range of devices.
* Git - for version control. 
* GitHub - to save and store the code pushed from Git.
* GitPod - using GitPod terminal to commit to Git and push to GitHub.

- - -

## Testing 
Issues raised in my project meetings with my mentor [Chris Quinn](https://github.com/10xOXR) :

1. 

### Solved Bugs

1. 

2. 

3. 

![Issue](docs/testing/issues/)



![Fix](docs/testing/issues/)

### Known Bugs

1. 

### PEP8 
Testing carried out via [PEP8 Validator](https://pep8ci.herokuapp.com/):
* 

### Manual Testing
* Tested website on mobile with [Chrome](docs/testing/manualtesting/chrome-mobile.jpg) & [Samsung internet](docs/testing/manualtesting/samsunginternet-mobile.jpg)
* Tested on laptop with [Microsoft Edge](docs/testing/manualtesting/microsoftedge-laptop.png) and desktop with [Firefox](docs/testing/manualtesting/firefox-desktop.png).

- - -

## Deployment 

### Local Deployment

#### How to Clone
1. Sign up or log in to GitHub
2. Go to the repository https://github.com/Sarohia94/Project-3-Hangman
3. Go to the code dropdown and select how you'd like clone and copy the link provided
4. Go to the new repo and enter in your workspace terminal, "git clone" (without quotes) followed by the link copied
5. Install necessary libraries/frameworks to the terminal 
6. Enter the following command "pip3 freeze > requirements.txt" (without quotes) to the terminal to install the libraries/frameworks dependencies which will be required if this is deployed to Heroku
7. Enter command "python3 manage.py runserver run.py" (without quotes) to run the browser.

#### How to Fork
1. Sign up or log in to GitHub
2. Go to the repository 
3. Click on the fork button towards the top right of the page 

### Remote Deployment
The website was deployed to GitHub Pages as follows:
1. Log in to GitHub
2. Assuming you have cloned or forked the repository, go on the "Settings" link for this repository
3. Click on the "Pages" link on the left hand side of the page
4. Under "Source" select "Deploy from branch" from the dropdown
5. Under "Branch" select "main" from the dropdown
6. Click "Save" which will then refresh the page
7. It might take a few mins before you can refresh and view the link to the site published

### Deploy project to Heroku
1. Assuming you have cloned or forked the repository, sign up or log in to Heroku
2. Go to "new" and click "create new app", the "create new app" is also available from the dashboard
3. Enter a unique app name and choose a region
4. Click "create app"
6. Go to the Settings tab and set the Buildbacks to Python and NodeJS, in that order
7. On the same tab go to Config Vars, click "reveal config vars" and enter PORT in to "KEY" and 8000 in to "VALUE" and then click "Add"
8. Now go to the Deploy tab and click "Connect to Github" from Deployment Method.
9. Search by the repository name (which needs to match exactly), once this is found 
10. Enable automatic deploys if preferred 
11. Go to Manual deploy, the branch to deploy should be main and then click on "Deploy Branch"
12. Once deployment is complete you can click "View" to open the game in Heroku

- - -

## Credits

### Code
* 

### Content
* The content was written by the developer Amritpreet Sarohia.
* 
* 

### Acknowledgements 
Thank you to anyone taking the time to view my third project. Special thanks to the Slack community and the below individuals:
* [Chris Quinn](https://github.com/10xOXR), my mentor. Thank you for your guidance and feedback.
* To the tutors from tutor support for their help and assistance: S