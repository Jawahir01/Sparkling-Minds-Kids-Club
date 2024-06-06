<h2 align="center"><img src="/static/img/logo-2.png" width="180" height="180"></h2>

# Sparkling Minds Club

Sparkling Minds club is a fictional club for children to join in . It reflects the wide range of activities and courses that kids’ clubs typically offer.

![Site](static/img/Doc/am-i-responsive.png)

**To visit the live link click**: [Sparkilng Minds Club](https://sparkling-minds-ffd249568f6d.herokuapp.com/)

## Table of Contents

- [Sparkling Minds Club](#sparkling-minds-club)
  - [Table of Contents](#table-of-contents)
- [User Experience Design](#user-experience-design)
  - [The-Strategy-Plane](#the-strategy-plane)
    - [Site Goals](#site-goals)
    - [Agile Planning](#agile-planning)
    - [User Stories](#user-stories)
- [The-Scope-Plane](#the-scope-plane)
- [The Structure Plane](#the-structure-plane)
    - [Features](##features)
  - [The Skeleton Plane](##the-skeleton-plane)
    - [Wireframes](#wireframes)
    - [Database Design](#database-design)
    - [Security](#security)
  - [The-Surface-Plane](#the-surface-plane)
    - [Design](#design)
    - [Colour-Scheme](#colour-scheme)
    - [Typography](#typography)
    - [Imagery](#imagery)
  - [Technolgies](#technolgies)
- [Testing](#testing)
- [Deployment](#deployment)
    - [Heroku Deployment](#heroku-deployment)
    - [Run Locally](#run-locally)
    - [Fork Project](#fork-project)
- [Credits](#credits)
- [Acknowledgments](#acknowledgments)

# User Experience Design(UX)
 - ## The-Strategy-Plane
     - ### a. Site Goals
        -	Overview:

            Sparkling Minds Club website aims to provide a diverse array of options for parents to enroll their children in various courses, sports, and activities. The primary goal is to create a user-friendly platform where parents can easily explore, select, and register their kids for enriching experiences.
        - Key Objectives:

          	- User-Friendly Interface: The website prioritizes ease of use and navigation, ensuring that parents can quickly find relevant information and enroll their children in desired activities.

        	- Diverse Offerings: We offer a wide range of courses, sports, and activities to cater to different interests, ages, and skill levels of children.

        	- Convenient Registration Process: Parents can easily register and add their children for courses and activities.

        	- Transparent Information: We provide detailed information about each course and activity, including schedules and instructors enabling parents to make informed decisions.

        	- Engaging Content: The website features engaging content, including photos, and testimonials, to showcase the excitement and benefits of participating in our programs.



      - ### b. Agile Planning
        The Agile planning for Sparkling Minds Club involved breaking down the project into smaller, manageable tasks and iterations, prioritizing them based on value, and adapting to changes as needed.
	![Agile](static/img/Doc/agile.png)


      - ### c. User Stories
        -	As a First Time Users:
            1.	I want to be able to easily understand the main purpose of the app, so that I can learn more about this app.
            2.	I want to be able to easily navigate through the app, so that I can find the content.
            3.	I want to be able to register my account, so that I can learn the benefits of the app as a user.
        -	As a Frequent Users:
            1.	I want to be able to log in to my account, so that I can have a personal account.
            2.	I want to be able to easily log in and log out.
            3.	I want to be able to easily recover my password in case I forget it, so that I can recover access to my account.
            4.	I can be able to change my password, so that I can be sure that nobody else can access my account.
            5.	I would like to be able to add my child/children to the site and enrol him/them on the desired program.
            6.	I would like to be able to edit my child/children information so that I can make changes when needed.
            7.	I would like to be able to delete my child/children information when they are done or no longer participating in the program.
        -	As a Site Owner:
	    
            I want parents and kids to have a blast using the app! I envision an experience where families can easily check out all the cool activities and courses we offer. Parents should feel informed, and kids should be super excited to join in. My goal is to make the app easy to use, fun to explore, and full of awesome opportunities for learning and growth.
        -	As a developer:
            1.	I need to create the navbar so that users can navigate the website from any device.
            2.	I need to create the base.html page and structure so that other pages can reuse the layout.
            3.	I need to create static resources so that images, css and javascript work on the website.
            4.	I need to set up the project so that it is ready for implementing the core features.


# The-Scope-Plane
  -	Responsive Design - Site should be fully functional on all devices.
  -	Hamburger menu for tablet/mobile devices
  - Ability to perform CRUD functionality on Users and child/children added by the users.

# The Structure Plane
- ## Features
  The website includes a home page, a login page, a registration page, a profile page, and a calendar page. Every page is designed to adapt seamlessly to various devices, ensuring full responsiveness across different screen sizes.

  All pages have:
  #### A header:
  contains an image and a text of the logo at the far left and a navigation bar at the right.
The Navigation bar has the links of Home page, Features [About us, Gallery, Teachers, Testimonials] subheadings in the main page, courses page, contact Us page and a dropdown of User font awesome icon.
  -	If the user is new or not registered, the user fontaweson will dropdown to two links: Sign in and Register.
    ![Header](static/img/Doc/Features/header-non-registerd.png)

  -	If the user is registered or signed in, the user fontawesome icon will dropdown to two links: Profile and Sign out.
     ![Header](static/img/Doc/Features/header-regisred.png)
  
  On the mobile version of the website, the navigation bar will have a hamburger menu icon.
  ![Header](static/img/Doc/Features/mobile-header.png)

  #### A Footer:
  contains the following sections:
  -	Get in Touch with address, phone number, email address and social media links that open in a new tap.
  -	Quick Links to some sections or pages on the website.
  -	Photo Gallery which contains a sample photo of the Gallery Section.
  -	Section for the copy right with an image of the logo and reference to the designer, distributer, developer of the website.
    ![Footer](static/img/Doc/Features/footer.png)

  On the mobile/ tablet version these sections will layout on top of each other.

![Footer](static/img/Doc/Features/mobile-footer.png)

  **The pages of the website are:**
  #### Home page
   ![Home](static/img/Doc/Features/home-1.png)
  ![Home](static/img/Doc/Features/home-2.png)
  ![Home](static/img/Doc/Features/home-3.png)
  ![Home](static/img/Doc/Features/home-4.png)
  ![Home](static/img/Doc/Features/home-5.png)
  #### Courses Page
  ![Courses](static/img/Doc/Features/courses-page.png)
  #### Register Page
  ![Register](static/img/Doc/Features/register-page.png)
  #### Sign in Page
  ![signin](static/img/Doc/Features/sign-in-page.png)
  #### Forget Password Page
  ![singin](static/img/Doc/Features/forgot-password-page.png)
  #### Update Password Page
  ![signin](static/img/Doc/Features/update-password-page.png)
  #### Profile Page
   ![Profile](static/img/Doc/Features/profile-page.png)
  #### Profile Page when add Child button is clicked.
   ![Profile](static/img/Doc/Features/profile-add-child-btn.png)
  #### Profile Page after a child is added.
  ![Profile](static/img/Doc/Features/profile-child-added.png)
  #### Profile Page when child is edited.
  
  #### Contact Us Page
  ![Contact-us](static/img/Doc/Features/contact-us-page.png)
  #### Thank You Page
  ![Thank-you-page](static/img/Doc/Features/thank-you-page.png)


- ## Future Implementations
  -	Give the user to choose whether he wants to delete his account.
  -	Make the course/Activities with various prices that suits the parents with coupons feature.
  -	Use a safe payment method.
   

- ## The Skeleton Plane
  - ### Wireframes
    -	Home page
	![Home](static/img/Doc/wireframes/home-page.png)

    -	Courses page
	![courses](static/img/Doc/wireframes/course-page.png)

    -	Register page.
	![register](static/img/Doc/wireframes/register-page.png)

    -	Sign in page.
	![signin](static/img/Doc/wireframes/signin-page.png)

    -	Profile page.
	![profile](static/img/Doc/wireframes/profile-page.png)

    -	Profile page/add a child/children.
	![profile-add-child](static/img/Doc/wireframes/profile-add-child.png)

    -	Profile page/ preview child/children.
	![profile-preview-child](static/img/Doc/wireframes/profile-preview-child.png)

    -	Contact us page.
	![contact-us](static/img/Doc/wireframes/contact-us-page.png)

    -	Thank you page.
	![thank-you](static/img/Doc/wireframes/thank-you-page.png)



  - ### Database Design
      ![database_design](static/img/Doc/wireframes/database_design.png)

    This is the basic outline of the database design and data modeling for the Sparkling Minds kids club project using MongoDB, taking in consideration the different entities and their relationships within the application:
	- **Entities:**

		- Users: Store information about registered users.
		- Kids: Store information about children registered by users.
		- Courses: Store information about available courses or activities for kids.
	- **Database Schema:**
		- Users Collection:
			- _id: Unique identifier for the user (automatically generated by MongoDB).
			- username: Username of the user.
			- first-name: First name of the user.
			- last-name: Last name of the user.
			- email: Email address of the user.
			- password: Hashed password of the user.
			- security-question: Security question for password recovery.
			- security-answer: Answer to the security question.
		- Kids Collection:
			- _id: Unique identifier for the child (automatically generated by MongoDB).
			- username: Username of the parent (related to the Users collection).
			- childfname: First name of the child.
			- childlname: Last name of the child.
			- date_of_birth: Date of birth of the child.
			- school_name: Name of the school the child attends.
			- school_year: Current academic year of the child.
			- child_choice: List of courses or activities chosen by the child(related to the Courses collection).
			- child_med_conditions: Medical conditions or allergies of the child.
		- Courses Collection:
			- _id: Unique identifier for the course (automatically generated by MongoDB).
			- course_name: Name of the course or activity.
			- description: Description of the course or activity.
			- age_group: Suitable age group for the course.
			- schedule: Schedule or timings of the course.

	- **Data Modeling:**
		- Users Collection:

	  ``` 
			{
  			"username": "john34",
  			"first-name": "John",
  			"last-name": "Doe",
  			"email": "john@example.com",
  			"password": "hashed_password",
  			"security-question": "What is your favorite teacher's name?",
  			"security-answer": "Mrs.Baker"
			}
		```

		- Kids Collection:

		```
			{
 			"username": "John",
 			"childfname": "Alice",
  			"childlname": "Doe",
  			"date_of_birth": "2010-05-15",
  			"school_name": "ABC School",
  			"school_year": "Year 4",
  			"child_choice": ["Football", "Englisg Course"],
  			"child_med_conditions": "None"
			}
			```

	- Courses Collection:

		```
			{
  			"course_name": "Maths Course",
  			"Teacher": "Elena Jacobs",
  			"School_year": "1 - 6",
  			"course_Days": "Saturday - Sunday",
  			"course_time": " 10:00 - 11:00 AM"
			}
		```


- # The-Surface-Plane

  - ## Design
  - ### Colour-Scheme
      ![Thank-you-page](static/img/Doc/colors.png)
  - ### Typography

    - The fonts for the website were imported using Google Fonts.
    - The main font is ‘Heebo’ as a clear, legible font suitable for body text. and ‘San Serif’ as a fallback font for the text on screens of all sizes.
    - The Headings are ‘cursive’ to add a playful and whimsical touch to the website, and ‘Lobster Two’ as a fallback font for the text on screens of all sizes.
  	In fact, by combining the features of both fonts and design principles, The Sparkling Clubs Website can effectively capture the attention and imagination of its young audience while providing an enjoyable and informative online experience.

  - ### Imagery
    - The Website logo was made by [Ussama Youssif](https://www.linkedin.com/in/ussama-youssif-59bb94105/?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=android_app) as copyright.
    - The images were taken from google.

- ## Technolgies
  - ### Languages:
    -	Python 3.11: the primary language used to develop the server-side of the website.
    -	JS: the primary language used to develop interactive components of the website.
    -	HTML: the markup language used to create the website.
    -	CSS: the styling language used to style the website.
  - ### Frameworks and libraries:
    -	Flask: python framework used to create the application.
    -	Javascript and jQuery User Interface were used to create interactive elements.
  - ### Databases:
    -	Mongo Database: the database used to store all the data.
  - ### Other tools:
    -	Git: the version control system used to manage the code.
    -	Pip3: the package manager used to install the dependencies.
    -	GitHub: used to host the website's source code.
    -	Chrome DevTools: was used to debug the website.
    -	Font Awesome: was used to create the icons used on the website.
    -	Google: was used to for random photos of children and teachers.
    -	W3C Validator:  was used to validate HTML5 code for the website.
    -	W3C CSS validator: was used to validate CSS code for the website.
    -	JShint: was used to validate JS code for the website.
    -	PEP8: was used to validate Python code for the website.
    -	BootStrap5: was used to create responsive elements.


# Testing
Test cases and results can be found in the [TESTING.md](TESTING.md) file.

# Deployment

- ## Heroku Deployment


- ## Run Locally
  Navigate to the GitHub Repository to clone to use locally:

    - Click on the code drop down button.
    - Click on HTTPS
    - Copy the repository link to the clipboard.
    - Open your IDE of choice (git must be installed for the next steps)
    - Type 
    ```
     git clone 'https://github.com/Jawahir01/Sparkling-Minds-Kids-Club.git'
    ```
    into the IDE terminal.
    
    The project will now have been cloned on your local machine for use.

#### **The Live Link:** https://sparkling-minds-ffd249568f6d.herokuapp.com/


# Credits
- [Codeanywhere](https://codeanywhere.com/): the IDE used to develop the website.
- [ThemeWagon](https://themewagon.com/themes/free-responsive-html5-bootstrap-5-preschool-website-template-kider/): For providing a free Responsive HTML5 Bootstrap 5 Educational Website Templates.
- [ChatGPT](https://chat.openai.com/): was used to write the update form codeand to give more formal sentences for the website and README file.
- [Favicon.io](https://favicon.io/): was used to convert the logo image into favicon.
- [Stack Overflow](www.stackoverflow.com) - was used to search for code related errors and bugs.
- [jeda.ai](https://go.jeda.ai/): was used to make wireframes for the website.

# Acknowledgments
  - **[Iuliia Konovalova](https://github.com/IuliiaKonovalova)** :My Mentor Guidance at Code Institute for her professional teaching and helping throughout the project time.
  - **[Manu Perez](https://github.com/Manuperezro)** : My supervisor at City of Bristol College for his patience, support and encouragement all the time.
  - **[Ussama Youssif](https://www.linkedin.com/in/ussama-youssif-59bb94105/?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=android_app)** : For his exceptional contribution and creative input in designing the logo for my project.
  - **[community-london in Slack and WhatsApp](https://app.slack.com/client/T0L30B202/CU0RJPEBF)**: for their continuous support and availability. Special thanks to [Erikas Ramanauskas](https://github.com/Erikas-Ramanauskas?tab=repositories) for his dedicated efforts in assisting with code-related issues
  - **[Student Care](https://learn.codeinstitute.net/ci_support/level5diplomainwebappdevelopment/studentcare)** :for their support.
  - **[Gareth-McGirr](https://github.com/Gareth-McGirr)** :a GitHub user whose Portfolio-Project-4-SizzleAndSteak project inspired me to create my README file.
