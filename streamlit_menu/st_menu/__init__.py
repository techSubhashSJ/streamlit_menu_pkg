from streamlit_menu.st_menu.register import register_callback, init, get_component_rerender_count, set_component_rerender_count

import os
import streamlit.components.v1 as components

# Create a _RELEASE constant. We'll set this to False while we're developing
# the component, and True when we're ready to package and distribute it.
# (This is, of course, optional - there are innumerable ways to manage your
# release process.)
_RELEASE = True

# Declare a Streamlit component. `declare_component` returns a function
# that is used to create instances of the component. We're naming this
# function "_component_func", with an underscore prefix, because we don't want
# to expose it directly to users. Instead, we will create a custom wrapper
# function, below, that will serve as our component's public API.

# It's worth noting that this call to `declare_component` is the
# *only thing* you need to do to create the binding between Streamlit and
# your component frontend. Everything else we do in this file is simply a
# best practice.

if not _RELEASE:
    st_component = components.declare_component(
        # We give the component a simple, descriptive name ("my_component"
        # does not fit this bill, so please choose something better for your
        # own component :)
        "Menu",
        # Pass `url` here to tell Streamlit that the component will be served
        # by the local dev server that you run via `npm run start`.
        # (This is useful while your component is in development.)
        url="http://localhost:3000",
    )
else:
    # When we're distributing a production version of the component, we'll
    # replace the `url` param with `path`, and point it to to the component's
    # build directory:
    parent_dir = os.path.dirname(os.path.abspath(__file__))
    build_dir = os.path.join(parent_dir, "frontend/menu")
    st_component = components.declare_component("Menu", path=build_dir)

# Overridden inbuilt streamlit css

# Create a wrapper function for the component. This is an optional
# best practice - we could simply expose the component function returned by
# `declare_component` and call it done. The wrapper allows us to customize
# our component's API: we can pre-process its input args, post-process its
# output value, and add a docstring for users.

init()

def getMenu(header={},
            menu_items = [],
            divider_between_header_and_body=True,
            header_style = {},
            wrapper_style = {},
            submenu_style = {},
            single_menu_style = {},
            is_collapsible=True,
            key=None,
            on_select=None,
            args: tuple = ()):

    register_callback(key, on_select, *args)
    render_count = get_component_rerender_count(key)
    
    component_value = st_component(header=header,
                                   menu_items=menu_items,
                                   divider_between_header_and_body=divider_between_header_and_body,
                                   header_style=header_style,
                                   wrapper_style = wrapper_style,
                                   submenu_style = submenu_style,
                                   single_menu_style = single_menu_style,
                                   is_collapsible=is_collapsible,
                                   key=key,
                                   render_count=render_count,
                                   default=0)
    
    set_component_rerender_count(key)
    # We could modify the value returned from the component if we wanted.
    # There's no need to do this in our simple example - but it's an option.
    return component_value
