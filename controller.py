
import view
import data

def button_click():
    name = view.set_name()
    surname = view.set_surname()
    phone = view.set_phone()
    description = view.set_description()

    data.init(name, surname, phone, description)
    data.add_member(name, surname, phone, description)
    view.view_data(name, surname, phone, description)