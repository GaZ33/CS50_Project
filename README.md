# SCHEDUALE ONLINE
#### Video Demo:
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
### DER
I would like to show my Schema, explain the tables, why and where I used them.
![image](https://github.com/user-attachments/assets/fea3cdf3-58e8-41fe-9863-8588e93178ce)




