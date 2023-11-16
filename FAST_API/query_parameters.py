# When you declare other function parameters that are not part of the path parameters, they are automatically interpreted as "query" parameters.

# query-parameter = parameter included in your function parameter but not in your path operation
from fastapi import FastAPI ,  Query
from typing import Annotated

app = FastAPI()

fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]


@app.get("/items/")
async def read_item(skip: int = 0, limit: int = 10):
    return fake_items_db[skip : skip + limit]


# optional parameters
# q: str | None = None

# Query parameter type conversion
#  short: bool = False  => equal to   on / true / True / False / false / 1 / yes


# required
# item_id: str

# You could also use Enums the same way as with Path Parameters.


# additional validations
# q: Annotated[str | None, Query(max_length=50)] = None

# q: str | None = Query(default=None, max_length=50) - without annotation

# q: Annotated[str, Query()] = "rick" - default with annotation

#  q: Annotated[str | None, Query(min_length=3, max_length=50)] = None

# Add regular expressions
#  str | None, Query(min_length=3, max_length=50, pattern="^fixedquery$")

# Pydantic v1 regex instead of pattern
#  str | None, Query(min_length=3, max_length=50, regex="^fixedquery$")

# default
# q: Annotated[str, Query(min_length=3)] = "fixedquery"

# Required with Ellipsis (...)
# q: Annotated[str, Query(min_length=3)] = ...

# Query parameter list / multiple values
# q: Annotated[list[str] | None, Query()] = None

# Query parameter list / multiple values with defaults
# q: Annotated[list[str], Query()] = ["foo", "bar"]

# Using list
# q: Annotated[list, Query()] = []

# You can add a title
#  q: Annotated[str | None, Query(title="Query string", min_length=3)] = None

# And a description:
#  description="Query string for the items to search in the database that have a good match"

# Alias parameters
# (q: Annotated[str | None, Query(alias="item-query")] = None)

# Deprecating parameters
# deprecated=True,

@app.get("/items/")
async def read_items(
    q: Annotated[
        str | None,
        Query(
            alias="item-query",
            title="Query string",
            description="Query string for the items to search in the database that have a good match",
            min_length=3,
            max_length=50,
            pattern="^fixedquery$",
            deprecated=True,
        ),
    ] = None,
):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results


# Query Parameter reserved keyword arguments =
    # default: Any = Undefined,
    # *,
    # default_factory: (() -> Any) | None = _Unset,
    # alias: str | None = None,
    # alias_priority: int | None = _Unset,
    # validation_alias: str | None = None,
    # serialization_alias: str | None = None,
    # title: str | None = None,
    # description: str | None = None,
    # gt: float | None = None,
    # ge: float | None = None,
    # lt: float | None = None,
    # le: float | None = None,
    # min_length: int | None = None,
    # max_length: int | None = None,
    # pattern: str | None = None,
    # regex: str | None = None,
    # discriminator: str | None = None,
    # strict: bool | None = _Unset,
    # multiple_of: float | None = _Unset,
    # allow_inf_nan: bool | None = _Unset,
    # max_digits: int | None = _Unset,
    # decimal_places: int | None = _Unset,
    # examples: List[Any] | None = None,
    # example: Any | None = _Unset,
    # openapi_examples: Dict[str, Example] | None = None,
    # deprecated: bool | None = None,
    # include_in_schema: bool = True,
    # json_schema_extra: Dict[str, Any] | None = None,
    # **extra: Any