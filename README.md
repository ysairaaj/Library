# Library
Library web-app using Django

This project uses Django to implement a Library webapp . This Web-App allows users to add new books , edit the books , and delete the books . This project also implements user authentication using inbuilt functionalities in Django . 

Salient features : 

1) Any user trying to use the Library web app will need to login first . I he does not have an account , he has to register (functionality is provided) . ![Login Page](login_page.png) ![Register Page](register_page.png) 
2) After Login , the person can view the homepage with list of all books . To view the details of a particular book , click on "Details" button provided .![Home Page](homepage.png) 
3) All the details of the book like preview image , publication date , ISBN , date of upload , name of uploader are available . ![Book detail](book_detail.png) 
4) Back button is also provided to go back to homepage .
5) Download button is provided to download the book .
6) Edit and Delete option is available to the user who has uploaded the file . Other users cannot edit or delete it (View of other user shown . Note that the option for edit and delete are not available) .  ![Book detail (view of other user)](book_detail_other_user.png) 
7) Form to add new book and logout button both are provided in navbar .
8) requirements.txt contains all the dependencies .
9) Note :- Virtual environment was used to create the project . It contains two apps namely :- accounts , Book .
10) New book form and Edit book form are shown below . ![new_book](new_book.png) ![New Book] ![Edit book](Edit_book.png) ![Edit book]
