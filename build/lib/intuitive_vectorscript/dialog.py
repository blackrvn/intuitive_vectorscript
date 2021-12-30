import vs


class Dialog:

    def __init__(self, dialog_title, resizeable: bool = True, has_help: bool = False, button_name_default = "OK", button_name_cancel = "Cancel"):
        self.setup_dialog_c = 12255
        self.dialog_title = dialog_title
        self.dialog = self.create_layout(resizeable, has_help, button_name_default, button_name_cancel)
        self.items = []
        self.item_counter = 30

    def create_layout(self, resizeable, has_help, btn_1, btn_2):
        if resizeable:
            dialog = vs.CreateResizableLayout(self.dialog_title, has_help, btn_1, btn_2, True, True)
        else:
            dialog = vs.CreateLayout(self.dialog_title, has_help, btn_1, btn_2)
        return dialog

    def create_item(self, item_type: str, has_listener: bool = True):
        item = Item(self, self.item_counter, item_type)
        self.items.append(item)
        self.item_counter += 1

    def dialog_handler(self, item, data):
        if item == self.setup_dialog_c:
            pass
        elif item == kCreatePullDownMenu:
            pass

    def create_my_dialog(self):
        self.create_item("PullDownMenu")
        self.create_item("PullDownMenu")
        self.create_item("TextField")
        vs.SetFirstLayoutItem(self.dialog, 30)
        vs.SetBelowItem(self.dialog, 30, 31, 0, 0)
        vs.SetBelowItem(self.dialog, 31, 32, 0, 0)

        if vs.RunLayoutDialog(self.dialog, self.dialog_handler) == 1:
            pass


class Item:
    def __init__(self, dialog: Dialog, item_id: int, item_type):
        self.item_id = item_id
        self.item_type = item_type
        self.create(dialog, item_type)

    def create(self, dialog, item_type, chars=24):
        if item_type == "PullDownMenu":
            vs.CreatePullDownMenu(dialog.dialog, self.item_id, chars)
        if item_type == "TextField":
            vs.CreateEditText(dialog.dialog, self.item_id, "", chars)
