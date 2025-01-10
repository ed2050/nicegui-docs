I recently started using logview to show output from external programs.  Works great, but ran into some tricky bits.  Thought I'd share for others.

## Usage

I wanted a function that does the following:
- take a command for external program with args and run it
- show an indicator while external prog running (ui.spinner)
- show text results (stdout, stderr) on page when finished (ui.log).

Implementation of this func as `runprog()` at end of this post.  Pretty straightforward.  Usage is like this:

```py
@ui.page ('/somepage') 
def somepage () :
    heading ('Some Page', 1)
    
    heading ('Chosen Image', 2)
    ui.image (someimage)
    ui.button ('Show Stats').on ('click', 
        lambda : runprog (['imgstats', '-psx', someimage], results)
    )
    
    results = ui.column ()
```

User clicks button, `imgstats` is invoked, results are shown on page.  Beautiful.

## Tricky bits

Here's the result with default quasar styling.  Total mess.  I assure you there is output text in the box, though you have to really squint to see it (text is highlighted to help).

<img width="500" alt="Screen Shot 2025-01-08 at 4 11 53 PM" src="https://github.com/user-attachments/assets/44434be2-515b-4b1e-93ed-1f08ed250d79" />

The tricky bits are fixing Quasar's default settings, which are awful:
1. It creates a very small box about 15 chars wide by 2 rows high.  You can't fit anything in there.
2. Text doesn't wrap.  Long lines force horizontal scrolling.
3. Text is blurry and impossible to read.  For godforsaken reasons, quasar puts a high opacity (0.4 iirc) on logview (technically on <textarea> with disabled attribute).  Goodbye contrast, hello vision trouble! 🤓 
4. Difficult to change logview height.  Quasar sticks a height **attribute** on generated <textarea> because of course, why make it possible to change with css? 🙄 

## Fixes
1 - easy to change width.  You can use classes & props in nicegui.  Even better, just set in css.  I use width and max-width so it takes all available space but isn't ridiculously wide.

2 - easy to fix by setting text-wrap.

3 - opacity can be fixed once you figure out the issue.  but have to use `!important` because quasar doesn't care about your styles.

4 - this was the trickiest.  You can set `height` but then height is fixed.  If output is short, you don't want a huge empty box.  If output is long, you don't want a short box with tons of scrolling.  So just use max-height right?

The problem is, logview contents change.  We want height to adjust dynamically.  On first display, logview is empty.  Then we log 1 or 2 info lines while external program runs.  When program finishes, we log more - maybe a little, maybe a lot.

You would think `height : fit-content` or `height : max-content` would do the trick.  But no.  They set the height once but don't adjust as content changes, from what I can tell.

Another problem is that quasar sticks a `height` property on logview.  Which overrides any css settings.  Why style with css when you can hardcode properties on each element, right quasar? Brilliant! 🙄

The solution is twofold.  First, use `props('height=fit-content')` on your nicegui element to replace the pixel height crap quasar sticks on it.  Second, in your css use `field-sizing : content` to make the textarea resize dynamically.  With `max-height` as a limit.

Et voila!

<img width="1653" alt="Screen Shot 2025-01-08 at 4 10 57 PM" src="https://github.com/user-attachments/assets/0dc70788-e007-4fbb-875b-44829781aa68" />


## CSS

Here's the css incorporating these fixes.  And some decent margins because quasar / tailwind believe whitespace is the tool of the devil - readability be damned. 👿 

```css
.nicegui-log
{
    /* fix 1 */
    width : 100% ;
    max-width : 60vw ;

    /* fix 2 */
    text-wrap : wrap ;

    /* fix 3 */
    color : #fff ;

    /* fix 4 */
    max-height : 40rem ;
    field-sizing : content ;  /* make height match content */

    margin : 1em 0 ;
}

/* fix 3 */
.disabled , [disabled]  { opacity: 0.9 !important; }  /* fucking quasar... */

```

## Code

Here's the implementation of `runprog`.

```py
# ------------------------------------------------
async \
def runprog (cmd , parent = none , savelog = false) :
    'launch cmd in new process. show results under parent.  cmd can be string or list'

    if not parent :
        parent = ui.column ().classes ('cmdresult')

    cmdtext = cmd
    if istype (cmd, list) :  cmdtext = ' '.join (cmd)

    with parent :
        spin   = ui.spinner (size = '3rem').props ('id=theyspinning')
        cmdlog = ui.log ().props ('height=fit-content')  # resize dynamically
        cmdlog.push (f'running cmd : { cmdtext }')
        scrollto ('theyspinning')

    def runner () :
        # helper to wait for cmd in separate thread
        proc = subprocess.run (cmd , capture_output = true , text = true)
        ret  = proc.returncode
        out  = proc.stdout or ''
        err  = proc.stderr or ''
        return ret , out , err

    cmdtext = istype (cmd, str) and cmd or ' '.join ([ f"'{ x }'" for x in cmd ])
    log (f'calling cmd : { cmdtext }')
    ret = out = err = ''

    try :
        # use io_bound to spawn separate thread
        ret , out , err = await nicegui.run.io_bound (runner)

    except Exception as e :
        warn (f'exception in cmd = { cmdtext } : { e }')

    spin.delete ()
    ui.notify (f'command complete : { ret } : { len (out) } : { len (err) }\n{ cmdtext }')

    # --- show results in logview

    cmdlog.push (f'exit val = { ret }')

    cmdlog.push ('\n--------------- STDOUT --------------')
    cmdlog.push (out or 'empty')

    cmdlog.push ('\n--------------- STDERR --------------')
    cmdlog.push (err or 'empty')

    # show command again for easy reference (avoids scrolling back to top)
    cmdlog.push (f'\nfrom cmd : { cmdtext }')

    # --- save results to log files

    if savelog :
        now     = time.time ()
        outfile = os.path.join (CMDLOGS, f'runproc.{ now }.out')
        errfile = os.path.join (CMDLOGS, f'runproc.{ now }.err')

        u.save (out, outfile)
        u.save (err, errfile)

        cmdlog.push (f'\nstdout saved  : { outfile }\nstderr saved  : { errfile }')
```

