# brython script to move edit buttons next to corresponding row

import browser

from browser import window
from browser import console
from browser import document as doc

# ------------------------------------------------

true, false, none = True, False, None
istype = isinstance
DEBUG  = false

# ------------------------------------------------

modname =  __file__.split ('/') [-1]

log    = lambda x : console.log   (f'{ modname } : { x }')
warn   = lambda x : console.warn  (f'{ modname } : { x }')
debug  = lambda x : console.debug (f'{ modname } : { x }')

rawlog = console.log

# ------------------------------------------------

log (f'loading : { __file__ }')

# ------------------------------------------------

gap = 10

def place_button (node) :
    'place edit button next to node'

    log (f'place button : node = { str (node) }')

    #classes = node.querySelector ('td').classList
    uid    = [ x.split ('-') [-1] for x in node.classList if x.startswith ('uid-') ] [0]
    button = doc.querySelector (f'#button-{ uid }')

    log (f'found uid = { uid }')

    # make button visible
    button.classList.remove ('hide')

    coords = node.getBoundingClientRect ()
    width  = button.getBoundingClientRect ().width

    # get doc origin coords to translate from boundingrect to absolute css
    docpos  = doc.body.getBoundingClientRect ()
    doctop  = docpos.top
    docleft = docpos.left

    #button.style.left = coords.left - width
    button.style.left = f'{ coords.left - docleft - width - gap }px'
    button.style.top  = f'{ coords.top  - doctop }px'
    button.style.position = 'absolute'

    return

# ------------------------------------------------

def scan_rows () :
    'scan doc for visible rows and place edit buttons next to them'

    # hide all edit buttons on page
    buttons = doc.querySelectorAll (f'.rowedit')
    for button in buttons :
        button.classList.add ('hide')

    # get visible table cells
    cells = doc.querySelectorAll (f'td.editable')  # cells with editable class
    for cell in cells :
        try :
            place_button (cell)
        except Exception as e :
            warn (f'place button failed : { cell } : { e }')

# ------------------------------------------------

def watch_rows (mutlist, observer) :
    'watch for new table rows in document'

    DEBUG and log (f'mutations : { len (mutlist) }')
    DEBUG and console.log (mutlist)

    nodechanges = any ([ mut.addedNodes for mut in mutlist ])
    if nodechanges :
        scan_rows ()

# ------------------------------------------------

log ('adding row watcher mut obs')

mutob = window.MutationObserver.new (watch_rows)
mutob.observe (doc.body, { 'subtree' : true , 'childList' : true , 'attributes' : false })

# init page
scan_rows ()

