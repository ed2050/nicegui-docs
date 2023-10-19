# What is Nicegui

Nicegui is a python toolkit for building modern, responsive user interfaces with minimal code.  Nicegui apps can run in a native window, as a web app, or as a local or remote web page.  App logic can be written entirely in python in a single code base - client-side code is optional and not required for any functionality.

# How to use this guide

This guide explains how to use nicegui.  Section 1 contains an overview of nicegui basics and concepts.  The remaining sections cover each nicegui component in detail.  It is recommended to start by reading the entire Overview section, then refer to other sections as needed.

# Basic concepts

Nicegui provides UI components such as buttons, sliders, text, images, charts, and more.  Your app assembles these components into _pages_.  When the user interacts with an item on a page, nicegui triggers an _event_ (or _action_).  You define code to _handle_ each event, such as what to do when a user clicks a button named `Go`.

Components are arranged on a page using _layouts_.  Layouts provide things like grids, tabs, carousels, expansions, menus, and other tools to arrange your components.  Many components are linked to a _model_ (data object) in your code, which automatically updates the user interface when the value changes.

Styling and appearance can be controlled in several ways.  Nicegui accepts optional arguments for certain styling, such as icons on buttons.  Other styling can be set with functions such as .styles, .classes, or .props that you'll learn about later.  Global styles like colors and fonts can be set with dedicated properties.  Or if you prefer, almost anything can be styled with css.

# Implementation

Nicegui is implemented with html components served by an http server (FastAPI), even for native windows.  If you already know html, great, everything will feel very familiar.  If you don't know html, that's fine too!  Nicegui abstracts away the details, so you can focus on creating beautiful interfaces without worrying about how they are implemented.

# Customization

If you want more customization of your app, you can use the underlying Tailwind classes and Quasar components to control the style or behavior of your components.  You can extend the available components by subclassing existing nicegui components or importing new ones from Quasar.  All of this is optional.  Out of the box, Nicegui provides everything you need to make modern, stylish, responsive user interfaces.

# Deploying Nicegui

There are several options for deploying nicegui. ...

# Contents

The remaining pages in this section provide examples of the concepts above.  Read through them to see how nicegui code fits together to build a complete app.
