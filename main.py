from bokeh.layouts import layout
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
title2 = Div(text='Login', css_classes=['login_title2'])
validation = Div(
    text='', css_classes=['login_validation'], name='login.validation'
)
# edits
user = Div()
user.text =""" 
    <p>
      Usuario:  <input type="text" class="redondeado" value="input con borde redondeado">
    </p>
"""

password = PasswordInput(
    css_classes=['login_password'],
    name='login.password',
    title='Contraseña:',   
)
# button
button_go = Button(
    label='',
    button_type="primary",
    css_classes=['login_button_go'],
)
# dashboard
login = layout(
    [
        [logo],
        [title1],
        [title2],
        [user],
        [password],
        [button_go]
    ],
)
login.name = 'login'
curdoc().add_root(login)
curdoc().title = 'PTM'
