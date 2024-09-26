from fastapi import FastAPI
from pydantic import BaseModel

#Create your data model
class Item(BaseModel):
    name: str
    description: str | None = None # Optional
    price: float
    tax: float | None = None # Optional


app = FastAPI()

#Inside of the function, you can access all the attributes of the model object directly

@app.post("/items/")
async def create_item(item: Item):
    item_dict = item.dict()
    if item.tax:
        price_with_tax = item.price + item.tax
        item_dict.update({"price_with_tax": price_with_tax})
    return item_dict


#Request body + path + query parameters: You can declare body, path and query parameters, all at the same time
@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item, q: str | None = None):
    result = {"item_id": item_id, **item.dict()}
    if q:
        result.update({"q": q})
    return result