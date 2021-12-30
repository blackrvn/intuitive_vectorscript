import vs


class Dialog:

	setup_dialog_c = 12255

	def __init__(self, dialog_title, resizeable: bool = True, has_help: bool = False, button_name_default="OK",
				 button_name_cancel="Cancel"):

		self.control_ids = {}  # Container for the control IDS of the items in format 'control_ID = instance'
		self.item_base_id = 30  # Item counter for control IDs

		self.dialog_title = dialog_title
		self.dialog = self.create_layout(resizeable, has_help, button_name_default, button_name_cancel)  # Dialog handle

	def dialog_event_handler(self, item, data):
		if item == self.setup_dialog_c:
			pass

	def reset_choice_sample(self):
		for value in self.control_ids.values():
			self.control_ids[0] = value

	def create_layout(self, resizeable, has_help, btn_1, btn_2):
		if resizeable:
			dialog = vs.CreateResizableLayout(self.dialog_title, has_help, btn_1, btn_2, True, True)
		else:
			dialog = vs.CreateLayout(self.dialog_title, has_help, btn_1, btn_2)
		return dialog

	def create_item(self, index: int, item_type: str, is_group: bool = False, has_listener: bool = True):
		item = Item(self, self.item_base_id + index, item_type, is_group)
		self.control_ids[item.item_id] = item

	def create_my_dialog(self):
		vs.SetFirstLayoutItem(self.dialog, 30)
		vs.SetBelowItem(self.dialog, 30, 31, 0, 0)
		vs.SetBelowItem(self.dialog, 31, 32, 0, 0)

		if vs.RunLayoutDialog(self.dialog, self.dialog_handler) == 1:
			pass


class Item:
	def __init__(self, dialog: Dialog, item_id: int, item_type, is_group):
		self.is_group = is_group
		self.item_id = item_id
		self.item_type = item_type
		self.create(dialog, item_type)

	def create(self, dialog, item_type, chars=24):
		if item_type == "PullDownMenu":
			vs.CreatePullDownMenu(dialog.dialog, self.item_id, chars)
		if item_type == "TextField":
			vs.CreateEditText(dialog.dialog, self.item_id, "", chars)
