from nicegui import ui
from nicegui import native_mode

true, false, none = True, False, None
DEBUG = false

# ------------------------------------------------

class container (object) : pass

g = container ()
g.root = none

# ------------------------------------------------

def set_root (node) :
	'find and set the root node for all ui elements'
	
	while node.parent_slot :
		node = node.parent_slot.parent

	g.root = node
	return node

# ------------------------------------------------

def findall (searchids, startnode = none) :
	'return a list of all nodes under startnode (deafult: root) matching dot-separated searchids'

	if startnode is none : 
		startnode = g.root

	classlist = searchids.split ('.')

	# --- gather all nodes under startnode
	# use a set so each node only appears once; assumes ui elements implement ==

	checknodes = set (startnode._collect_descendants ())
	checknodes.add (startnode)

	matches = []

	while classlist :

		# --- match next item in classlist 

		klass = classlist.pop (0)
		matches = [ x for x in checknodes if klass in x._classes ]

		DEBUG and print (f'{ klass = } : found { len (matches) } : { matches }')

		# --- are we done ?

		if not len (classlist)  : break
			
		# --- update for next item in classlist
		# not efficient to rewalk subtree on each iteration, improve later if needed

		checknodes = set ()
		for node in matches :
			checknodes.add (node)
			checknodes.update (node._collect_descendants ())
			desc = node._collect_descendants ()
			
			DEBUG and print (f'found { len (desc) } descendants : { desc }')

		matches = []

	return matches

# ------------------------------------------------

def register (nodeid, node) :
	'register node with id nodeid'

	node.classes (nodeid)
	return node

# ------------------------------------------------

def change_color (node, color) :

	# remove old color classes, because button colors are broken
	imp = [ x for x in node._classes if x[0] == '!' ]
	[ node._classes.remove (x) for x in imp ]
	node.classes (f'!{color}')

# ------------------------------------------------

def update_buttons (searchids, color) :

	nodes = findall (searchids)
	DEBUG and print (f'changing { len (nodes) } { searchids } to { color }')

	for node in nodes :

		change_color (node, color)

# ------------------------------------------------

ISDARK = true

#red    = 'bg-red-300 dark:bg-red-600'
red    = 'bg-red-500'
blue   = 'bg-blue-500'
green  = 'bg-green-500'
orange = 'bg-yellow-500'
grey   = 'bg-slate-500'

def mainpage () :

	dark = ui.dark_mode ()
	if ISDARK :  dark.enable ()

	with ui.left_drawer (top_corner = true, bottom_corner = true).classes ('bg-yellow-300 dark:bg-yellow-800') as drawer :

		set_root (drawer)
		ui.label ('findall demo').classes (add = 'text-3xl')

		switch = ui.switch ('Dark mode', value = ISDARK, on_change = dark.toggle)

		# set a dummy color param.  value doesnt matter, will change later
		# if we dont pass color param, value is fixed

		b1 = ui.button ( 'Make foo red'   , color = 'red' ,
			on_click = lambda x : update_buttons ('foo', red)
		)
		b2 = ui.button ('Make bar green' , color = 'green' ,
			on_click = lambda x : update_buttons ('bar', green)
		)
		b3 = ui.button ('Make even blue' , color = 'blue' ,
			on_click = lambda x : update_buttons ('evencard.btn', blue)
		)
		b4 = ui.button ('Make odd orange', color = 'orange' ,
			on_click = lambda x : update_buttons ('oddcard.btn', orange)
		)

	with register ('card1 oddcard', ui.card ()) :

		ui.element ('h2')._text = 'Card 1'
		# have to pass dummy color to button or later color changes don't work.  stupid.
		register ('foo btn', ui.button ('Foo', color = grey))
		register ('bar btn', ui.button ('Bar', color = grey))

	with register ('card2 evencard', ui.card ()) :

		ui.element ('h2')._text = 'Card 2'
		register ('foo btn', ui.button ('Foo', color = grey))
		register ('bar btn', ui.button ('Bar', color = grey))

	with register ('card3 oddcard', ui.card ()) :

		ui.element ('h2')._text = 'Card 3'
		register ('foo btn', ui.button ('Foo', color = grey))
		register ('bar btn', ui.button ('Bar', color = grey))

	
	# --- set width on all cards

	cards = findall ('nicegui-card')
	for card in cards :
		card.classes ('w-40')

	# --- set color on all buttons
	# doesnt work unless color flag passed to button constructor.  dumb.

	buttons = findall ('btn')
	for button in buttons :
		change_color (button, orange)

	# --- start app

	title = 'findall demo'

	ui.run (title = title ,
		port = native_mode.find_open_port () ,
	)

# ------------------------------------------------

if __name__ in { '__main__', '__mp_main__' } :

	mainpage ()

# ------------------------------------------------

# ------------------------------------------------

def get_children (node) :

	return node.slots ['default'].children

# ------------------------------------------------

def _find (root, klass) :
	'return a list of all nodes under root with class klass'

	matches = []

	if klass in root._classes :
		matches.append (root)

	for child in get_children (root) :
		matches.extend (_find (child, klass))

