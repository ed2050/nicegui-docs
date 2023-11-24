# Redirects

```
from fastapi.responses import RedirectResponse

def redirect () :
    return RedirectResponse ('/foo')
```

see https://fastapi.tiangolo.com/uk/advanced/custom-response/#redirectresponse

If you await the client connection, NiceGUI will internally generate a html response which can then connect back via websocket to the server. Therefore the RedirectResponse can not be interpreted anymore. 

To open a new page after connection is established you can use https://nicegui.io/documentation/open. If you only need the IP address you could use #1695 (comment) instead of getting it from the client.

https://github.com/zauberzeug/nicegui/discussions/1743#discussioncomment-7193414
