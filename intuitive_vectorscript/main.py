import vs

from intuitive_vectorscript.dialog import Dialog

dialog = Dialog("Test")
item1 = dialog.create_item(0, "TextField")
item2 = dialog.create_item(1, "PullDownMenu")
item3 = dialog.create_item(2, "TextField")
item4 = dialog.create_item(3, "PullDownMenu")
item3.set_default_value("asef")
arg = {0: "test", 1: "fsü"}
item2.add_choices(arg)
item4.add_choices(arg)
dialog.create_my_dialog()
