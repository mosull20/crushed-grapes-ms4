# Crushed Grapes

![Website mockup screenshot](media/all-devices-black.png)

View the live website [here](https://crushed-grapes.herokuapp.com/).
---
Crushed Grapes is an online wine store created for educational purposes only for the Code Institute Final Milestone Project. Users can browse through the selection of wines available, sort results and search the site for a particular item, select products to purchase, add them to their cart and finally use a secure checkout facilty to make their purchase, and receive email confirmation of their order. Registered users can further choose to add reviews to any products. Store Admin can add, edit and delete products from the database, and also add, edit or remove blog posts to/from the site. 

___ 
## Contents
* [UX](#UX)
* [Database](#database)
* [Features](#features)
* [Technologies Used](#technologies-used)
* [Testing](#testing)
* [Deployment](#deployment)
* [Credits](#credits)
___

## UX
### Project Goals

This site has been created to provide users with a fully functioning e-commerce website for those interested in shopping for, and purchasing, wine online.
While this site has been created for eductional purposes only, the aim has been to provide an intuitive, user friendly, easy to navigate website that is clear and easy to understand for each step of the browsing and purchasing process and providing feeback to users along the way, each time an action is performed. 


### User Stories
##### As a user I want to:
1. view what products are available on this website
2. see all the wine products available
3. see all the details on any particular product and read more info about the product
4. look at different categories of wine rather than having them all display, ie. browse all the red wines only
5. have the option to sort the products in a number of different ways - by price, rating, country and by name
6. search the site for a specific wine
7. easily identify any special offers
8. find out the delivery information ie. where the store delivers to and what the charges are
9. easily add any product to a shopping cart and have the cart hold these items while I continue to shop
10. view the contents of my shopping cart easily at any stage and see how much the running total is so I can keep track of how much I'm spending
11. easily checkout and complete my purchase by paying online securely
12. get an email confirmation of my order sent to me
13. read some interesting articles about wine and perhaps learn things I was not aware of
##### As a registered user I want to:
1. easily register for an account
2. receive an email confirmation when I register my account
3. have the site save my delivery info so I don't have to re-enter that each time I order
4. see my profile and be able to update my delivery details at any time
5. easily log in and see what I have purchased previously
6. easily log out
7. be able to reset my password if I forget it
##### As site owner/admin I want to:
1. easily add new products, make updates to existing products in the database and delete any product
2. encourage users to visit the site even if not planning a purchase
3. have all users confirm they are of legal age to drink alcohol (over 18) before making an order

[Back to Contents](#contents)
___

### Wireframes
View the wireframes [here](docs/ms4-wireframes.pdf)

[Back to Contents](#contents)
___

### Design
#### Overall Design, Images and Color Scheme
* The aim with the design of this project is to provide the user with a clear, easy to navigate, visually appealing website. I choose the overall colour scheme to tie in with shades of wine - blush and red in particular and ended up going with less vivid colors to create a sense of a calm and a relaxing shopping experience, while also ensuring the colour scheme keeps focusing on showcasing the products.

* I used Bootstrap for much of the site layout and it's components, modals, navbar, footer, and card layout for the products. I feel it gives the user a well structured, well laid out design that provides a good user experience. 

* The main background image on the home page gives a nice simple introduction to the website, without taking centre stage. 

#### Typography
* I choose the Oswald font for the bulk of the website typography to provide a sense of sophistciation, with the Shadows into Light font for the logo and home page content and blog page content to create contrast using a more whimsical style.

[Back to Contents](#contents)
___
## Database

Two relational databases were used in the creation of this project - during development SQLite was used and then Postgres was used for the deployed Heroku version. 


[Back to Contents](#contents)
___

## Features
### Existing Features

* Across the site:
    + Navigation bar with logo (linked back to home page), links to home page, wines (subdivided into categories or all wines), FAQ's/Delivery info page, Blog posts page. 
    + Search bar at top of nav bar
    + Account link to create and account, login or if logged in - links to my profile page, and logout. As an admin, additional options are shown here to manage products and manage blog
    + Shopping cart link
    + Footer containing links to social media sites and link to Delivery Info/FAq's page

* Home page 
    + Short intro to the site with a button to shop all wines

* Products & Product Detail pages
    + Page showing range of products, can display all products or each category by itself. Products are displayed in Bootstrap card format and contain an overview, with the option for user to click a link for more details. This then displays full product information with links to add item to cart, choose quantity or continue shopping. If there are any reviews for that wine, these are also displayed on this page underneath the main card display.

* Blog Page
    + Page showing short description of any blog posts that are available to look at. Clicking on the read post link will open that particular blog post in a new page. 

* Profile/Account page
    + Logged in users can access their profile page here with any personal/delivery details that have been used before and saved, any previous orders will be shown in summary form here and clicking on the order number will show the full details from the order confirmation for that order. Also shown here is any reviews the user may have uploaded and allow them to edit or delete them from here. 

* Shopping cart page
    + Displays all items with price, image, product info details and subtotal, delivery costs etc and a link to secure checkout. 
    + Users can amend quantity or remove any products they do not want to include in their order from here.

* Checkout page
    + User can enter all their details here - delivery details and payment details with the option to save these for future checkouts. 
    + User can complete a purchase without needing to be a registered user
    + User will be updated that payment is processing and will recieve a success message displayed on top right as well as being redirected to a checkout success page which shows a confirmation of their order, details entered etc. and lets the user know a confirmation email will be sent to the email address the user provided.

* Register/Create Account page
    + Allows user to create a new account for this site with email verification for enhance security. 

* Sign In page
    + Allows already registered user to log in to their account

* Add review page   
    + Allows registered users to add a review to any wine using a simple form. If not logged in, it will redirect user to sign in page.

* Admin additional features
    + Admin can add, edit or delete products and manage the store effectively and easily.
    + Admin can add, edit or delete a blog post
    + Admin can add, edit or delete a review, including those uploaded by any registered user 
    
### Features to implement in the future

There are a number of features that I would like to implement in the future to enhance the website both for the site owner and the user experience. 
* A special offers section for wines that are on sale and have a monthly offers section such as buy 6 bottles for the price of 5 etc. or free glasses with a purchase over a certain amount etc. Having a new offer on a monthly basis would enhance user experience and encourage repeat visits to the site and create more business on the site.
* Age Verification - an important feature for the site owner to have would be to add an age verification check to have the user confirm they are over 18 which is the legal age to purchase alcohol in Ireland
* Add the ability for registered users to upload blog posts they have written to feature on the site. Currently, only the admin can upload a new blog post. This would add to the user experience and have them more engaged with the content on the site. 
* I would also like to add the ability for registered users to leave comments on any blog post.
* Outside the time contraints of the course, I would also like to implement custom error pages. 
* Further security features would be important to ensure the integrity of the site in a real world application.



[Back to Contents](#contents)
___

## Technologies Used
#### Languages

* [HTML](https://en.wikipedia.org/wiki/HTML)
* [CSS](https://en.wikipedia.org/wiki/CSS)
* [JavaScript](https://en.wikipedia.org/wiki/JavaScript)
* [Python3](https://en.wikipedia.org/wiki/Python_(programming_language))

#### Programs, Frameworks, Libraries, Resources

* [Django](https://www.djangoproject.com/) High Level Python Framework
* [GitHub](https://github.com/) Code hosting platform
* [Gitpod](https://www.gitpod.io/) IDE used for writing and editing code, version control
* [Heroku](https://en.wikipedia.org/wiki/Heroku) Cloud platform
* [jQuery](https://jquery.com/) JavaScript Library
* [Bootstrap](https://getbootstrap.com/) Front end framework
* [SQLite3](https://www.sqlite.org/index.html) SQL database engine used for Development database
* [PostgreSQL](https://www.postgresql.org/) Relational Database system used for Deployed database
* [Stripe](https://stripe.com/ie) Online payment processing infrastructure
* [AWS](https://aws.amazon.com/) S3 - Storage service for hosting static files and images
* [Google Fonts](https://fonts.google.com/) Font library
* [Font awesome](https://fontawesome.com/) Icons
* [Pixlr](https://pixlr.com/e/) Image Editor used for main background image optimisation
* [TinyPNG](https://tinypng.com/) Image compressor
* [Balsamiq](https://balsamiq.com/wireframes/) Wireframe software
* [dbdiagram.io](https://dbdiagram.io/home) Database diagram design software
* [coolers.co](https://coolors.co/) Color scheme generator
* [Randomkeygen.com](https://randomkeygen.com/) Secure password/secret key generator
* [Favicon.io](https://favicon.io/favicon-converter/) Favicon generator
* [Website Mockup Generator](https://websitemockupgenerator.com/) used to generate responsive screenshot
* [Autoprefixer.io](https://autoprefixer.github.io/) used to add vendor prefixes for the major browsers

[Back to Contents](#contents)
___
## Testing
Testing is detailed in a seperate document [here](TESTING.md).

[Back to Contents](#contents)
___
## Deployment

This project was developed using the Gitpod IDE and pushed to a Github repository with the use of Git version control. The project was then deployed using Heroku.

### To deploy to Heroku, the following steps were taken:

1. In advance of deployment, Heroku needs the requirements for the project. In Gitpod, create a requirements.txt file using the `pip3 freeze --local > requirements.txt`. Then a Procfile needs to be created with the follwing code and no balnk like follwing it `web: gunicorn crushed_grapes.wsgi:application`. Push these files to your Github Repo.

2. Go to the [Heroku Website](https://id.heroku.com/login) and log in.

3. In the dashboard, select "Create New App".

4. Choose a unique app name and select the region appropriate to your location and click on 'Create App'.

5. When the app has been created, click on the "Resources" tab to provision a new Postgres database, using the free plan.

6. To use Postgres, return to your IDE and install `dj_database_url` and `psycopg2-binary` using the `pip3 install` command, making sure to add these to your requirements.txt file.

7. In `settings.py` comment out the default database setting and add the following code - 
`DATABASES = {'default' = dj_database_url.parse('database url')` - the database url can be found by going to the Heroku dashboard under the Settings tab, click on 'Reveal Config Vars', and copy the value next to 'DATABASE_URL'

8. Next, migrations need to be run again as we are now connecting to Postgres so run migrations using the `python3 manage.py migrate` command in the terminal.

9. To import all product data using fixtures we can load the categories data first, followed by the products data using the command `python3 manage.py loaddata categories` and `python3 manage.py loaddata products`.

10. Next, create a superuser for login with Heroku using `python3 manage.py createsuperuser`.

11. Before commiting to GitHub, the Database settings need to be changed in `settings.py` so that when the app is running on Heroku, it will connect to the Postgres database, otherwise, it will connect to the default SQLite DB, and ensuring the database url entered above in step 7 is removed and replaced with `parse(os.environ.get('DATABASE_URL'))`

12. Add the host name of the Heroku app into "Allowed Hosts' in settings.py file

13. To enable automatic deployment, in the Heroku dashboard, go to the 'Deployment' tab, set the deployment to 'Github' and search for your repository. Click 'Connect' then 'Enable Automatic Deployments'

### Environment Variables 

1. Set the environment variables in Heroku under 'Settings' and 'Reveal Config Vars' 

| Key       | Value        | 
| --------- |:------------:| 
| AWS_ACCESS_KEY_ID  | aws-access-key |
| AWS_SECRET_ACCESS_KEY  | aws-secret-access-key | 
| DATABASE_URL |   database-url-postgres   | 
| EMAIL_HOST_PASS | email-key |
| EMAIL_HOST_USER | host-email |
| SECRET_KEY | secret-key |
| STRIPE_PUBLIC_KEY | Stripe-public-key |
| STRIPE_SECRET_KEY | Stripe-secret-key |
| STRIPE_WH_SECRET |Stripe-webhook-secret-key |
| USE_AWS | True |


### Setting up AWS

1. Go to [AWS](https://aws.amazon.com/) and create an account, sign in, and search for S3. 
2. Open S3 and click on "Create Bucket" which will be used to store static files and images.
3. Set the bucket name to match the name of your heroku app and select region closest to you. 
4. Ensure you select the followig settings - 
    + Uncheck 'Block Public Access settings for this bucket' and acknowledge any warnings as the bucket needs to be public in order to allow public access to our static files.
    + Object Ownership - ensure 'ACL's enabled' is checked along with 'Bucket Owner preferred'
    + Properties tab, turn on static website hosting
    + Permissions tab - paste in the following CORS configuration - 
```
        [
            {
            "AllowedHeaders": [
            "Authorization"
            ],
            "AllowedMethods": [
            "GET"
            ],
            "AllowedOrigins": [
            "*"
            ],
            "ExposeHeaders": []
            }
        ]
```
5. Navigate to the 'Bucket Policy' Section and select policy generator. 
    + The policy type will be an S3 bucket policy. 
    + Allow all principles using '*'
    + Action will be 'Get Object'
    + Copy the ARN from the bucket policy editor tab and paste in to ARN box
    + Click on 'Add Statement' and then 'Generate Policy'
    + Copy this policy into the bucket policy editor and before saving add '/*' onto the end of the resource key to allow full access to all resources in this bucket.

6. Go to the Access Control List section, click 'Edit' and enable 'List for Everyone (public access)' and accept the warning box and save.

7. Next search for IAM (Identity and Access Management) in the main search bar in AWS. 
    + Under 'Access Management' click on 'User Groups' to create a new group.
    + Give the group a name and click 'Create Group'
    + Under 'Access Management' click on 'Policies' and then 'Create Policy'.
    + Click on 'JSON' tab and select 'Import Managed Policy', search for S3 and import the full S3 access policy, then paste in the bucket ARN from the bucket policy page in S3 in the "Resource" section as below - 
```
 "Resource": [
     "your ARN",
     "your ARN/*"
 ]
```

8. Click 'Next' to go through to the nextpage and on to the 'Review Policy' tab and 'Create Policy'.

9. To attach the policy, click on "User Groups", select your group, go to the 'Permissions' tab, open the 'Add Permisssions dropdown, and click 'Attach policies'. Select the policy and click 'Add permissions' at the bottom.

10. Next, create a user: In the IAM dashboard, click on 'Users' and then 'Add User'. 
    + Set the user name, then select 'Programmatic access' under 'Access Type' and select 'Next'.
    + Select the group to add the user to, then click next, through to the end and click 'Create User'. 

11. Download the CSV file which will contain the user's access keys.


### Connecting Django to AWS

1. Install `boto3` and `django-storages` and add to requirements.txt
2. Add 'storages' to installed apps in settings.py
3. Add the following settings in settings.py
```
if 'USE_AWS' in os.environ:
    # Bucket Config
    AWS_STORAGE_BUCKET_NAME = 'your-bucket-name'
    AWS_S3_REGION_NAME = 'your-region'
    AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
    AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
    AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'

    # Static and media files
    STATICFILES_STORAGE = 'custom_storages.StaticStorage'
    STATICFILES_LOCATION = 'static'
    DEFAULT_FILE_STORAGE = 'custom_storages.MediaStorage'
    MEDIAFILES_LOCATION = 'media'

    # Override static and media URLs in production
    STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{STATICFILES_LOCATION}/'
    MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{MEDIAFILES_LOCATION}/'
    
```

### To Clone or Fork this project

To clone or fork this project you will need a [Github](https://github.com/) account.

To Fork this project:

1. Open the [Project repository homepage](https://github.com/mosull20/crushed-grapes-ms4).
2. At the top right of the repository page, above the settings button, click on the **Fork** button.
3. This will create a copy of this project in your own GitHub account.

To Clone this project:
1. Open the [Project repository homepage](https://github.com/mosull20/crushed-grapes-ms4).
2. Click on the **Code** button at the top right of the file list.
3. Under **Clone** with the HTTPS option selected, copy the url link.
4. In your local IDE, open the terminal.
5. Change the current working directory to the location where you want the cloned directory.
6. Type in `git clone` and then paste the url you copied in step 3.
7. Press enter and your local clone will be created.



## Credits
### Content

All product images and detail content for the products database has been taken from external sources. I used 2 primary sources - 
1. [O'Brien's wine](https://www.obrienswine.ie/) website. Some images and almost all content on individual wines is from here. 
2. The second primary source was used mostly for images with some content also - [Vivino.com](https://www.vivino.com/IE/en/)

I also used a small number of images & product detail from [SuperValu.ie](https://shop.supervalu.ie/shopping/specialoffers/wine-beer-spirits/150200590) & [Tesco.ie](https://www.tesco.ie/groceries/product/browse/default.aspx?N=4294953032&Ne=4294954028)

Blog Post on Food Pairing - content taken from [The Wine Cellar Group](https://www.thewinecellargroup.com/wine-pairing-tips-for-beginners/)

Blog Post on how to choose wine - content taken from [GQ](https://www.gq.com/story/how-to-choose-wine-like-a-pro-in-any-situation)

### Code

Much of the code used for this was based around the Code Institute Boutique Ado walkthrough project, I relied heavily on this for the basic structure of the site. I have adapted it where possible or where needed for my own vision for this site along with adding custom models for reviews and blog page. 

Any small snippets used have been credited within the code where used. 

### Media
#### Images

Product images as credited above.

Image of wine bottle and glass used for logo from [kindpng.com](https://www.kindpng.com/imgv/TiRhmwo_wine-wine-bottle-and-glass-clipart-hd-png/)

Imge used on home page background: Photo by <a href="https://unsplash.com/@kymellis?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Kym Ellis</a> on <a href="https://unsplash.com/@msull21/likes?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Unsplash</a>

Image of wine & cheese on Food Pairing blog: Photo by <a href="https://unsplash.com/@sugercoatit?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Melissa Walker Horn</a> on <a href="https://unsplash.com/@msull21/likes?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Unsplash</a>

Image on how to choose wine blog post: Photo by <a href="https://unsplash.com/@chuttersnap?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">CHUTTERSNAP</a> on <a href="https://unsplash.com/s/photos/bottles-of-wine?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Unsplash</a>

Image on Blog Test 4 blog post: Photo by <a href="https://unsplash.com/@kelsoknight?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Kelsey Knight</a> on <a href="https://unsplash.com/@msull21/likes?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Unsplash</a>

Default image for blog posts if none uploaded: Photo by <a href="https://unsplash.com/@apolophotographer?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Apolo Photographer</a> on <a href="https://unsplash.com/@msull21/likes?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Unsplash</a>
  

### Acknowledgements

* The Code Institute Slack community has been the most valuable resource for any questions, problems and general support and I would like to thank the community of fellow students and alumni across the Slack channels for all the information that helped me throughout this and previous projects. 

* Stack Oveflow is another most valuable source of helpful guidance and problem solving.

* My mentor, Nishant Kumar, has been so supportive every step of the way and encouraged me to challenge myself a little bit more with each project.

* Tutor Support on Code Institute has also been a great resource throughout. 

[Back to Contents](#contents)