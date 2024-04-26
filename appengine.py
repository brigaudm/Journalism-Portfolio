#server.py
from flask import Flask, redirect, request, render_template, url_for 
import sqlite3 

app = Flask(__name__)

@app.route("/")
def home_page():
    return render_template("index.html")

@app.route("/contact")
def contactForm():
    return render_template("contact.html", title = "contact me")

def create_db_connection(db_file):
    con = None
    try:
        con = sqlite3.connect(db_file)
        return con
    except sqlite3.Error as e:
        print(e)
    return con

def create_contact_table():
    con = create_db_connection("contact_form_data.db")
    cur = con.cursor()
    cur.execute('''CREATE TABLE IF NOT EXISTS contact_data (
              id INTEGER PRIMARY KEY AUTOINCREMENT,
              user_name TEXT,
              user_email TEXT,
              user_message TEXT
              )''')
    con.commit()
    con.close()
create_contact_table()

@app.route("/contact-storage", methods=['POST'])
def submit_contact_form():
    if request.method == 'POST':
        user_name = request.form['user_name']
        user_email = request.form['user_email']
        user_message = request.form['user_message']

        con = create_db_connection("contact_form_data.db")
        cur = con.cursor()
        cur.execute("INSERT INTO contact_data (user_name, user_email, user_message) VALUES (?, ?, ?)", (user_name, user_email, user_message))
        con.commit()
        con.close()

        return redirect(url_for("contact_sent"))
    return render_template("contact.html", title = "contact me")

@app.route("/sent!")
def contact_sent():
    return "Thank you! Your message has been sent." 

@app.route("/view_contact_data")
def view_contact_data():
    con = create_db_connection("contact_form_data.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM contact_data")
    data = cur.fetchall()

    con.close()
    return render_template("view_contact_data.html", data=data)

@app.route("/stories")
def display_articles():
    con = create_db_connection("all_my_articles.db")
    cur = con.cursor()
    cur.execute("SELECT Article, Publication, Date, Tags FROM articles_table ORDER BY date DESC")
    data = cur.fetchall()

    con.close()
    return render_template("stories.html", data=data, title="stories")


if __name__ == "__main__":
    app.run(debug=True, PORT=8080)

# app = Flask(__name__, static_folder = 'web')