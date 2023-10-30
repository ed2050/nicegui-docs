Put something here about how to manage components in an app.
I.e. how to pass elements between contexts and retrieve them later in different contexts.

If current approach is saving references for later, then show that:

Say we have button foo.  Depending on what actions the user takes, we may want to enable or disable the button at other points in the app.  To do so, we need to save a reference to the button object somewhere we can access later.
```
class container (object) : pass
myelements = container ()

def main () :
    myelements.foo = ui.button ('Foo')

    more code...

def some_func () :
    do something...
    myelements.foo.disable ()


def another_func () :
    do something...
    myelements.foo.enable ()

```

I don't have a good example in mind right now.  Something to work on.

If a new element query function like `findall` is added in future, that should be introduced here. 

