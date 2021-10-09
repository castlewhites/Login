from logging import PlaceHolder
from bokeh.layouts import layout, Spacer
from bokeh.models.widgets import Button, Div, TextInput, PasswordInput
from bokeh.plotting import curdoc


logo = Div(css_classes=['login_logo'])
logo.text = """
    <img
        style='height:100px; width: auto;'
        src='login/static/im/business_logo.png'
    />
"""
# title1
title1 = Div(
    text='Alarmas PTM',
    css_classes=['login_title1']
)
# title2
title2 = Div(text='login', css_classes=['login_title2'])
# edits
user= TextInput(
    title='', value='',
    placeholder="Usuario",
    css_classes=['login_user']
)
# remember password

remember_password= Div(css_classes=['remember_password'])
remember_password.text =""""
    <a style= text-decoration:none  HREF= "" > Recordar contraseña</a>
"""
password= PasswordInput(
    title='', value='',
    placeholder="Contraseña",
    css_classes=['login_password']
)
# button

Button_go = Button(
    label='',
    button_type="primary",
    css_classes=['login_button_go'],
)
#Create new user

new_user = Div(css_classes=['new_user'])
new_user.text = """
    <a style= text-decoration:none HREF= "" > Crear nuevo usuario</a>
"""
# dashboard
login = layout(
    [
        [logo],
        [title1],
        [title2],
        [user],
        [remember_password],
        [password],
        [Button_go],
        [new_user]
    ],
)
login.name = 'login'
curdoc().add_root(login)
curdoc().title = 'PTM'
