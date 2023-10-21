# Adding Styles

Let's add some styling to our app.  

## Default styles

First let's add default styles that apply to the entire page.  Font family, size, background color.

## Element styles

Now let's style particular elements.  Image width, button color.


```py
from nicegui import ui

ui.image ('https://nicegui.iowebsite/static/logo.png')

with ui.label ('Hello world, from ') :
  ui.link ('nicegui', 'https://nicegui.io')

ui.button ('Tell me more', on_click = lambda : ui.notify ('Nice to meet you') )

ui.run ()
```

## Alternate approach: CSS styles

If you're familiar with CSS, you can use it to control styling.  If you don't know CSS, feel free to skip the rest of this page.

...

You can learn about other types of media in the _Appearance & Styling_ section.  Next let's...

[Next -->](overview-data.md)
