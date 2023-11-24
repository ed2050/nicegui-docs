# Query Params


When you declare other function parameters that are not part of the path parameters, they are automatically interpreted as "query" parameters.


As they are part of the URL, they are "naturally" strings.

But when you declare them with Python types (in the example above, as int), they are converted to that type and validated against it.

All the same process that applied for path parameters also applies for query parameters:
Editor support (obviously)
- Data "parsing"
- Data validation
- Automatic documentation
- Defaults

As query parameters are not a fixed part of a path, they can be optional and can have default values.


# See 
- https://fastapi.tiangolo.com/tutorial/query-params/?h=query#query-parameters
- https://github.com/zauberzeug/nicegui/discussions/870#discussioncomment-5773793
