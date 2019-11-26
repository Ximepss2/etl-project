from flask import Flask, render_template
import json
from sqlalchemy import create_engine
import psycopg2 


app = Flask(__name__)

engine = create_engine('postgresql://postgres:ximepss030311@localhost:5432/Movies_DB')

@app.route("/")
def home():
  return render_template("home.html")

@app.route("/credits")
def credits():
  try:
      connection = psycopg2.connect(
        database='Movies_DB',
        user='postgres',
        host='localhost',
        password='ximepss030311'
        
      )
      cursor = connection.cursor()
      postgreSQL_select_Query = 'SELECT * FROM "Credits_Data"'

      cursor.execute(postgreSQL_select_Query)
      mobile_records = cursor.fetchall()
      
      
  except (Exception, psycopg2.Error) as error :
      print ('Error while fetching data from PostgreSQL', error)

  return render_template("credits.html", mobile_records = mobile_records)



@app.route("/movies")
def movies():
    try:
      connection = psycopg2.connect(
        database='Movies_DB',
        user='postgres',
        host='localhost',
        password='ximepss030311'
      )
      cursor = connection.cursor()
      postgreSQL_select_Query = 'SELECT * FROM "MOVIE_DATA"'

      cursor.execute(postgreSQL_select_Query)
      mobile_records = cursor.fetchall()
      
      
    except (Exception, psycopg2.Error) as error :
      print ('Error while fetching data from PostgreSQL', error)

    return render_template("index.html", mobile_records = mobile_records)


if __name__=="__main__":
    app.run(debug=True)