import intuitive_vectorscript as ivs
import vs


class Dialog:
	setup_dialog_c = 12255

	def __init__(self, dialog_title, resizeable: bool = True, has_help: bool = False, button_name_default="OK",
				 button_name_cancel="Cancel"):

		self.control_ids = {}  # Container for the control IDS of the items in format 'control_ID = instance'
		self.item_base_id = 30  # Item counter for control IDs

		self.dialog_title = dialog_title
		self.dialog_id = self.create_layout(resizeable, has_help, button_name_default,
											button_name_cancel)  # Dialog handle

	def dialog_event_handler(self, item, data):
		if item == self.setup_dialog_c:
			for instance in self.control_ids.values():
				instance.activation()

	def reset_choice_sample(self):
		for key in self.control_ids.keys():
			self.control_ids[0] = self.control_ids.pop(key)

	def create_layout(self, resizeable, has_help, btn_1, btn_2):
		if resizeable:
			dialog = vs.CreateResizableLayout(self.dialog_title, has_help, btn_1, btn_2, True, True)
		else:
			dialog = vs.CreateLayout(self.dialog_title, has_help, btn_1, btn_2)
		return dialog

	def create_item(self, index: int, item_type: str, chars: int = 24, has_listener: bool = True):

		def instantiate_item(item_class):
			item = item_class(self, self.item_base_id + index, item_type, chars)
			self.control_ids[item.item_id] = item
			return item

		if item_type == "TextField":
			item_inst = instantiate_item(ivs.TextField)
			return item_inst
		elif item_type == "IntegerField":
			item_inst = instantiate_item(ivs.IntegerField)
			return item_inst
		elif item_type == "PDMenu":
			item_inst = instantiate_item(ivs.PDMenu)
			return item_inst
		elif item_type == "EnhancedPDMenu":
			item_inst = instantiate_item(ivs.EnhancedPDMenu)
			return item_inst
		elif item_type == "ClassPDMenu":
			item_inst = instantiate_item(ivs.ClassPDMenu)
			return item_inst
		elif item_type == "LayerPDMenu":
			item_inst = instantiate_item(ivs.LayerPDMenu)
			return item_inst
		elif item_type == "SheetLayerPDMenu":
			item_inst = instantiate_item(ivs.SheetLayerPDMenu)
			return item_inst

	def set_dialog_order(self):
		vs.SetFirstLayoutItem(self.dialog_id, self.item_base_id)
		for cid in self.control_ids.keys():
			vs.SetBelowItem(self.dialog_id, cid, cid + 1, 0, 0)

	def create_my_dialog(self):
		for instance in self.control_ids.values():
			instance.run()
			instance.set_alignment()
		self.set_dialog_order()
		if vs.RunLayoutDialog(self.dialog_id, self.dialog_event_handler) == 1:
			pass
