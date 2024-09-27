from fastapi import FastAPI, Query
from typing import Annotated
app = FastAPI()

#FastAPI will know that the value of q is not required because of the default value = None.
@app.get("/items/")
async def read_items(q: str | None = None):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results

#We are going to enforce that even though q is optional, whenever it is provided, its length doesn't exceed 50 characters.
@app.get('/items/')
async def read_items(q: Annotated[str | None, Query(max_length=50)] = None):
    result = {'items': [{"item_id": "Tin"}, {"item_id": "Tin dep trai"}]}
    if q:
        result.update({"q": q})
    return result

"""
q: str | None = None
q: Annotated[str | None] = None
Both of those versions mean the same thing, q is a parameter that can be a str or None, and by default, it is None.
"""

#Add regular expressions
@app.get("/items/")
async def read_items(
    q: Annotated[
        str | None, Query(min_length=3, max_length=50, pattern="^fixedquery$")
    ] = None,
):
    results = {"items": [{"item_id": "TIn"}, {"item_id": "Tin dep trai"}]}
    if q:
        results.update({"q": q})
    return results

#Required parameters
@app.get("/items/")
async def read_items(q: Annotated[str, Query(min_length=3)]):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results

#   or
@app.get("/items/")
async def read_items(q: Annotated[str, Query(min_length=3)] = ...):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results

#Required, can be None
@app.get("/items/")
async def read_items(q: Annotated[str | None, Query(min_length=3)] = ...):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results

#Query parameter list / multiple values
@app.get("/items/")
async def read_items(q: Annotated[list[str] | None, Query()] = None):
    query_items = {"q": q}
    return query_items
# --> http://localhost:8000/items/?q=foo&q=bar
'''
RESULTS
{
  "q": [
    "foo",
    "bar"
  ]
}
'''
#Alias parameters
@app.get("/items/")
async def read_items(q: Annotated[str | None, Query(alias="item-query")] = None):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results

