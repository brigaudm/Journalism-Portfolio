# Journalism Portfolio
I made this dynamic web application to showcase my journalism experience. It uses Flask, Jinja, and SQLite. I've coded in Python, JavaScript, HTML, and CSS. I've also used the SQLite and Jinja documentation to create and populate data tables and create html templates. 

The app introduces me as a journalist, pulls data about my published articles from a data base, and allows people to contact me by pushing their name, email, and message to a database. 

I made this for my Fundamentals of Programming module at Cardiff University.

List of features:
- Nav bar at the top, with hyperlinks to my LinkedIn, Twitter/x, and two other pages of my website (stories and contact form) 
- Media queries change the nav bar and other features of the website to better suit small screens. 
- JavaScript carousel/slideshow of three featured articles. Buttons get darker when you hover over them
- List of all my published articles in chronological order (most recent to least recent), pulled from an SQLite data table. The list includes article name, publication, date, and tags to categorize the articles by. The row the mouse is hovering over lights up green for visibility/accessiblity purposes. 
- Contact form with a security features to 1. keep people from putting non-emails in the email box 2. not reveal the contents of the form in the URL (POST versus GET methods). 
- Contact data is pushed to an SQLite table and can be viewed at the route /view_contact_data

## Resources I used
### Journalist portfolio ideas came from journoportfolio.com
### html and css help: 
- FlexBox refresher: https://www.youtube.com/watch?v=aRMIdKRYg6c&list=PLoYCgNOIyGABDU532eesybur5HPBVfC1G&index=6 
- Table styling: https://www.w3schools.com/css/css_table.asp 
- For colors/fonts: https://www.rapidtables.com/convert/color/hex-to-rgb.html; https://wdexplorer.com/20-examples-beautiful-css-typography-design/; https://3.7designs.co/blog/10-examples-of-beautiful-css-typography-and-how-they-did-it/;
### JavaScript carousel/slideshow help: https://www.youtube.com/watch?v=9HcxHDS2w1s 
### Jinja documentation: https://jinja.palletsprojects.com/en/3.1.x/
### SQLite documentation: https://docs.python.org/3/library/sqlite3.html 
