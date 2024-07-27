# ONLINE SCHEDUALE 
#### Video Demo: https://www.youtube.com/watch?v=z3ZOy2TB6YA
#### Description:
## The purpose of the project
My father works as an instructor of a driving school company, so, I created this website thiking in an online booking system. Where the user can scheduale or delete their classes through the website, and the instructor can delete classes and restrict some times. To improve the company and the rate of customers passing the driving test, I created a specific schema on my database to analyse what can be improve.
## About the project
This project is a booking system with login, register, database, cryptography, users type and forms system. I used those libraries:
- Flask: The main library to run the aplication.
- Flask_login: The extension of flask to management the users sessions.
- Flask_wtf: The extension of flask to create forms on html pages, and recive the data on the routes.
- Bcrypt: The library to cryptography users's passwords and check them when the user log in.
- SQLAlchemy: The library to management the database and the connection with my database on MySQL.
- Os and dotenv: Those libraries I used to get the connection with my database and the secret key that are in another folder.
- Datetime: The library that did the logic of days and time of the scheduale.
## Files
In my main folder of this project, I have those files and folders:
![image](https://github.com/user-attachments/assets/6a85a5dd-5ffe-4348-a084-bf392672638d)
- _pyache_: It's a folder that save some compiller files
- app: It's a folder with my whole application, like code, imgs, html files and css file.
- .replit: It's a file to run the application on replit website
- changelog: In this file, I saved my history of changes of my project. Everyday that I coded, I put in this files the changes. You can see the progress of the project there.
- DER: It's a file of schema from my database. DER is a portuguese term for Diagrama Entidade-Relacionamento, in english is ERD: Entity-Relationship Diagram.
- LICENSE: It's a MIT license
- requirements: Another file to run the application on replit website
- run: It's a file to run the application.
- SQL_commands: it's a file that I've used to write my databse on MySQL
### app
In app file I have those files and folders:
![image](https://github.com/user-attachments/assets/1ca7e330-eeef-492c-b4ca-7ab5bcd5a952)
- static: A folder that saves css files and images. This file need, even the name needs the same, to exist, because the Flask just interprets css files and images through this folder.
- templates: A folder thayt saves html files. There's the same purpose of the static folder.
- __init__: It's a file to import every libraries that I used in the project and setting some core objects for application run.
- forms: It's a file that management every form on my project. I used those forms to get the input of users.
- models: It's a file that management every object that connect with my database. I can get information from my databse through those models.
- routes: It's a file that contains every routes
### DER - ERD
I would like to show my Schema, explain the tables, why and where I used them.

![image](https://github.com/user-attachments/assets/fea3cdf3-58e8-41fe-9863-8588e93178ce)

Each table which is inside of yellow box, it's a table created thinking in analysis, contact and control metrics for the company.  And each table wich is inside of red box, it's a table created for some module or a funciton to work.
#### Account table
This table is used for management of user's login. It's needed a Username, that is unique, and a password, this password is provided by the user and is stored encrypted.
#### Classes table
This table is used for management of scheduale, it has a relationship to link the user to the instructor. So, it can then displayed on the scheduale page, so that users can see what time they can scheduale on the instructor's scheduale.
This table can also be used to manage an instructor's scheduale. Each class will be stored in this table, so, you can see how many classes that instructor has taken in given period.
#### Employees table
It's a table to store the information from the instructor. This exist for the same reason of Account and information table.
The instructor log in through this table, so, there is a Username column, which is unique, and a password column, which is encrypted.
#### Information table
It's a table to store the information from the user, through this table the company can perform some analysis and maintain contact with users.
#### Performance table
This table stores the user's progress , and can be used to monitor some metrics and improve user's skills before the driving test.
### HTML files
Each HTML file there is a main pupose. Each functionality of application is inside a file. The application have those HTML files:
- layout: In this file there are header, footer, links and head tags which I use on html files below. This file is the main template.
- index: It's the home page file, it will be the first page when new users enters
- register: This file is used to register new users, there is a form with many required inputs
- login: In this file, users can log in to their accounts
- Profile: It's a file for users can change some information about them
- Scheduale: Through this file, users can scheduale times for their classes
- loginemployee: In this file, Employees can log in to their accounts
- Schedualeemployee: In this file, Employees can see their classes and manage them



