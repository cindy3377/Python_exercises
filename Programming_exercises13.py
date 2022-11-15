import json
import mysql.connector
from flask import Flask
app = Flask(__name__)

#part1

@app.route('/prime_number/<int:number>')
def is_prime(number):
  flag = True
  if number > 1:
    for i in range(2, number):
      if number % i == 0:
        flag = False
        break
  if flag:
    print(number, "is not a prime number")
  else:
    print(number, "is a prime number")

  response = {
    "number": number,
    "is_prime:": flag
  }
  return json.dumps(response)



#part2

connection = mysql.connector.connect(
  host='127.0.0.1',
  port=3306,
  database='flight_game',
  user='trang',
  password='trang123'
)

@app.route('/airport/<string:icao>')
def get_airport_info(icao):
  airport_info = get_airport(icao)
  print(airport_info)
  return json.dumps(airport_info)

def get_airport(icao):
  sql = "SELECT name, municipality from airport where ident = %s;"
  cursor = connection.cursor()
  cursor.execute(sql, (icao,))
  result = cursor.fetchall()
  cursor.close()
  response = {
    "ICAO": icao,
    "Name:": result[0][0],
    "Location": result[0][1]
  }
  return response

if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=5000)
