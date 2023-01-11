# streamlit_menu_pkg

In streamlit, creating a custom menu takes a little while. With the help of this menu package, users may quickly construct a menu that meets their needs (Expandible or collapsible). This menu item is fully sized in both height and width. Therefore, users may put it anywhere they like in the streamlit window Ex. sidebar, left, right, or center. Users must provide menu information and menu styles (For custom menu themes) in the specified format. The user must modify some of the streamlit's built-in styles if they desire to add a menu component to the sidebar. This menu package will provide the user with the selected menu item and streamlit callback feature. so that based on the chosen menu item, he or she can take the appropriate action.

## Features

- Menu 
- Submenu
- Icon for each menu item 
- Expand and collapse (Configurable) 
- Title and logo (base64 image) for the menu


## Tech Stack

Streamlit, React, and Base Web

## User Guide
1.	Install the menu package using “pip install streamlit-menu”.
2.	Add "import streamlit_menu as menu" at the top of your __init__.py file
3.	Make a dictionary called "header" that contains a menu title and a logo (base64 image). For example: 
	```bash
	header = {“logo”: base64-image-string, “title”: “Gmail Clone”}
	```
4.	Create a list of dictionaries called "menu items" that should contain menu and submenu items in the appropriate format (As specified below). For example: 
    ```bash
    menu_items = [ 
        { 
            "id": 1, 
            "title": "Social", 
            "icon": "fa-solid fa-users", 
            "children": None, 
        }, 
     	{ 
            "id": 2, 
            "title": "Starred", 
            "icon": "fa-solid fa-star", 
            "children": None, 
        }, 
        { 
            "id": 3, 
            "title": "All mails", 
            "icon": "fa-solid fa-envelope", 
            "children": [ 
                { 
                    "id": 4, 
                    "title": "Sent", 
                    "icon": "fa-solid fa-share-from-square", 
                    "children": None, 
                }, 
                { 
                    "id": 5, 
                    "title": "Important", 
                    "icon": "fa-solid fa-tag", 
                    "children": None, 
                }, 
                { 
                    "id": 6, 
                    "title": "Spam", 
                    "icon": "fa-solid fa-triangle-exclamation", 
                    "children": None, 
                }, 
            ], 
        }, 
        { 
            "id": 7, 
            "title": "Bin", 
            "icon": "fa-solid fa-trash-can", 
            "children": None, 
        }, 
        { 
            "id": 8, 
            "title": "Settings", 
            "icon": "fa-solid fa-gear", 
            "children": None, 
        }, 
        { 
            "id": 9, 
            "title": "Logout", 
            "icon": "fa-solid fa-right-from-bracket", 
            "children": None, 
        }, 
    ]
    ```
	(Note: An icon should be a font awesome icon)

5.	Define a callback function. For example:
	```bash
	 def on_menu_select(widgetkey):
	   #Prints the selected menu item on the console
	   print(st.session_state["sidemenu"]["title"])
	```
    (Don’t forget to  write “widgetkey” as a parameter)
6.	To obtain an expandible menu with a default theme, enter the following lines of code.
	```bash
	 menu.st_menu(
	   header = header,
	   menu_items = menu_items,
	   on_menu_select = on_menu_select,
	   args=("sidemenu", )
	  )
    ```
    where args is a tuple holding the parameters for the callback function that was previously specified.

Result:

<img width="960" alt="default expandible menu" src="https://user-images.githubusercontent.com/111497133/211731812-c60a3543-e5f2-40a0-a54c-ee810562274a.PNG">

7.	Follow the first five steps as described above, and then the ones listed below, to create a custom-themed menu.
8.	Make a dictionary called “wrapper_style” and fill it with the background color for the menu (As specified below).  For example:
    ```bash
    wrapper_style = {"background_color": "#32373d"}
    ```
9.	Make a dictionary called “header_style” and fill it with the following specified styles for the menu header.  For example:
    ```bash
    header_style = {
        "items_direction": "column",
        "horizontal_alignment": "center",
        "font_family": "'Brush Script MT', cursive",
        "text_color": "#fff",
        "font_fize": "2.75rem",
        "height": "8rem",
        "logo": {
            "border_radius": "0px",
            "width": "3rem",
            "height": "3rem"
        }
    }
    ```
10.	Make a dictionary called “single_menu_style” and fill it with the following specified styles for the menu item which don’t have children.  For example:
    ```bash
    Single_menu_style = {
        "color": "rgba(255,255,255,.6)",
        "font_family": "'Courier New', monospace",
        "hover": {
            "color": "#fff",
            "background_color": "#2f89fc",
            "left_border":True
        },
        "active_menu": {
            "color": "#fff",
        }
    }
    ```
11.	Make a dictionary called “submenu_style” and fill it with the following specified styles for the submenu.  For example:
    ```bash
    submenu_style = {
        "color": "rgba(255,255,255,.6)",
        "font_family": "'Courier New', monospace",
        "hover": {
            "color": "#fff",
            "background_color": "#2f89fc",
            "left_border":True
        },
        "active_submenu": {
            "color": "#fff",
        }
    }
    ```
12.	Create a variable called "divider_between_header_and_body". Initialize it with the value false if you don't want a line to appear between the menu body and         header. If you do, set its initial value to true. For example:
    ```bash
    divider_between_header_and_body = True
    ```
13.	 If you want the submenu items to be expanded and collapsed, create the variable "is_collapsible" and initialize it with true. Set it to false if you don’t. For      example:
     ```bash
     is_collapsible = True
     ```
14.	Last but not least, add the code below to get the styled menu of your choice:
    ```bash
    menu.st_menu(
        header = header,
        menu_items = menu_items,
        wrapper_style = wrapper_style,
        header_style = header_style,
        single_menu_style = single_menu_style,
        submenu_style = submenu_style,
        divider_between_header_and_body = divider_between_header_and_body,
        is_collapsible = is_collapsible,
        on_menu_select = on_menu_select,
        args = ("sidemenu", )
    )
    ```

Result:

<img width="959" alt="Custome theme menu" src="https://user-images.githubusercontent.com/111497133/211732285-b8a7ef7b-171d-4dbf-a128-7339852d91f3.PNG">

## Conclusion
The user can use this highly customizable menu component package to build a streamlit menu per their needs.
