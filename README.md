# Milestone Project 3 – In Season

# **In Season Recipe Website**

![A mock-up of the website on different devices](# "Mock Up of the site")


## **Project Goals**

The primary goal of this site is to provide users with a space to find and share recipes for dishes that use ingredients that are currently in season in Ireland. Using information from the Bord Bia(Irish food Board) users can find out what produce is in season or coming into season soon and search a database of recipes or add their own recipes for certain seasonal ingredients. 

## **UX**

### *User goals*

The central audience for this site is people in Ireland who like to cook and  have an interest in cooking with seasonal and locally sourced ingredients to cover a wide range of cuisines. 

### **Site user goals**

Users to this site would like to:

 * Find out what ingredients are currently in season or perhaps coming into season in the following months.

* Browse recipes that use these ingredients.

* Find recipes using these ingredients that cover a wide range of cuisines or styles(starter, dessert, beginner, advanced etc)

* Save recipes to a personal profile. 

* Rate and/or recommend existing recipes.

* Add their own recipes to the site. 

In Season will meet these goals by:

* Allowing users to automatically see what ingredients are in season in the current date, as well as search for what is in season in future months.

* Giving users the opportunity to search or browse a collection of recipes by ingredient. 

* Allowing users to search for a recipe by cuisine or other keyword.

* Providing users the ability to register a profile and add recipes to their personal to-cook-list. 

* Allowing users who are logged-in to rate dishes out of 5 stars.

* Allowing users to upload their own recipes to the site’s database. 

## **Wireframes**

[Wireframes](#)

Homepage

In Season Now page

Recipes Page

My Profile Page

Register Page

Log In Page

My Profile Page

Upload Recipe Page

### **User Story**

As a visitor to In Season , I want/need:

1. An uncomplicated user interface which allows quick access what ingredients are currently in season.
2. The ability to browse  and navigate the site on a variety of devices sizes.
3. Information about seasonal ingredients to be presented in a clear and visually attractive way that will make me excited to cook with them.
4.  A quick and simple way to navigate from my chosen ingredients to recipes that use those ingredients.
5. Recipes to be presented in an easy-to-follow layout with a visual representation of the final dish.
6. All recipes to follow a consistent easy-to-follow layout throughout the site. 
7. To find recipes that cover a wide range of cuisines (Irish, French, Thai etc) as well dish type(appetiser, main, dessert etc)or match my dietary requirements (vegan, gluten free etc)

As a regular visitor to In Season, I want/need:

1. The ability to register a personal account with the site and be able to easily log-in and log-out of the site.
2. To save my favourite recipes to my user profile allowing for quick access to them in the future. 
3. To see what other site users think of certain recipes.
4. To rate and comment about recipes which I have made.
5. To upload my own recipes for particular ingredients in a quick and user-friendly way using a form to help speed-up the process. 


**Design Choices**


	
* **Font**
There is only one font used throughout the website, which is Lora- a contemporary serif font with moderate contrast. This font was chosen primarily for its suitability to stand out equally well in the body text of the recipes and the headings found throughout the site.  
* **Colours**
As the site will feature a host of images of different ingredients and recipes the majority of pages’ content will be inherently  colourful. As a result I have chosen to keep custom colours on the site to a minimum to let the images stand out. Depending on the size of screen., the homepage will either show an image of fresh tomatoes or asparagus, I used the Color Palette Picker Chrome extension to match the colour of the displayed ingredient to the buttons on the homepage.

On all other pages throughout the site the buttons and card headers for login/register forms use the green asparagus colour. 

## **Features**

### **Existing Features**

### **On Every Page**

**Navigation**

On every page there is a standard, collapsible nav bar built using Bootstrap 5 classes that shows the website’s name in the top left, followed by links for the Homepage, In Season page, and recipe library. On the right are options to log in / register.


If the user is logged in then a My Recipes link is activated and a log out link is found on the top right. 


### **Homepage**

![A screenshot of the homepage](# "Screenshot of the homepage")

**Hero-Image**

On large screens (above width 992px) an image of a basket of cherry tomatoes and some basil is shown with the cover text aligned to the top right against the white backdrop of the image.
On screens below 992px, an image of a bunch of asparagus is shown with the cover text appearing against the white backdrop of the image in the top left of the screen. 
The decision to use multiple images was guided firstly by the fact that this website is all about showcasing a variety of ingredients and a slightly varied visual experience is a good way to emphasise that fact. 

** Call to action button**

As stated previously in the Colours Section, I decided to match the colour of the call to action button with the main ingredient shown in the image to help with the pages visual consistency . Clicking on this buttons will take users to the next page which shows what ingredients are currently in season in Ireland.


**Card Panels**

Below the hero image are three cards guiding the user through the process of using the website.
1. Step 1 - Find what ingredients are in season.
This button will take users to the next page which shows what ingredients are currently in season in Ireland.
2. Step 2 - Find recipes which use those ingredients.
This button will take users to the recipe library page in which they can search for recipes.

3. Step 3 – Join our community.
This button launches the register page in which users can sign up to the site and start to save and upload recipes. 

### **In Season Page**

![A screenshot of the in season page](# "Screenshot of the In Season Page")

**Carousels**

This page shows the users two multi-slide carousels implemented through the JQuery plugin Owl Carousel. At the top the user can see In Season in {current month} and at the bottom the user can see can Coming into Season {next month}.
On large screens the user should see three slides per row, medium screens two and small screens only one slide is shown at a time. The user can scroll through the carousels to see the ingredients or wait to see them automatically rendered.
Each ingredient image has a button below which when clicked will take the user to recipe section showing every recipe that uses that ingredient. 

### **Recipes Page**
![A screenshot of the recipes page](# "Screenshot of the Recipes Page")


This page shows the full library of recipes available on the site. There is a search bar through which the user can search for the name of a recipe, a single ingredient or cuisine type or category(e.g. Italian, dessert etc. Each recipe appears on a bootstrap card with a recipe image, recipe name and short description and a button leading to a full-page version of that particular recipe. The page has a responsive design therefore on larger screens(>=992px) and above the recipes are displayed three per row and 2 per row on medium screens(>=768px) and one per row on small screens(>=320px). 

If a user selects one of the ‘In Season’ ingredients from the In Season page it will redirect them to this page but with only recipes containing that particular ingredient. 

GIF OF SELECTION
### **Full Recipe Page**
![A screenshot of the full recipe page](# "Screenshot of the Full Recipe Page")

Once a user has selected the Get Full Recipe button from the recipes page it will take them to the full version of the recipe as seen above. The recipe name, description and image are all shown, along with the ingredients in a unordered list and a ordered list of the recipe method. On large screens and above the ingredients appear to the right of the image and method below, whereas for all other screens the information flow is vertically aligned. 

If the user is logged in there will be a button below the method labelled ‘Save Recipe’. Upon clicking this a user will save the recipe to their favourite recipes and a flash message will appear confirming the recipe has been saved. If the recipe is already in the user’s collection then a flash message will be appear notifying them that the recipe is already saved in their favourite recipes. 

If the site user is not logged in then the button appearing below the recipe method will read “Log In to Save Recipe”, which will lead the user to the login page. 
The user who submitted the recipe will be given credit below the ‘Save Recipe’ button. 


### **My Recipes Page**
![A screenshot of the my recipes page](# "Screenshot of the My Recipes Page")

When a user has successfully logged on to the site they will be able to navigate to the My Recipes section of the site which is divided into two parts.
1. Favourite Recipes
This section shows any recipe the user has saved to their favourites by clicking the ‘Save Recipe’ button on the full recipe page. If there are no recipes saved this section will display text saying ‘You haven’t saved any recipes yet”. The layout for this section is exactly the same as the main recipes page in showing rows of Bootstrap cards with recipe image, name, ,description and ‘Get Full Recipe Button”.

2. My Recipes
This section shows any recipes the current user has uploaded to the site. The layout is the same as the section above however as these are user-generated recipes there are two extra buttons on each recipe card. 
The edit recipe button allows a user to edit a recipe that they previously uploaded. Upon clicking the button the user is taken to edit recipe page seen below.

INSERT SCREENSHOT OF EDIT RECIPE

The form appears with the current information stored about the recipe and the user can change any field and re-submit the updated recipe to the site. 

Note that user-generated recipes use an image of their seasonal ingredient as their recipe image so a user is currently unable to upload their own recipe as this would require image hosting which is somewhat beyond the scope of this education project but could be implemented in the future.

The third button on the my recipe page is ‘Delete Recipe’ which gives the user the ability to remove their recipe from the site completely. Upon clicking this button a flash message will appear confirming the recipe’s deletion. 

At the bottom of the My Recipes page is the ‘Upload Recipe” button 

### **Upload Recipe Page**
![A screenshot of the upload recipe page](# "Screenshot of the Upload Recipe Page Page")

The upload recipe page consists of a Bootstrap form in which users can input a recipe’s name and short description. There is a select box which the user can pick one Seasonal Ingredient which is included in the recipe which allows the recipe to be linked to a particular ingredient. 

The ingredients text area input is next and the placeholder text gives the user the instruction to start a new line for each ingredient. As the python code will split this input’s value at each new line this is important as ingredients are stored in the database as an array. 
The recipe method has a similar placeholder for the same reason as above. 
Below the method text area is a dish category select box which has three choices of starter, main or dessert. This is followed by a text input in which the user can enter a type of cuisine that best represents the recipe, the placeholder reads “e.g. French Irish, Italian”.
At the bottom of the form is a submit button labelled ”Upload Recipe” which will validate and submit the completed form and a flash message will appear confirming the upload and the user will be redirected to the My

### **Log In Page**
![A screenshot of the log in page](# "Screenshot of the Log In Page")

The log in page is a bootstrap card with a header and footer and two input fields of email and password. The card header’s background colour matches the green shade used throughout the site for all buttons and there is a link to register in the card footer if the user does not already have an account. If the user enters and incorrect email or password then a flash message appears indicating an error was made with either email/ password. 
After successfully logging in a flash message appears confirming the user is logged in and they are taken to homepage and the added ‘My Recipes’ and ‘ Log Out’ links are activated on the nav bar. 

### **Register Page**
![A screenshot of the register page](# "Screenshot of the Register Page")

The register page is a bootstrap card with a header and footer and four input fields of username, email, password and confirm password. The card header’s background colour matches the green shade used throughout the site for all buttons and there is a link to log in in the card footer if the user already has an account. 
The form uses standard HTML validation and will not submit unless the following validation checks pass.

***Username*** – Min length 3 characters Max length 12. (Users are allowed duplicate usernames as this is not used to log in and only to appear in messages and submission posts. )
***Email*** – Must not already be in use on the site. If a user tries to register with a pre-existing email a flash message will be displayed telling the user that the email is already in use. 
***Password*** – Min length 5 characters Max length 20 characters. Password must match the input of confirm password otherwise a flash message will appear alerting the user that there was a discrepancy between the two input values. 
After successfully registering  a flash message appears confirming the user has registered and they are taken to homepage and the added ‘My Recipes’ and ‘ Log Out’ links are activated on the nav bar. 






## **Information Architecture**

**Database**

This project uses MongoDB ,which is a noSQL, document oriented database, and the data for this project is separated into four collections, users, recipes, ingredients and months.
The information architecture was designed from the standpoint of a user’s first visit to site, following the steps outlined on the homepage, connecting the current month to ingredients that in are in season and then ingredients to recipes which contain those seasonal ingredients. Meanwhile the users collection not only holds log in details but also a user’s favourite recipes. 

**Users Collection**

| Title | Key in db | form validation type | Data type |
--- | --- | --- | --- 
Account ID | _id | None | ObjectId 
Name | username | text, `minlength="3"` `maxlength="15"`| string
Email Address | email | email, `maxlength="50"` | string
Password | password | text, `minlength=”5” maxlength="15"` | string
Favourite Recipes | favourite_recipes | None | list


**Months Collection**
| Title | Key in db | form validation type | Data type |
--- | --- | --- | --- 
Month | January | None | list
Month | February | None | list
…
Month | December | None | list



**Ingredients Collection**
| Title | Key in db | form validation type | Data type |
--- | --- | --- | --- 
Ingredient ID | _id | None | ObjectId
Ingredient Name | ingredient_name | None | string
Ingredient Description | ingredient_description | None | string
Ingredient Image | ingredient_image | None | string (representing a static url in the project folder)



**Recipes Collection**
| Title | Key in db | form validation type | Data type |
--- | --- | --- | --- 
Recipe ID | _id | None | ObjectId
Recipe Name | recipe_name | text, `max-length = "50"`| string
Recipe Description | recipe_description | text, `max-length = “150”` 
Recipe Ingredients | recipe_ingredients | None | string
Method | method | None | string
Recipe Image | recipe_image | None | string (representing a static url in the project folder)
Recipe Author | recipe_author | None | string (representing a user’s email)
Recipe Category | recipe_category | Select | string
Seasonal Ingredient | seasonal_ingredient |Select | string
Cuisine | cuisine | text, `max-length = "50"` | string
