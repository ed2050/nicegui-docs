# Text Elements

Let's start our simple app by adding a text element:
```py
from nicegui import ui

ui.label ('Hello world')
ui.run ()
```

Here's what each line does.
- First we import the ui object from nicegui package.  Most of your code will use the ui object to create and manage elements.
- Next we create a new object of type `ui.label` containing the text `Hello World`.  Label is the default text element.  See section [Text Elements](text-elements.md) for more choices.
- The last line starts the nicegui app by launching a local webserver and opening the page.

That's it.  It's really that simple.

# Composing Elements

Nicegui elements are nested in a tree structure.  You will often create elements as children under other elements.  If that sounds complicated, don't worry!  Nicegui makes it easy.

Let's add a link after our Hello World text:
```py
from nicegui import ui

with ui.label ('Hello world, from ') :
  ui.link ('nicegui', 'https://nicegui.io')

ui.run ()
```

The link is created with `ui.link`.  Note that we added `with` before `ui.label`.  This indicates that everything in the `with` block is nested under our label in the element tree.  We can add as many elements as we want inside the `with`.  Each one will be a child of the label node.

> [!NOTE]
> This nesting technique is crucial to using Nicegui.  How you nest elements affects how your pages will be created.

## Alternate Syntax

In this example, we created our label in the `with` statement initializer.  We can also create the label separately and use `with` later.  For instance, this code produces exactly the same result:
```py
from nicegui import ui

mylabel = ui.label ('Hello world, from ')
with mylabel :
  ui.link ('nicegui', 'https://nicegui.io')

ui.run ()
```

The important part is that `ui.link` is created in the context of its parent element in the tree.  You can learn more about contexts and how `ui` tracks parent elements on the _Auto-context_ page.

## Example without nesting

We could also have created the label and link without nesting.  However this would produce a slightly different result.  Say we do this:
```py
from nicegui import ui

ui.label ('Hello world, from ')
ui.link ('nicegui', 'https://nicegui.io')

ui.run ()
```

Now label and link are not nested, but siblings.  They occupy the same level in the element tree.  How these elements are displayed depends on several things, such as the layout element that contains them.  In this example, with no explicit layout elements created, the label and link will be stacked vertically, as each element takes up the entire line.

You can learn more about text elements in the _Text Elements_ section.  Next we'll add some controls to our app.

[Next -->](overview-controls.md)
