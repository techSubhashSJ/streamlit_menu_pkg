import setuptools

setuptools.setup(
    name="streamlit_menu",
    version="1.0.9",
    author="Subhash Jadhav",
    author_email="subhash.jadhav@bluepineapple.io",
    description="Customizable menu component for the streamlit developers",
    long_description="""
• Introduction
  In streamlit, creating a custom menu takes a little while. With the help of this menu package, users may quickly construct a menu that meets their needs (Expandible or collapsible). This menu item is fully sized in both height and width. Therefore, users may put it anywhere they like in the streamlit window Ex. sidebar, left, right, or center. Users must provide menu information and menu styles (For custom menu themes) in the specified format. The user must modify some of the streamlit's built-in styles if they desire to add a menu component to the sidebar. This menu package will provide the user with the selected menu item and streamlit callback feature. so that based on the chosen menu item, he or she can take the appropriate action.

• User Guide
    1. Install the menu package using “pip install streamlit-menu”.
    2. Add "import streamlit_menu as menu" at the top of your __init__.py file
    3. Make a dictionary called "header" that contains a menu title and a logo (base64 image). For example: 
    header = {“logo”: base64-image-string, “title”: “Gmail Clone”}
    4. Create a list of dictionaries called "menu items" that should contain   menu and submenu items in the appropriate format (As specified below). For example: 
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
    (Note: An icon should be a font awesome icon)
    5. Define a callback function. For example:
    def on_menu_select(widgetkey):
        #Prints the selected menu item on the console
        print(st.session_state["sidemenu"]["title"])

    (Don’t forget to  write “widgetkey” as a parameter)
    6. To obtain an expandible menu with a default theme, enter the following lines of code.
    menu.st_menu(
        header = header,
        menu_items = menu_items,
        on_menu_select = on_menu_select,
        args=("sidemenu", )
    )
    where args is a tuple holding the parameters for the callback function that was previously specified.

    7. Follow the first five steps as described above, and then the ones listed below, to create a custom-themed menu.
    8. Make a dictionary called “wrapper_style” and fill it with the background color for the menu (As specified below).  For example:
    wrapper_style = {"background_color": "#32373d"}
    9. Make a dictionary called “header_style” and fill it with the following specified styles for the menu header.  For example:
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
    10. Make a dictionary called “single_menu_style” and fill it with the following specified styles for the menu item which don’t have children.  For example:
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
    11. Make a dictionary called “submenu_style” and fill it with the following specified styles for the submenu.  For example:
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
    12. Create a variable called "divider_between_header_and_body". Initialize it with the value false if you don't want a line to appear between the menu body and header. If you do, set its initial value to true. For example:
    divider_between_header_and_body = True
    13. If you want the submenu items to be expanded and collapsed, create the variable "is_collapsible" and initialize it with true. Set it to false if you don’t. For example:
    is_collapsible = True
    14. Last but not least, add the code below to get the styled menu of your choice:
    menu.st_menu(
        header = data.header,
        menu_items = data.menu_items,
        wrapper_style = style.wrapper_style,
        header_style = style.header_style,
        single_menu_style = style.single_menu_style,
        submenu_style = style.submenu_style,
        divider_between_header_and_body =   style.divider_between_header_and_body,
        is_collapsible=data.is_collapsible,
        on_menu_select = on_menu_select,
        args=("sidemenu", )
    )

• GitHub repo link:
  https://github.com/techSubhashSJ/streamlit_menu_pkg

• Conclusion
  The user can use this highly customizable menu component package to build a streamlit menu per their needs.
    """,
    long_description_content_type="text/plain",
    url="",
    packages=setuptools.find_packages(),
    include_package_data=True,
    classifiers=[],
    python_requires=">=3.6",
    install_requires=[
        "altair==4.2.0",
        "aniso8601==9.0.1",
        "appdirs==1.4.4",
        "attrs==22.1.0",
        "blinker==1.5",
        "cachetools==5.2.0",
        "certifi==2022.6.15",
        "cffi==1.15.1",
        "charset-normalizer==2.1.1",
        "click==8.1.3",
        "colorama==0.4.5",
        "commonmark==0.9.1",
        "cryptography==38.0.1",
        "decorator==5.1.1",
        "docopt==0.6.2",
        "entrypoints==0.4",
        "ez-setup==0.9",
        "Flask==2.2.2",
        "Flask-API==3.0.post1",
        "Flask-Cors==3.0.10",
        "Flask-RESTful==0.3.9",
        "Flask-SQLAlchemy==2.5.1",
        "gitdb==4.0.10",
        "GitPython==3.1.29",
        "greenlet==1.1.3",
        "idna==3.3",
        "importlib-metadata==5.1.0",
        "itsdangerous==2.1.2",
        "Jinja2==3.1.2",
        "jsonschema==4.17.3",
        "jwt==1.3.1",
        "lxml==4.9.1",
        "MarkupSafe==2.1.1",
        "multitasking==0.0.11",
        "mysql-connector-python==8.0.31",
        "numpy==1.23.5",
        "packaging==21.3",
        "pandas==1.5.2",
        "Pillow==9.3.0",
        "pipreqs==0.4.11",
        "protobuf==3.20.1",
        "pyarrow==10.0.1",
        "pycparser==2.21",
        "pydeck==0.8.0",
        "Pygments==2.13.0",
        "PyJWT==2.4.0",
        "Pympler==1.0.1",
        "pyparsing==3.0.9",
        "pyrsistent==0.19.2",
        "python-dateutil==2.8.2",
        "pytz==2022.2.1",
        "pytz-deprecation-shim==0.1.0.post0",
        "requests==2.28.1",
        "rich==12.6.0",
        "semver==2.13.0",
        "six==1.16.0",
        "smmap==5.0.0",
        "SQLAlchemy==1.4.41",
        "streamlit==1.15.1",
        "toml==0.10.2",
        "toolz==0.12.0",
        "tornado==6.2",
        "typing_extensions==4.4.0",
        "tzdata==2022.7",
        "tzlocal==4.2",
        "urllib3==1.26.12",
        "validators==0.20.0",
        "watchdog==2.1.9",
        "Werkzeug==2.2.2",
        "yarg==0.1.9",
        "yfinance==0.1.87",
        "zipp==3.11.0",
    ],
)
