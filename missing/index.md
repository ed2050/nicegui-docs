# Missing Items

These items are undocumented in nicegui docs.

1. nicegui API reference - list of all methods like add_head_html, add_body_html, etc with desc
2. nicegui.client api
3. what is client.id?  see https://github.com/zauberzeug/nicegui/discussions/872#discussioncomment-5776545
4. how to get current client / state info outside @ui.page (eg keyboard callbacks)
5. nicegui.app
6. root of current element tree - what is it, how to get it, etc
7. wtf are slots?
8. quasar docs
9. fastapi docs
10. tailwind docs
11. how to change page title dynamically  -- see https://github.com/zauberzeug/nicegui/discussions/1436#discussion-5528911
12. dealing with multiple clients and refresh state (one browser multiple tabs)
13. globals - state is same across _all_ clients / connections
14. access url of current page
15. wtf is context and how does it work?
16. what is request object and how to get it -- see https://github.com/zauberzeug/nicegui/discussions/2026#discussioncomment-7592144 (broken link to fastapi)
17. handling query params
18. how to do redirects
19. that request params (path, query) are SPACE SENSITIVE!!!  @ui.page ('/foo/{num}/') works, @ui.page ('/foo/{ num }/') doesnt!

