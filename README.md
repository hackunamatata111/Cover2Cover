# Cover2Cover
This website is designed to connect students of a college who no longer need a book and students who are looking for a book.
This detailed readme will help to navigate through the code, understand it, and help to make further contributions.
# Contents
1)How to run the code?\
2)Basic structure and URL paths\
3)Database\
4)Forms\
5)Views\
6)Static and Templates
# 1)How to run the code?
1.1)Clone the GitHub repository.\
1.2)Make sure you have installed Python 3.10.0 and Django 4.0.1\
1.3)cd into the main repository in the terminal. When you run the ls command, if you see the file manege.py, you are at the correct location to run the next command.If you don't see, then use cd to reach the correct directory.\
1.4)Now if python 3.10.0 is the only version of python you have, then run the command "python manage.py runserver". If you have multiple versions of python, then run "python3 manage.py runserver"\
1.5)You would see something like this in terminal "Starting development server at (a url)". Copy that URL and run it in the browser(Chrome and Safari are strongly recommended).\
1.6)You can now access the website. Either sign up to make a new account or use email:nitheez@iiitb.ac.in password:dogcat123 to login(this is also the admin account). While signing up, if you use enter college as IIITB or IIMB, you will be able to see a few sample books that are posted beforehand.
# 2)Basic structure and URL paths
2.1)Basic structure

"bms" is the main project file that contains the settings.py. "take" is the core app of the whole website. "static" contains all the static files.  
2.2)URLs\
urls.py in bms directly points to urls.py inside the take directory. If you use /admin, you can access the Django admin panel.\
All the URLs in take/urls.py has been listed below.\
2.2.1)Unrestricted URLs:\
\
Landing page: ''\
Login page: login/\
Sign up page: register/\
\
2.2.2)URLs restricted to logged-in users(reason for restriction specified in parenthesis):\
\
Home page: home/(Has a welcome customized to user)\
Browse books page: takehome/(Only books available in the user's college has to be shown)\
Information of a particular Book page: info/'a string'/(for the same reason as above)\
Donating a book: post/(username, phone number, email of the donor is taken automatically from his profile)\
Redirecting after posting book:redirect/(follows after a restricted page post)\
Profile of user: profile/(profile is unique to each user)\
Update book information:updateBook/'a string'/(user should be able to update only their books)\
Delete book: deleteBook/'a string'/(user should be able to delete only their books)\
Logout:logout/(login required to logout)

# 3)Database
Three models are used in the project:\
3.1) The django inbuilt User model. It stores username(email) and password.\
3.2) "Profile" model, which is in a one to one relation with the User model. It stores username(email)(one to one key)-'user', name-'name',mobile number-'mob',college name-'cname'\
3.3) "Take" model, which stores details of the book posted. It has a foreign key pointing to the User model. It stores username(email)(foreign key)-'roll', Book name-'name', Book description-'description', Author name-'auth', email (can be null if the doner wishes)-' contact', Mobile Number (can be null if the doner wishes)-'mob', Time of posting(time), Course name-'course', College name-'cname'.

# 4)Forms
Two forms, namely BookForm and SignUpForm are present in take/forms.py\
4.1)BookForm: Used for both posing and editing book details. All the fields of "take" model are present except 'roll', 'cname', 'contact', 'mob', which are automatically filled from the "Profile" model of the logged-in user. 'mob' and 'contact' is filled only if the user checks the checkbox, else it's filled with None.\
4.2)SignUpForm: This contains all the fields needed to fill the User model and the Profile model. Note that 'password2' is confirm password.

# 5)Views
There are 14 views in total in the take/views.py\
In most cases, views have been given the same name as the corresponding URL that refers to it.\
The views are simple and easy to understand on glancing through the code. Since there are a lot of them, it is not going to be covered one by one in this readme.\
Note: decorator 'login_required' imported from django.contrib.auth.decorators has been used to restrict the pages that are meant for logged in users only.

# 6)Static and Templetes
Static files are stored in the directory 'static' present in the main directory. static/img contains images used throughout the website. Static/styles contains the css files.\
'templates' directory of the main directory contains navbar.html that is extended at all required pages using Django templating engine. All the other HTML files are stored in take/templetes/take.\
Templates use Bootstrap 5 and animate.css, given below are the GitHub repo for the same:\
https://github.com/twbs/bootstrap \
https://github.com/animate-css/animate.css

# Developed by Hackuna Matata
Front End Developers:\
Brij Desai\
Yukta Rajapur\
Backend End Developers:\
Nilay Kamat\
Nitheezkant R

Project report:\
Project Demo:

# The End

