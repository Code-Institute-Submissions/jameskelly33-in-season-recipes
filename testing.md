## **Testing**

### **Automated Testing**

The W3C Markup Validator and W3C CSS Validator Services were used to validate every page of the project to ensure there were no syntax errors in the project. The PEP8 onlince checker tool was used to check the python code is PEP8 compliant. JSlint was used to check the quality of the javascript code and Prettier was used to format code across the project. 

* [W3C Markup Validator](https://validator.w3.org/) 
* [W3C CSS Validator](https://jigsaw.w3.org/css-validator/)
* [JSLint](https://www.jslint.com/)
* [Prettier](https://prettier.io/)
* [Python PEP8 Validator](http://pep8online.com/)


## **Testing User Stories from User Experience (UX) Section**


As a user of this site, I want:

* Find out what ingredients are currently in season or perhaps coming into season in the following months.
 	- Users can click on the ‘What’s In Season Button’ on top of the hero image on the homepage and on the card panel in step 1 on the homepage to be taken to the ‘In Season” page which present ingredients that are in season in the current month and the ingredients that are in season in the next month. 

* Browse recipes that use these ingredients.
	- Once the users are on the ‘In Season” page each image of an ingredient has a button that when clicked will take the user to the recipe page with recipes filtered by that particular ingredient. So for example if the user clicks on apples, they will only see recipes that contain apples. 

* Find recipes using these ingredients that cover a wide range of cuisines or styles(starter, dessert, beginner, advanced etc).
	- The recipes page has a search bar in which the user can search by recipe name, ingredient, cuisine, dish category or general keyword that could be found in the recipe method. 

* Save recipes to a personal profile. 
	- Once a user has registered for an account  the my recipes section will appear on the nav bar and any full recipe page will now contain a button which will save the recipe to their favourite recipe collection, which can be accessed via the my recipes page. 


* Add their own recipes to the site. 
	- All logged on users can upload recipes to the site via the upload recipe form which can be reached via the My Recipes page. After users have successfully submitted the form the recipe will be added to the general recipe library, accessible to all site users. If a users wishes to edit or delete a recipe for some reason they are able to do that via the my recipes section of the my recipes page. 



## **Manual Testing Procedure**

All steps were taken on Google Chrome, Firefox, Safari and Internet Explorer on a Thunderbolt Display and MacBook Pro at two different desktop screen resolutions and subsequently an iPhone X screen, iPad 3, and iPhone 8.

## **Elements on each page**

**Navbar**

* Click on **In Season** to check it brings user to homepage.
* Click on **Home** to check it brings user to homepage.
* Click on **In Season Now** to check it brings user to the In Season Now page.
* Click on **Recipes** to check it brings user to the Recipes page.
* Click on **Log In** to check the log in page appears.
* Click on **Register** to check the register page appears.
* Hover over each inactive link to check hover effect is working on all nav items.
* Check the Navbar collapses at the correct breakpoint.
* Follow the steps above to check all links work correctly on the collapsible navbar. 
* Log in as an existing user to check that the **My Recipes** link appears.
* Click on the **My Recipes** link to check that it brings up the correct My Recipe profile page for the correct user. 
* Log in as an existing user to check that the **Log In** and **Register** links disappear and are replaced by Log out.
* Click on the **Log Out** link to check that the user has been successfully logged out the **My Recipes** link has disappeared and the **Log In** and **Register** links have reappeared. 

**Flash Messages**

* Log in as an existing user to see the flash message **Successfully logged in** appear below the navbar. 
* Attempt to log in with an incorrect email and / or password to see the flash message **Incorrect Email / Password** appear below the navbar. 
* Sign up as new user via the **Register** page and check to see the flash message **Successfully registered** appear.
* Attempt to sign up as a new user with an existing email address to see the flash message **Email already in use** appear. 
* Attempt to sign up a new user with two different inputs into the password and confirm password field to see the flash message “ Passwords do not match” appear.
* Upload a new recipe to the site via the **Upload Recipe* form to check that the flash message “Recipe Added” appears.
* Edit a previously uploaded recipe to the site via the **Edit Recipe** button in the **My Recipes** section of the site to check the flash message “Recipe Edited” appears.
* Delete a previously uploaded recipe to the site via the **Delete Recipe** button in the **My Recipes** section of the site to check the flash message “Recipe Deleted” appears. 
* Save a recipe via the **Save Recipe** button on a **Full Recipe** page to check the flash message “Recipe Saved” appears.
* Attempt to Save a recipe that has already been saved to a user’s favourite recipe collection via the **Save Recipe** button on a **Full Recipe** page to check the flash message “Recipe already saved” appears.
* Log out a user to check that the flash message “You have been logged out” appears. 


## **Homepage**

* Check that the correct image (tomatoes.jpg)is displayed on all screen resolutions above 992px.
* Check that the correct image (asparagus.jpg)is displayed on all screen resolutions below 992px.
* Check that the button colours match the hero image (orange for tomatoes.jpg and green for asparagus.jpg)
* Check the text is right-aligned and is displayed clearly on large screens
* Check the text is left-aligned and is displayed clearly on small and med screens.
* Hover over **What’s In Season** button to check hover effect works.
* Click on **What’s In Season** button to check it takes the user to the **In Season Now** page.
* Check that the 3 card panel below the hero-image is displayed horizontally on large screens and above.
* Check that the 3 card panel below the hero-image is displayed vertically on small and medium screens.
* Check that font awesome icons are displaying correctly
* Check that the three buttons are horizontally aligned when arrange vertically. 
* Hover over each button to check that hover effect is working.
* Click on **Ingredients** button to check that it takes user to the **In Season Now** page.
* Click on **Recipes** button to check that it takes user to the **Recipes** page.
* Click on **Join** button to check that it takes user to the **Register** page.

## **In Season Page**

* Check that the correct current month is being displayed in the top page heading.
* Check that the correct next month is being displayed in the second page heading. 
* Change the current month variable in the app.py file to check that every month’s ingredients are correctly displayed. 
* Check that the carousel is showing three slides on large(>=1000px) screens.
* Check that the carousel is showing two slides on medium(>=500px) screens.
* Check that the carousel is showing three slides on small screens(<500px) screens.
* Check that the navigation arrows and dots appear for each carousel.
* Click on the navigation arrows to check the carousel moves from slide to slide. 
* Drag the images to the left and right to check the carousel slides from one image to the next. 
* Check that the ingredient name, description and image match and click on the button to check that it correctly brings the user to the recipe page showing results which contain the selected ingredient.
  

## **Recipe Page**

* Check that all images are displayed and are of the same dimensions.
* Check that recipe name and recipe description are displayed and capitalised.
* Click on the **Get Full Recipe** button to check that the user is taken to the correct full recipe page. 
* Check that the column layout is displaying as intended, 3 recipes per row on larger screens, 2 recipes on medium screens, 1 per row on small screens.
* Check that the search bar is working by searching for a recipe name, ingredient, cuisine or recipe category.
* Check that the search bar doesn’t accept an empty search.
* Check that  a search for an ingredient, cuisine or recipe that does not exist in the recipe collection displays the correct no search result image and message. 


## **Full Recipe Page**

* Check that the correct image and recipe details are displayed. With the image arranged to the left of the screen on large screens and
* Check that if no user is currently logged in the button at the bottom of the page takes redirects users to the Log In page.
* Check that if a user is currently logged in the button at the bottom of the page successfully saves the recipe to the user’s saved recipes collection and a flash message appears reading ”Recipe Saved”. 

## **Log In Page**

* Check that the log in form does not submit with empty email or password inputs.
* Check that the log in form accepts a correct email and password combination and the user is redirected to the homepage and the **My Recipes** **Log Out** links are active on the nav bar.
* Check that a correct email but an incorrect password displays the flash message “Incorrect Email or Password” and resets the form. 
* Check that an incorrect email and a correct password displays the flash message “Incorrect Email or Password” and resets the form. 
* Check that the Register Here link redirects the user to the register page.

## **Register Page**

* Check that the register form does not submit with any of the inputs empty.
* Check that username input does not submit a username of fewer than 3 characters or more than 20 characters.
* Check that the email input does not submit an invalid email format.
* Check that an already existing email input displays the flash message “Email already in use”.
* Check that password and confirm password inputs do not submit a matching password that is fewer than 5 characters or more than 20 characters. 
* Check that a the “Passwords do not match” flash message appears when contrasting valid length passwords are inputted. 
* Check that a form submission matching all valid validation criteria redirects the user to the homepage and displays the flash message “Successfully Registered”.
* Check that  the **Log in here** link redirects a user to the log in page. 

## **My Recipes Page**

* Check that the current user’s username is correctly displayed in the heading. 
* Check that the current user’s favourite recipes are displayed and correctly link to the right full recipe for each recipe.
* Check that the ‘You haven’t saved any recipes yet” message is displayed for a user without any favourite recipes. 
* Check that the "Remove Saved Recipe" button sucessfully removes the recipe from user's collection and the correct flash message is displayed.
* Check that current user’s authored recipes are displayed and correctly link to the right full recipe for each recipe.
*  Check that the ‘You haven’t uploaded any recipes yet” message is displayed for a user without any authored recipes. 
* Check that the upload recipe button redirects the user to the Upload Recipe page. 
* Check the edit recipe buttons redirects the user to the Edit Recipe page.
* Check the delete recipe button deletes the chosen recipe and a flash message appears informing the user that the recipe has been deleted.

## **Upload Recipe Page**

* Check that the form does not submit with any empty required fields.
* Check that the form does not accept a recipe name greater than 50 characters.
* Check that the form does not accept a recipe description greater than 150 characters.
* Check that the form does not accept a cuisine input greater than 50 characters.
* Check that upon successfully submitting the form a flash message appears reading “Recipe Added” and the user is redirected back to the **My Recipes** page.  

## **Edit Recipe Page**

* Check that the form does not submit with any empty required fields.
* Check that the form does not accept a recipe name greater than 50 characters.
* Check that the form does not accept a recipe description greater than 150 characters.
* Check that the form does not accept a cuisine input greater than 50 characters.
* Check that upon successfully submitting the form a flash message appears reading “Recipe Updated” and the user is redirected back to the **My Recipes** page. 


#**Bugs**

**Recipe Already Saved**

* During testing I discovered that even if a user had no saved recipes when they attempted to save a recipe that had been saved by another user the **Recipe Already Saved** flash message would be displayed and the recipe wouldn’t be added to their collection. 


![Screenshot of Recipe Already Saved Error](/static/images/screenshots/alreadysaved.png "Recipe Already Saved Error")


The source of this issue was found in the save recipe function. 

```python
def saverecipe(recipe_id):
    
    if session['current_user']:
        email = mongo.db.users.find_one(
            {"email": session["current_user"]})['email']
        if mongo.db.users.find_one{'favourite_recipes' : recipe_id}):
            flash ('Recipe already saved')
            return redirect(url_for('myrecipes', email = email)) 
        else:    
            mongo.db.users.update({'email':email},{"$push": {"favourite_recipes":recipe_id}})
            flash ("Recipe saved!")
            return redirect(url_for('myrecipes', email = email))

```

The issue was being caused by the find_one query looking for one user that had the selected recipe in their favourite recipes. The function was therefore searching all users instead of looking for the current session user only and if the selected recipe had previously been saved by any other user it would end the function before the else statement. 

The fix to the problem was to replace the find_one query seen above with the following.

```python
if mongo.db.users.find_one({"email" : email,'favourite_recipes' : recipe_id}):
            flash ('Recipe already saved')
            return redirect(url_for('myrecipes', email = email))
```
The user can now save a recipe to their own collection regardless of whether the recipe has been saved by another user as the query targets the specific session users collection. 


**Edit Recipe Form Whitespace issues **

* This issue occurred during setting up the edit recipe form to include the pre-exsiting recipe information in the form’s text inputs, areas and select boxes. The Jijna template language was inserting white spaces in the two for loops of the recipe ingredients and method. The result can be seen in the following screenshot. 

![Screenshot of Whitespace error on edit recipe form](/static/images/screenshots/whitespace.png "Whitespace error on Edit Recipe form") 

The solution was found thanks to this article on Jinja Whitespace control https://ttl255.com/jinja2-tutorial-part-3-whitespace-control/
The first step was to enable trim blocks in the app.py file.
```python
app.jinja_env.trim_blocks = True
app.jinja_env.lstrip_blocks = True
```
And secondly in the two for loops by adding a minus sign to strip white space at the end of the for loop as seen below.

```html
<textarea class="form-control form-label-required" id="ingredients" name="ingredients" rows="10" placeholder= "Start a new line for each ingredient" required>
    {% for recipe_ingredient in recipe_info recipe_ingredients -%}
        {{recipe_ingredient}}
    {% endfor %}
</textarea>
```    

```html
<textarea class="form-control form-label-required" id="method" name="method" rows="10” placeholder="Start a new line for each step " required>
    {% for step in recipe_info.method -%}
       {{step}}
    {% endfor %}</textarea>
```

**Next Month Ingredients Carousel not showing**

* After writing the code for the In Season Ingredients page the second carousel showing the Coming Into Season ingredients was not displaying on the page. 

![Screenshot of missing carousel](/static/images/screenshots/missingcarousel.png "Missing Carousel") 


The root of this issue is the ingredients collection cursor object that results from the find call can not be looped over twice on the same page as  The solution was a simple one and was found with help from this answer from the Mongo DB community forums.
https://www.mongodb.com/community/forums/t/how-can-i-reload-the-for-loop-in-flask-jinja2/8359

By converting the result of the find call to a list, I was able to include more than one for loop on the data thus rendering the second carousel successfully . 

**Delete Recipe Function**

After implementing the delete recipe function, recipes were successfully being removed from the recipes collection, however the My Recipes page was still showing an empty recipe card where the recipes were previsouly being stored.

![Screenshot of emptyrecipe slot](/static/images/screenshots/emptyrecipe.png "Empty Recipe Slot Error") 

This was simply because the delete recipe function did not include any functionality for removing saved recipes from the favourite recipe array in the Users collection. The function was updated to include the following code to solve the issue. 
```python
mongo.db.users.update({'email':username},{"$pull": {"favourite_recipes":recipe}})
```


























