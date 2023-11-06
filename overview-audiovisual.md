# Audiovisual Elements

Let's add an image to our sample app.
```py
from nicegui import ui

ui.image ('https://nicegui.io/static/logo.png')

with ui.label ('Hello world, from ') :
  ui.link ('nicegui', 'https://nicegui.io')

ui.button ('Tell me more', on_click = lambda : ui.notify ('Nice to meet you') )

ui.run ()
```

`ui.image` takes one parameter: a link to an image file to display.  Besides urls, you can also pass local paths or base64-encoded mimetype strings.  These are described on the _Images_ page.  You can also add other audiovisual media like videos, audio, animations, and interactive images.  

# Linking the image

Let's improve our app slightly by linking the image file to the nicegui website.
```py
from nicegui import ui

with ui.link (target = 'https://nicegui.io') :
  ui.image ('https://nicegui.iowebsite/static/logo.png')

with ui.label ('Hello world, from ') :
  ui.link ('nicegui', 'https://nicegui.io')

ui.button ('Tell me more', on_click = lambda : ui.notify ('Nice to meet you') )

ui.run ()
```

To make the image itself part of the clickable link, we nest the image under our ui.link element.  The first argument to ui.link is normally the text to display.  Because this link has no text, we use `target =` to indicate the provided argument is the link target.

You can learn about other types of media in the _Audiovisual_ section.  Next let's add a data element to our app.

[Next -->](overview-data.md)
