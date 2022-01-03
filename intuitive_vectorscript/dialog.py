import vs


class Dialog:
	setup_dialog_c = 12255

	def __init__(self, dialog_title, resizeable: bool = True, has_help: bool = False, button_name_default="OK",
				 button_name_cancel="Cancel"):

		self.control_ids = {}  # Container for the control IDS of the items in format 'control_ID = instance'
		self.items_which_need_activation = []
		self.item_base_id = 30  # Item counter for control IDs

		self.dialog_title = dialog_title
		self.dialog_id = self.create_layout(resizeable, has_help, button_name_default,
											button_name_cancel)  # Dialog handle

	def dialog_event_handler(self, item, data):
		if item == self.setup_dialog_c:
			if len(self.items_which_need_activation) > 0:
				for instance in self.items_which_need_activation:
					instance.run_choices()

	def reset_choice_sample(self):
		for value in self.control_ids.values():
			self.control_ids[0] = value

	def create_layout(self, resizeable, has_help, btn_1, btn_2):
		if resizeable:
			dialog = vs.CreateResizableLayout(self.dialog_title, has_help, btn_1, btn_2, True, True)
		else:
			dialog = vs.CreateLayout(self.dialog_title, has_help, btn_1, btn_2)
		return dialog

	def create_item(self, index: int, item_type: str, is_group: bool = False, chars: int = 24,
					has_listener: bool = True):
		if item_type == "TextField":
			item = TextField(self, self.item_base_id + index, item_type, is_group, chars)
			self.control_ids[item.item_id] = item
			return item
		elif item_type == "PullDownMenu":
			item = PullDownMenu(self, self.item_base_id + index, item_type, is_group, chars)
			self.control_ids[item.item_id] = item
			self.items_which_need_activation.append(item)
			return item

	def set_dialog_order(self):
		vs.SetFirstLayoutItem(self.dialog_id, self.item_base_id)
		for cid in self.control_ids.keys():
			vs.SetBelowItem(self.dialog_id, cid, cid + 1, 0, 0)

	def create_my_dialog(self):
		for instance in self.control_ids.values():
			instance.run()
		self.set_dialog_order()
		if vs.RunLayoutDialog(self.dialog_id, self.dialog_event_handler) == 1:
			pass


class Item:
	def __init__(self, dialog: Dialog, item_id: int, item_type, is_group, chars):
		self.dialog = dialog
		self.is_group = is_group
		self.item_id = item_id
		self.item_type = item_type
		self.chars = chars


class TextField(Item):

	def __init__(self, dialog: Dialog, item_id: int, item_type, is_group, chars):
		super().__init__(dialog, item_id, item_type, is_group, chars)
		self.default_value = ""
		self.is_editable = True

	def set_default_value(self, default_value):
		self.default_value = default_value

	def run(self):
		vs.CreateEditText(self.dialog.dialog_id, self.item_id, self.default_value, self.chars)

	def change_editable(self):
		if self.is_editable:
			self.is_editable = False
			vs.SetTextEditable(self.item_id, False)
		else:
			self.is_editable = True
			vs.SetTextEditable(self.item_id, True)


class PullDownMenu(Item):

	def __init__(self, dialog: Dialog, item_id: int, item_type, is_group, chars):
		super().__init__(dialog, item_id, item_type, is_group, chars)
		self.choices = None

	def run(self):
		vs.CreatePullDownMenu(self.dialog.dialog_id, self.item_id, self.chars)

	def add_choices(self, choices: dict):
		self.choices = choices

	def return_choices(self):
		for choice in self.choices.items():
			return choice

	def run_choices(self):
		for item in self.choices.items():
			vs.AddChoice(self.dialog.dialog_id, self.item_id, item[1], item[0])
