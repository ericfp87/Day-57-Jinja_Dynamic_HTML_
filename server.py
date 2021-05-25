from flask import Flask, render_template
import random
import datetime
import requests

app = Flask(__name__)


@app.route('/')
def home():
    current_year = datetime.datetime.now().year
    random_number = random.randint(1, 10)
    return render_template("index.html", num=random_number, year=current_year)


@app.route('/guess/<name>')
def guess_name(name):
    gender_url = f'https://api.genderize.io?name={name}'
    gender_response = requests.get(gender_url)
    gender_data = gender_response.json()
    gender = gender_data["gender"]

    if gender == "male":
        gender = "Homem"
    if gender == "female":
        gender = "Mulher"

    age_url = f'https://api.agify.io?name={name}'
    age_response = requests.get(age_url)
    age_data = age_response.json()
    age = age_data["age"]

    return render_template("guess.html", myname=name, mygender=gender, myage=age)

@app.route('/blog/<num>')
def get_blog(num):
    blog_url = "https://api.npoint.io/f67bcc9a467d8597c8f9"
    blog_response = requests.get(blog_url)
    blog_data = blog_response.json()
    return render_template("blog.html", posts=blog_data)

if __name__ == "__main__":
    app.run(debug=True)
