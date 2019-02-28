import re


value = """


#main-header .et_mobile_menu .menu-item-has-children > a { background-color: transparent; position: relative; }

#main-header .et_mobile_menu .menu-item-has-children > a:after { font-family: 'ETmodules'; text-align: center; speak: none; font-weight: normal; font-variant: normal; text-transform: none; -webkit-font-smoothing: antialiased; position: absolute; }

#main-header .et_mobile_menu .menu-item-has-children > a:after { font-size: 16px; content: '\4c'; top: 13px; right: 10px; }

#main-header .et_mobile_menu .menu-item-has-children.visible > a:after { content: '\4d'; }

#main-header .et_mobile_menu ul.sub-menu { display: none !important; visibility: hidden !important; transition: all 1.5s ease-in-out;}

#main-header .et_mobile_menu .visible > ul.sub-menu { display: block !important; visibility: visible !important; }

 """
new_expression = '[Contents]'
new_expression = re.sub("[\[].*?[\]]", value, new_expression, 1)
print(new_expression)
