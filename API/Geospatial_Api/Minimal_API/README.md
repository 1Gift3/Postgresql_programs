# WHAT
# Questions
# FastAPI - a Fast Web Framework for building APIs with Python.
# Its on par with Nodejs and go
# Based on and compatible with open standards for APIs: OpenAPI known as Swagger, and JSON Schema

# Fastapi query - Is used to declare query parameters i.e values passed via URL like city=Durban

# JSON
# - a lightweight, human-readable format used to store and exchange data — especially between a client (like a web browser or mobile app) and a server (like your FastAPI backend).

# Nominatim is Geocoder from OpenStreetMap ecosystem - turning place names into Lat/Lon
# While geodesic calculates great circle distance between twon coordinates
# Line 4 - alows me to manually control the response very useful when returning errors on no 200 statuses
# Line 11 is Endpoint logic, declaring GET endpoint at /distance_
# - Accepting query parameter e.g ?city=cape town
# - Query(...) enforces that city is required
# - And description helps auto-generate Swagger UI docs
# Now line 15 - remember line 4 (connected)
# - Is a custom error handle - sending a 404 response if the city cant be geocoded
# - Now what that means is, JSONResponse is like grabbing the steering wheel — super useful when you're handling errors, custom responses, or want full control over how the client receives your data.
# - using Status code:404, response body:{"error": "Location not found."}, and optional headers:Still JSON (because it’s JSONResponse)
# Return is returning a dictionary
# - When returning a Dict FastAPI automatically converts it into JSON ()

# This is a basic API with one endpoint getting -
# GET /distance_to_zweni?city=Johannesburg
# Now this code uses Geocode the city using geopy
# Calculates the distance to Zweni my HQ
# And returns result as JSON

# But i firstly had to install fastapi
# - I was turning my script into a small web api which Fastapi and uvincorn are there to assist
# pip install fastapi
# Uvicorn is ASGI server that run my fastapi app handling incoming web requests.
# And also had to install uvicorn

# So basically i use Fastapi to define API Logic and use Uvicorn to serve it on localhost ( or deploy it later)

# The script receives a city name
# Geocodes it turning it into GPS coordinates using geopy
# Calculates distance from that point to my HQ Zweni
# Returns the distance in KM

# HOW
# This API can be used by a mobile app to show users hor far they from my base or office
# Can offer location based features
# And allows us to compare locations.
# Can used for a web Portal for logistics company or NGO
# - Entering any city to instantly know proximity to HQ
# - Plan routes or assign workers based on distance
# - Use it in dashboards for regional planning
# Can add this as a backend component
# - into a larger system, to check distance from driver to HQ
# Using it as a notification system.

# To run code i Run * python -m uvicorn main:app --reload *
# Then test it in browser http://127.0.0.1:8000/docs

# WHY
# It makes it accessible from any device not just PC
# Allows other developers to use it
# Makes it scalable - connecting it to 100+ devices at once


# Improving
# Adding JWT-auth to secure the enpoint
# return live ETA or routes withOSRM or graphhopper
# support batch queries with post and payloads
# swap to a more robus geocoding API (google maps or HERE) for production.

# SO now for me i want to intergrate e.g Saloons in Zweni that specialize of specialities around my area


