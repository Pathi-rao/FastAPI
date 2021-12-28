from fastapi import FastAPI, Path, Query, HTTPException, status
from typing import Optional
from pydantic import BaseModel

class Item(BaseModel):
    name:str
    price: float
    brand: Optional[str] = None

class UpdateItem(BaseModel):
    name:Optional[str] = None
    price: Optional[float] = None
    brand: Optional[str] = None

app = FastAPI()

inventory = {}

@app.get("/get-item/{item_id}")
def get_item(item_id: int = Path(None, description="The ID of the item you would like to view", gt=0)): 
    return inventory[item_id]


@app.get("/get-by-name")
def get_item(name: str = Query(None, title="Name", description="Name of item.", max_length=10, min_length=2)):
    for item_id in inventory:
        if inventory[item_id].name == name:
            return inventory[item_id]
    # return {"Data":"not found"}
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail = "Item name not found")
    
# Request Body and POST method
@app.post("/create-item/{item_id}")
def create_item(item_id: int, item: Item):
    if item_id in inventory:
        # return {"Error": "Item ID already exists"}
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail = "Item already exists")

    inventory[item_id] = item
    return inventory[item_id]


# PUT method
@app.put("/update-item/{item_id}")
def update_item(item_id: int, item:UpdateItem):
    if item_id not in inventory:
        # return {"Error": "Item ID does not exists"}
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail = "Item ID does not exist")

    if item.name != None:
        inventory[item_id].name = item.name
    if item.price != None:
        inventory[item_id].price = item.name
    if item.brand != None:
        inventory[item_id].brand = item.brand
    return inventory[item_id]


# DELETE method
@app.delete("/delete-item")
def delete_item(item_id: int = Query(..., description="The ID of the item to delete", gt=0))
    if item_id not in inventory:
        # return {"Error": "ID is not in inventory"}
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail = "Item ID is not in inventory")

    del inventory[item_id]
    return {"Success": "Item is deleted!"}


# some basic status codes
"""
200 : ok
201: created
404: Not found
"""





