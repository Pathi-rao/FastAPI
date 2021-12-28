"""
ref: https://www.youtube.com/watch?v=-ykeT6kk4bk

Installation:
    - pip install fastapi
    - pip install uvicorn - Uvicorn is a lightning-fast ASGI server implementation

Run: 
    - command to run the API, `uvicorn main:app --reload`
    main is the name of the script, app is the name of the variable that you initialize 
    the API to(see below) and --reload reloads the server whenver the API python file 
    is updated.
"""

"""
Advantages:
    Data Validation: When we create normal API's, we need to do a lot of data validation 
        when sending information to the API for example whether it is integer or proper 
        strings or etc. But here the FastAPI handles it for us.

    Also, it generates auto-documentation.
"""

from fastapi import FastAPI, Path
from typing import Optional

# always need to initialize this call if we want to use the API
app = FastAPI()

"""
Create an endpoint

Endpoint: is like the last end point in our url.
Eg: Let's we have some url in our localhost and we would like to access the
home page, then the endpoint would be "localhost/homepage"

Eg: In "facebook.com/home", the /home is like an endpoint for the facebook

When we setup an endpoint, we have different methods like
GET - returning information
POST- send information/create something new
PUT -  update something that is already existing
DELETE - delete something
"""
# @app.get("/") # whenever we go to this route, the following function is triggered
# def home():
#     return {"Data":"Test"}

# #create another endpoint
# @app.get("/about")
# def about():
#     return {"Data":"About"}


# for the sake of understanding, let's treat this API as an inventory management system

inventory = {
        1: {
            "name": "Milk",
            "price": 3.99,
            "brand": "Regular"
        }
}

"""
PathParameter:
lets create an endpoint that can retreive item information based on its id
"""
# @app.get("/get-item/{item_id}") # item_id here is like a place holder where we give the id
# def get_item(item_id: int): # "item_id: int" is called a type hint in python and it tells the 
#                             # FastAPI that this variable should be a integer type

#     return inventory[item_id]

# if we want to create multiple path-parameters
# @app.get("/get-item/{item_id}/{name}")
# def get_item(item_id: int, name: str):
#     return inventory[item_id]


# Path allows us to add more details/constraints to our path parameter

@app.get("/get-item/{item_id}")
def get_item(item_id: int = Path(None, description="The ID of the item you would like to view", gt=0)): 
                                # None is the default value for this parameter
                                # gt-greater than, the constraint
                                # we can pass a combination of them like gt=0, lt=2(greater than 0, less than 2)
    return inventory[item_id]

"""
QueryParameter:
It is what comes after a question mark in an url
"""
@app.get("/get-by-name")
def get_item(name: str): #if we pass str = None here then the pass the parameter "name" becomes optional
# def get_item(name: Optional[str] = None): # use this for better docs (recommended but not necessary)
    for item_id in inventory:
        if inventory[item_id]["name"] == name:
            return inventory[item_id]
    return {"Data":"not found"}
# test it by going to "localhost/get-by-name?name=Milk"

#create multiple query parameters
# @app.get("/get-by-name")
# def get_item(*, name: Optional[str]=None, test: int):
#     for item_id in inventory:
#         if inventory[item_id]["name"] == name:
#             return inventory[item_id]
#     return {"Data":"not found"}


"""
Combining Path parameters and Query parameters
"""
# @app.get("/get-by-name/{item_id}")
# def get_item(*, item_id: int, name: Optional[str]=None, test: int):
#     for item_id in inventory:
#         if inventory[item_id]["name"] == name:
#             return inventory[item_id]
#     return {"Data":"not found"}

