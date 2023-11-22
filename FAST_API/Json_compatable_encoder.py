from datetime import datetime
from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel

app = FastAPI()

fake_db = {}

class Item(BaseModel):
    title: str
    timestamp: datetime
    description: str | None = None

@app.put("/items/{id}")
def update_item(id: str, item: Item):
    json_compatible_item_data = jsonable_encoder(item)
    fake_db[id] = json_compatible_item_data

# objects -> json

# body updates ----------------------------
from typing import Union
class Item1(BaseModel):
    name: Union[str, None] = None
    description: Union[str, None] = None
    price: Union[float, None] = None
    tax: float = 10.5
    tags: list[str] = []


items = {
    "foo": {"name": "Foo", "price": 50.2},
    "bar": {"name": "Bar", "description": "The bartenders", "price": 62, "tax": 20.2},
    "baz": {"name": "Baz", "description": None, "price": 50.2, "tax": 10.5, "tags": []},
}


@app.get("/items/{item_id}", response_model=Item)
async def read_item(item_id: str):
    return items[item_id]


@app.put("/items/{item_id}", response_model=Item)
async def update_item(item_id: str, item: Item):
    update_item_encoded = jsonable_encoder(item)
    items[item_id] = update_item_encoded
    return update_item_encoded


# to partially update the data

@app.patch("/items/{item_id}", response_model=Item)
async def update_item(item_id: str, item: Item):
    stored_item_data = items[item_id]
    stored_item_model = Item(**stored_item_data)
    update_data = item.model_dump(exclude_unset=True)
    updated_item = stored_item_model.model_copy(update=update_data)
    items[item_id] = jsonable_encoder(updated_item)
    return updated_item

# stored_item_data = items[item_id]: This line retrieves the existing data for the item with the given item_id from some data structure or database. The assumption here is that there is a dictionary named items containing item data, and item_id is used as a key to fetch the stored data.

# stored_item_model = Item(**stored_item_data): This line creates an instance of the Item Pydantic model using the data retrieved from items. This step allows us to use Pydantic's model validation and manipulation features.

# update_data = item.model_dump(exclude_unset=True): This line extracts the data from the incoming item instance, excluding any fields that have not been set (i.e., fields with default values or fields that are not present in the incoming data).

# updated_item = stored_item_model.model_copy(update=update_data): This line creates a copy of the stored_item_model with the specified updates from the update_data. It utilizes Pydantic's model_copy method, allowing for easy updating of model instances.

# items[item_id] = jsonable_encoder(updated_item): This line updates the data for the item in the items dictionary with the newly updated item data. The jsonable_encoder function is used to convert the updated_item instance into a JSON-serializable format.

# return updated_item: Finally, the updated item data is returned as the response. The response is automatically serialized to JSON according to the Item Pydantic model due to the response_model=Item decorator parameter.