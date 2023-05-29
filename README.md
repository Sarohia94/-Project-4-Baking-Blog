# Let's Bake!

Let's Bake is a baking blog developed using Django, Python, HTML, CSS and JavaScript.

The blog is designed to share the love of baking.  The blog provides general baking relating posts as well as recipes for visitors, which is the core purpose of the blog. 

Registered users have the option to share, edit and delete their own recipes. They can also like and comment on all posts.

[Go to blog website, Let's Bake!]()

![Game shown on a range of devices](docs/amiresponsive.png)

* [User Experience (UX)](#User-Experience-(UX))
  * [User & Blog Goals](#User-&-Blog-Goals)
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
  * [W3C Validator](#W3C-Validator)
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


### User & Blog Goals

#### Targeted User Goals:
* A user interested in baking.
* A user who wants access to recipes.
* A user that wants a platform to share their own recipes.

#### Site User Goals:
* For users to be able to interact with the site intuitively.
* For users to be able to access and view all posts.
* For users to be able to learn recipes and baking related posts.
* For users to be able to create an account to access additional functionality.
* For registered users to be able to log in and out of their account.
* For registered users to be able to like and comment on all posts.
* For registered users to be able add, edit and delete their own recipes.

#### Blog Goals:
* Offers a platform to promote community and love for baking.
* Provide registered users the access to like, comment and share recipes with full CRUD functionality.


### Agile Methodology

This blog was developed with agile planning. Each individual user feature was split into a user story. Each user story was defined and included an acceptance criteria. The acceptance criteria were tasks to mark as complete to complete the user story. 

Related user stories achieving a certain functionality of the blog were grouped together in to Epics.

Each user story was labeled as Must Have, Should Have and Could Have to help prioritise which were most important to implement.

As the blog evolved, tasks were added or updated, based on the changing needs / understanding of the what the blog should provide the user.

This was implemented through Github Issues and the Kanban board in the projects view in Github, the project was divided into a few different sections:

* To Do - All user stories were initially entered in the 'To Do' column
* In Progress - During development stories were moved into the 'In Progress' column
* Done - On completion they get moved into the 'Done' column
* Future - Any 'could have' stories with features that I can look to implement at a later date, where due to time restraints I was unable to work on.

Please find my Kanban Board with my user stories [here](https://github.com/users/Sarohia94/projects/3/views/1).


### Epics & User Stories

Epic 1: Website UI Features

User Story #1

Site pagination (must have) - As a site user I can view a paginated list of posts so that easily select a post to view.

Acceptance Criteria:
* As a site user I can view 4 posts per page.
* As a site user it is easy to navigate and view posts to pick which one I want to read.

User Story #2

View post (must have) - As a site user I can view a list of posts so that I can select one to read.

Acceptance Criteria:
* As a site user, I can view posts submitted.
* As a site user, I can view the image, recipe title and short description to help choose what to read.

User Story #3

Open a post (must have) - As a site user I can click on a post so that I can read the full text.

Acceptance Criteria:
* Clicking on post opens a page where user can view the full post/recipe.

User Story #4

Search bar (could have) - As a site user I can use a search bar to search for a specific recipe so that I have quick and easy access to the information I want.

Acceptance Criteria:
* As a site user, I can easily find and navigate to the search bar.
* As a site user, I can use the search bar to search by recipe name.
* As a site user, I can view the results yielded by my search that I can click from.

Epic 2: Registration & Account Features

User Story #6 

Account registration (must have) - As a site user I can register an account so that I can submit my own post, comment and like.

Acceptance Criteria:
* As a site user, I intuitively know where to go to sign up.
* As a site user, I can easily register my account without issue.

User Story #7

Login & logout (must have) - As a registered user, I can login and logout of the site so that I can have access to my account.

Acceptance Criteria:
* As a registered user, I can login and out successfully.

User Story #8

Comment on a post (must have) - As a registered user I can leave comments on a post.

Acceptance Criteria:
* As a logged-in user I can leave comments on a post so that I can be involved in the conversation.

User Story #9

Like/Unlke (must have) - As a site user I can like or unlike a post.

Acceptance Criteria: 
* As a logged-in user I can like or unlike a post so that I can interact with the content.

User Story #10 

Add a recipe post (must have) - As a registered site user I can add a recipe post.

Acceptance Criteria: 
* As a logged-in user I can add a recipe so that I participate in growing the site.
* As a logged-in user I can edit/delete my recipe so that I can update/delete my submission.

User Story #11

View my posts and likes (could have) - As a registered site user, I can access all my blog posts and likes easily in one place so that I can easily track my activity on the site.

Acceptance Criteria: 
* As a logged-in user I can view a page with a list of all my posts.
* As a logged-in user I can view a page with a list of all my likes.

Epic 3: Blog Features

User Story #12 

Manage posts (must have) - As a site admin I can create, read, update and delete posts so that I can manage my blog content.

Acceptance Criteria: 
* As a site admin, I can create new posts.
* As a site admin, I can click and read posts.
* As a site admin, I can edit and delete posts.

User Story #12 

Create drafts (should have) - As a site admin I can create draft posts so that I can finish writing the content later.

Acceptance Criteria:
* As a site admin I can start a draft post.
* As a site admin I can return back to my account and finish my draft.
* As a site admin I can then successfully post once ready.

User Story #13

View likes (must have) - As a site user, I can view the number of likes on each post so that I can see which is the most popular or viral.

Acceptance Criteria:
* As a site user, I can clearly view a symbol associated with likes on a post.
* As a site user, I can view the number of likes next to the likes symbol.

User Story #14

View comments (must have) - As a site user, I can view comments on an individual post so that I can read the conversation.

Acceptance Criteria:
* As a site user, I can clearly view a symbol associated with comments on a post.
* As a site user, I can view the number of comment next to the comments symbol.


- - -

## Design

### Colour Scheme

The colour scheme was taken from [Coolors](https://coolors.co/). 

It was based on the image used for the [Favicon icon](https://www.pngall.com/wp-content/uploads/5/Yummy-Cupcake-PNG-Picture.png) which I thought was fun and inviting.

The use of these colours have been consistently maintained throughout the website and checked for contrast to allow easy accessibility.

![Colour palette for the Let's Bake blog website](docs/colourpalette.png)

### Fonts

[Google Fonts](https://fonts.google.com/) were used as below:

* Indie Flower is used for the title.
* Acme is used for the body of the text. 

### Imagery

Images used were warm or colourful to fit the theme and intention of the website, which is about love of baking & sharing recipes to engage users to want to make themselves. 

Hero image and placeholder featured image for post was taken from [Pexels](https://www.pexels.com/), the Favicon icon from [PNG All](https://www.pngall.com/) and all recipe images can be found in the credits section.

### Wireframes

Wireframes were created for destop/laptop, tablet and mobile.

* Home page wireframe can be found here for [desktop/laptop](docs/wireframes/laptop_desktop_blog_home.png), here for [tablet](docs/wireframes/tablet_blog_home.png) and here for [mobile](docs/wireframes/mobile_blog_home.png).

* Recipe page wireframe can be found here for [desktop/laptop](docs/wireframes/laptop_desktop_blog_recipe.png), here for [tablet](docs/wireframes/tablet_blog_recipe.png) and here for [mobile](docs/wireframes/mobile_blog_recipe.png).

* Sign up page wireframe can be found here for [desktop/laptop](docs/wireframes/laptop_desktop_blog_sign_up.png), here for [tablet](docs/wireframes/tablet_blog_sign_up.png) and here for [mobile](docs/wireframes/mobile_blog_sign_up.png).

* Sign in page wireframe can be found here for [desktop/laptop](docs/wireframes/laptop_desktop_blog_sign_in.png), here for [tablet](docs/wireframes/tablet_blog_sign_in.png) and here for [mobile](docs/wireframes/mobile_blog_sign_in.png).


A bootstrap template was used to help format the core blog website. Custom css styling and html was also used.

* [Bootstrap template](https://startbootstrap.com/template/blog-home)

### Database Model

Principles of object-oriented programming was used throughout this project and Django’s class-based generic views. Django AllAuth was used for user authentication.

A custom database model was developed as below for recipes.

![Custom database model](docs/custom__model.png)

The custom model was made to incorporate CRUD functionality. This allows registered users and admin to add, edit or delete recipes, both from the live site and from the Django database via the Django admin page.

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
* From the user page the user will be able to view all their recipes and likes easily in one place so that they can see their activity on the site.
* As the blog grows it would be ideal to implement a search bar so the user can easily find what they are looking for.
* As the blog grows, update the recipe model to include catergories and have all recipes classified and accessible from the main site by these categories (i.e. cakes, pastry, bread etc).

- - -

## Security Features & Defensive Design

I have tried to use defensive programming throughout the site to prevent users accessing pages, submitting requests if they don't have the relevant permissions. 

#### User Authentication

* Django's LoginRequiredMixin is used to ensure that any requests to access secure pages by non-authenticated or, in some cases, non-admin users, are immediatley redirected to the login page.

* Django's UserPassesTestMixin is used to check any number of conditions and will deny a request with a permission error if the test_func() method returns false. As such the user is authenticated before the request is completed.

* Check for authenticated users in templates by using the if statement i.e. {% if user.is_authenticated %}, before allowing access (adding comments) or visibility to links (user page).

#### Form Validation

* Messages are present for fields forms where validation is required. If a user attempts to sign up or login without completing the relevant fields a message is displayed. User will not be able to sign in or login until all relevant fields are filled in.

* Similary when submitting a recipe if the required fields are not filled in then the user will be directed to the empty required field. This will not submit until all required fields are completed.

#### Database Security

The database url and secret key are stored in the env.py file to prevent unwanted connections to the database. The env.py file was created before the initial push to GitHub.

Cross-Site Request Forgery (CSRF) tokens were used on all forms throughout this site.

#### Custom Error Page

This was created following a tutorial (linked in the credits) for when a user is trying to access a recipe to delete it. This will give the user some information on the error and give them a link to return home.

* 403 Unauthorized Access - You're not authorized to perform this action

- - -

## Technologies Used

### Languages Used

* HTML
* CSS
* Javascript
* Python

### Frameworks, Libraries & Programs Used
* [Am I responsive?](https://ui.dev/amiresponsive) - to show game across a range of devices.
* Git - for version control. 
* GitHub - to save and store the code pushed from Git.
* GitPod - using GitPod terminal to commit to Git and push to GitHub.
* Balsamic - to create the wireframes when designing the website.
* Dev Tools - for testing and troubleshooting.
* [Google Fonts](https://fonts.google.com/) - to import font to apply on the website.
* [Font Awesome](https://fontawesome.com/) - to add icons.
* [Wave](https://wave.webaim.org/) - to test web accessibility.
* [W3C](https://validator.w3.org/) - HTML validator.
* [Jigsaw](https://jigsaw.w3.org/css-validator/) - CSS validator.
* [Jshint](https://jshint.com/) - to check for errors and problems with javascript code.
* Hover.css - to make the nav bar, footer links and the sign up button interactive.
* [Tiny PNG](https://tinypng.com/) - to compress images.
* [Responsive design checker](https://responsivedesignchecker.com/) - to check responsive design for a variety of screen sizes.
* [Favicon.io](https://favicon.io/favicon-generator/) - to creat favicon icon for the website.
* Django Crispy Forms - provides a tag and filter that lets you quickly render forms
* Django Allauth - used for authentication, registration & account management.
* Django - a high-level Python web framework that encourages rapid development
* Bootstrap - a framework for building responsive, mobile-first sites.

- - -

## Testing 
Issues raised in my project meetings with my mentor [Chris Quinn](https://github.com/10xOXR) :S

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
Testing carried out via [PEP8 Validator](https://pep8ci.herokuapp.com/), all clear, no errors found:
* Letbake
1. [asgi.py](docs/testing/pep8/pep8_asgi.png)
2. [settings.py](docs/testing/pep8/pep8_settings.png)
3. [urls.py](docs/testing/pep8/pep8_urls.png)
4. [wsgi.py](docs/testing/pep8/pep8_wsgi.png) 


### W3C Validator 
No issues with the HTML pages or CSS:
* [Home](docs/testing/w3c/w3c_home.png)
* [Post detail](docs/testing/w3c/w3c_post_detail.png)
* [Recipe detail](docs/testing/w3c/w3c_recipe_detail.png)
* [Recipes](docs/testing/w3c/w3c_recipes.png)
* [Sign up](docs/testing/w3c/w3c_signup.png)
* [Login](docs/testing/w3c/w3c_login.png)
* [Logout](docs/testing/w3c/w3c_logout.png)
* [User page](docs/testing/w3c/w3c_user_page.png)
* [css](docs/testing/w3c/w3ccss.png) - parse errors only

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