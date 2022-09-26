import mysql.connector

connection = mysql.connector.connect(
   host='127.0.0.1',
   port= 3306,
   database='flight_game',
   user='trang',
   password='trang123'
 )

if (connection.is_connected()):
    print("Connected")
else:
    print("Not connected")

#Exercise1


def airport():
  ident = input("Please enter ICAO to fetch airport: ")
  print(ident)
  sql = "SELECT name as 'airport name', municipality as 'location' from airport where ident = %s;"
  print(sql)
  cursor = connection.cursor()
  cursor.execute(sql, (ident,))
  result = cursor.fetchall()
  print(result)
  return
airport()


#Exercise2


def areaCode():
  code = input("Please enter area code to fetch information: ")
  print(code)
  sql = "SELECT country.name as 'country name', airport.name as 'airport name', airport.type as 'airport type' from country, airport WHERE country.iso_country = airport.iso_country AND airport.iso_country = %s order by airport.type;"
  print(sql)
  cursor = connection.cursor()
  cursor.execute(sql, (code,))
  result = cursor.fetchall()
  print(result)
  return

areaCode()


#Exercise3

def get_geo_location(ident):
  sql = "SELECT airport.latitude_deg as 'latitude', airport.longitude_deg as 'longitude' from airport, country WHERE country.iso_country = airport.iso_country AND ident = %s LIMIT 1;"
  cursor = connection.cursor()
  cursor.execute(sql, (ident,))
  result = cursor.fetchall()
  return result[0]


from geopy import distance
ident_1 = input("Please enter the ICAO of the first airport:")
place_1_geo = get_geo_location(ident_1)

ident_2 = input("Please enter the ICAO of the second airport:")
place_2_geo = get_geo_location(ident_2)

print("Location of the first airport: ", place_1_geo)
print("Location of the second airport: ", place_2_geo)
print(f"The distance between two airports is:", distance.distance(place_1_geo, place_2_geo).km, "km.")
