import streamlit as st
import os
from streamlit_menu.st_menu import getMenu

parent_dir = os.path.dirname(os.path.abspath(__file__))
css_file = os.path.join(parent_dir, "style.css")


def st_menu(menu_items={}, header={}, divider_between_header_and_body=True, header_style={}, wrapper_style={}, submenu_style={}, single_menu_style={}, is_collapsible=False, on_menu_select=None, args=None):
    with st.sidebar:
        getMenu(menu_items=menu_items,
                header=header,
                divider_between_header_and_body=divider_between_header_and_body,
                header_style=header_style,
                wrapper_style=wrapper_style,
                submenu_style=submenu_style,
                single_menu_style=single_menu_style,
                is_collapsible=is_collapsible,
                key="sidemenu",
                on_select=on_menu_select,
                args=args)

    return st.session_state["sidemenu"]
