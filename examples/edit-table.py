# module to create nicegui page with editable table rows
# uses brython script rowedit.py to reposition edit buttons

import random
import string
import json

import nicegui
from nicegui import ui
from nicegui import app

# ---

true, false, none = True, False, None
istype = isinstance

# js code to launch brython after doc loads
launcher = '''
console.log ('brython launcher loading') ;
var modpaths = [
    '/urlpath/to/my/brython/modules' ,
] ;

var launched = false ;  // guard to prevent loading multiple times

function launch ()
{
    if (! launched) {
        console.log ('launching brython...') ;
        brython ({ pythonpath : modpaths }) ;
        launched = true ;
    }
}

document.addEventListener ('DOMContentLoaded', launch) ;
console.log ('brython launcher loaded') ;
'''

# ------------------------------------------------

def shared_headers () :
    'add shared page headers with scripts and styles'

    jscripts = [
        'https://cdn.jsdelivr.net/npm/brython@3.13.0/brython.min.js' ,
        'https://cdn.jsdelivr.net/npm/brython@3.13.0/brython_stdlib.js' ,
    ]

    # get url to local file with brython code
    editscript = app.add_static_file (local_file = 'rowedit.py')
    pscripts = [ editscript ]

    for src in jscripts :
        ui.add_head_html (f'<script type="text/javascript" src="{ src }"> </script>')

    for src in pscripts :
        ui.add_head_html (f'<script type="text/python" src="{ src }"> </script>')

    # add brython launch code
    ui.add_head_html (f'<script type="text/javascript"> { launcher } </script>')

    # --- add stylesheet with default styles
    styles = '''
        #mytable { margin-left : 5em ; }
        .hide    { display : none ; }
    '''
    ui.add_head_html (f'<style type="text/css"> { styles } </style>')

# ------------------------------------------------

@ui.page ('/')
def mainpage () :

    shared_headers ()

    # make random data
    data = [
        {
            'uid'   : random.randint (1000, 10 * 1000) ,
            'file'  : ''.join (random.choices (string.ascii_lowercase, k = 10)) ,
            'size'  : random.randint (2**8, 2**14) ,
            'mtime' : random.randint (14e8 , 17e8) ,  # timestamp in seconds
            'long stuff' : ''.join (random.choices (string.ascii_lowercase, k = 50)) ,
        }
        for x in range (50)
    ]


    # make column settings
    cols   = []
    fields = list (data [0])

    for field in fields :
        cols.append ({
            'name'  : field ,
            'label' : field.title () ,
            'field' : field ,
            'align' : 'left' ,
        })

    # add uid to class of first cell
    cols [0] [':classes'] = 'row => "editable uid-" + row.uid'

    # make table
    print (f'{ data [0] = }')
    print ('cols = ' + json.dumps (cols, indent = '\t'))

    table = ui.table (
        columns = cols ,
        rows    = data ,
        pagination = { 'rowsPerPage' : 20 } ,
    ).props ('id=mytable')

    # nicegui / quasar dont let us manipulate table rows directly, because reasons :/
    # instead we'll add edit buttons here and re-position later

    def edit_row (item) :
        drawer = ui.right_drawer ()
        with drawer :
            # put whatever edit fields you want here
            ui.label (str (item))

            save = ui.button ('save')
            save.on ('click', lambda : drawer.toggle ())

    for item in data :
        editbutton = ui.button (icon = 'edit').classes ('rowedit')
        editbutton.props (f'id=button-{ item ["uid"] }')

        # set default arg on lambda or will always use last item in data
        editbutton.on ('click', lambda item = item :  edit_row (item))

# end mainpage

# ------------------------------------------------

if __name__ in {'__main__', '__mp_main__'} :
    ui.run (dark = True)
