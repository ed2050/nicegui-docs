# What is Nicegui

Nicegui is a python toolkit for building modern, responsive user interfaces with minimal code.  Nicegui apps can run in a native window, as a web app, or as a local or remote web page.  App logic can be written entirely in python in a single code base - client-side code is optional and not required for any functionality.

# How to use this guide

This guide explains how to use nicegui.  Section 1 contains an overview of nicegui basics and concepts.  The remaining sections cover each nicegui component in detail.  It is recommended to start by reading the entire Overview section, then refer to other sections as needed.

# Basic concepts

Nicegui provides UI _components_ (or _elements_) such as buttons, sliders, text, images, charts, and more.  Your app assembles these components into _pages_.  When the user interacts with an item on a page, nicegui triggers an _event_ (or _action_).  You define code to _handle_ each event, such as what to do when a user clicks a button named `Go`.

Components are arranged on a page using _layouts_.  Layouts provide things like grids, tabs, carousels, expansions, menus, and other tools to arrange your components.  Many components are linked to a _model_ (data object) in your code, which automatically updates the user interface when the value changes.

Styling and appearance can be controlled in several ways.  Nicegui accepts optional arguments for certain styling, such as icons on buttons.  Other styling can be set with functions such as .styles, .classes, or .props that you'll learn about later.  Global styles like colors and fonts can be set with dedicated properties.  Or if you prefer, almost anything can be styled with css.

# Components

Nicegui provides many types of components for building interfaces:
- The section _Text Elements_ covers different text-based components such as headings, paragraphs, links, and labels.  You can also insert formatted text using markdown or html.
- The section _Controls_ cover elements for getting user input: buttons, sliders, checkboxes, text input, date or color choosers, and many more.
- The section _Audiovisual_ covers adding media elements to your interface, such as images, video, audio, or animations.
- The section _Data Elements_ covers different ways of displaying data: tables, graphs, charts, trees, progress bars, and more.  There are also components for editing styled text, code, or json.
- The section _Layout_ covers components for arranging other elements on a page.  Grids, cards, scroll areas, tabs, splitters, menus, and more are available.
- The section _Appearance_ covers ways to style components, including size, shape, color, and much more.

# Actions

Nicegui runs an event loop to handle user input and other events like timers and keyboard bindings.  You can write asynchronous functions for long-running tasks to keep the UI responsive.  The _Actions_ section covers how to work with events.

# Implementation

Nicegui is implemented with html components served by an http server (FastAPI), even for native windows.  If you already know html, everything will feel very familiar.  If you don't know html, that's fine too!  Nicegui abstracts away the details, so you can focus on creating beautiful interfaces without worrying about how they are implemented.

# Running Nicegui Apps

There are several options for deploying nicegui. By default, Nicegui runs a server on localhost and runs your app as a private web page on the local machine.  When run this way, your app appears in a web browser window.  You can also run Nicegui in a native window separate from a web browser.  Or you can run Nicegui on a server that handles many clients - the website you're reading right now is served from Nicegui.

After creating your app pages with components, you call `ui.run()` to start the nicegui server.  Optional parameters to `ui.run` set things like the network address and port the server binds to, whether the app runs in native mode, initial window size, and many other options.  The section _Configuration and Deployment_ covers the options to the `ui.run()` function and the FastAPI framework its based on.

# Customization

If you want more customization in your app, you can use the underlying Tailwind classes and Quasar components to control the style or behavior of your components.  You can learn about interacting with Tailwind and Quasar in the section [to be added].  You can also extend the available components by subclassing existing nicegui components or importing new ones from Quasar.  All of this is optional.  Out of the box, Nicegui provides everything you need to make modern, stylish, responsive user interfaces.

# Contents

The remaining pages in this section provide examples of the concepts above by building a simple app.  Read through them to see how nicegui code fits together.  Then reference the other sections for more details.

1. [Overview](overview.md) (this page)
   1. [Text Elements Intro](overview-text-elements.md)
   2. [Controls Intro](overview-controls.md)
   3. [Audiovisual Elements Intro](overview-audiovisual.md)
   4. [Data Elements Intro](overview-data.md)
   5. [Page Layout Intro](overview-layout.md)
   6. [Styling & Appearance Intro](overview-styles.md)
   7. [Actions & Events Intro](overview-events.md)
   8. [Configuring & Deploying Intro](overview-deploying.md)
1. Text Elements (copy from existing docs index page)
    1. Label (existing page)
    2. Header (existing page)
    3. Paragraph (existing page)
    4. ...
1. Controls (copy from existing docs index page)
    1. Button
    1. Slider
    1. Checkbox
    1. ...
1. Audiovisual Elements
    1. Image
    1. Video
    1. Audio
    1. ...
6. ...


[Next -->](overview-text-elements.md)
