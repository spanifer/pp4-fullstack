<h1 align="center">PROJECT NAME</h1>

[View the live project here.]()

DESCRIPTION

![Responsive Design from http://ami.responsivedesign.is/]()

# Table of content

+ [Design Process](#design-process)
+ [Features](#features)
+ [Technologies](#technologies-used)
+ [Testing](#testing)
+ [Deployment](#deployment)
+ [Credits](#credits)

***

## Design Process

-   ### Roadmap

-   ### Application Aim

-   ### Opportunities

-   ### Implementation Priorities

-   ### User Stories

-   ### Agile Approach

-   ### Flowchart

![](readme/diagrams/)

-   ### Wireframes

![](readme/wireframes/)

-   ### Data Model

-   ### Surface 

![](readme/diagrams/)

## Features
<a href="#table-of-content">Go back <span style="font-size: 1.3em">🔝</span></a>

## Technologies Used
<a href="#table-of-content">Go back <span style="font-size: 1.3em">🔝</span></a>

### Languages Used

-   [Python](https://en.wikipedia.org/wiki/Python_(programming_language))

### Frameworks, Libraries & Programs Used

1. [Git](https://git-scm.com/)
1. [GitHub](https://github.com/)
1. [draw.io](https://www.diagrams.net/)

## Testing
<a href="#table-of-content">Go back <span style="font-size: 1.3em">🔝</span></a>

### Validators Testing
-   [W3C Markup Validator](https://jigsaw.w3.org/css-validator/#validate_by_input)
-   [W3C CSS Validator](https://jigsaw.w3.org/css-validator/#validate_by_input)
-   [Python](http://pep8online.com/)

### Testing User Stories

### Further Testing

### Found Bugs

- While deploying early to heroku: 
    1. Build failed:
        -   `git push heroku main` failed when running `python manage.py collectstatic --noinput` with *No such file or directory: '/tmp/build_643c5311/static'*    
        -   caused by Git not storing empty directories, and heroku does not automatically create the target directory that `collectstatic` uses. Solution found on [heroku documentation](https://devcenter.heroku.com/articles/django-assets)
        -   solution was to include a dummy file to make git create the folder. After that the heroku build process passed, and the deployment was a success. 
    1. Static files missing:
        -   self hosted static files are not supported on heroku, as stated [in the documentation](https://devcenter.heroku.com/articles/django-assets#whitenoise)
        -   the documentation draws attention to a project called [whitenoise](http://whitenoise.evans.io/en/stable/) that can integrate into Django applications, and were designed for this purpose. This solution been chosen for early deployment and testing.

### Known Bugs

-   ?

## Deployment
<a href="#table-of-content">Go back <span style="font-size: 1.3em">🔝</span></a>

The project was deployed using Code Institute's mock terminal for Heroku.

-   Steps for deployment:
    -   Fork or clone this repository
    -   Create a new Heroku app
    -   In the app settings:
        -   Add a config var of `PORT`:`8000`
        -   Set the buildpacks to `Python` and `NodeJS` in that order
    -   Link the Heroku app to the forked repository
    -   Manually **Deploy**

### Making a Local Clone

> *Review* to make the whole project locally deployable
Requires Python 3 installed in local environment, to run the game in a terminal

-   Fork or clone this repository
-   Navigate to folder in a terminal
-   Run the following command `python3 manage.py runserver`

## Credits
<a href="#table-of-content">Go back <span style="font-size: 1.3em">🔝</span></a>

### Code

### Acknowledgements

-   README.md structure inspired by several Code Institute's samples