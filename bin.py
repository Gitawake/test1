from Box import *


body = LoginBody()
app = Tk()
app.title(body.Window_title)
app.geometry(body.Window_size)
body.login_ui(app)
app.mainloop()






