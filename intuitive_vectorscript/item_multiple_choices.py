from intuitive_vectorscript.item import Item
import vs


class MultipleChoicesItems(Item):

	def __init__(self, dialog, item_id: int, item_type, chars):
		super().__init__(dialog, item_id, item_type, chars)
		self.choices = None
		self.has_listener = True

	def add_choices(self, choices: dict):
		self.choices = choices

	def activation(self):
		if self.has_listener:
			vs.NotifyPullDownClicked(self.dialog.dialog_id, self.item_id)
		for item in self.choices.items():
			vs.AddChoice(self.dialog.dialog_id, self.item_id, item[1], item[0])


# Class PDMenu for pull down menu items
class PDMenu(MultipleChoicesItems):

	def __init__(self, dialog, item_id: int, item_type, chars):
		super().__init__(dialog, item_id, item_type, chars)
		self.has_search = False

	def set_has_search(self, has_search: bool):
		self.has_search = has_search

	def run(self):
		if self.has_search:
			vs.CreatePullDownSearch(self.dialog.dialog_id, self.item_id, self.chars)
		else:
			vs.CreatePullDownMenu(self.dialog.dialog_id, self.item_id, self.chars)


class ClassPDMenu(MultipleChoicesItems):

	def run(self):
		vs.CreateClassPullDownMenu(self.dialog.dialog_id, self.item_id, self.chars)

	def activation(self):
		pass


class LayerPDMenu(MultipleChoicesItems):

	def run(self):
		vs.CreateLayerPDMenu(self.dialog.dialog_id, self.item_id, self.chars)

	def activation(self):
		pass


class SheetLayerPDMenu(MultipleChoicesItems):

	def run(self):
		vs.CreateSheetLayerPullDownMenu(self.dialog.dialog_id, self.item_id, self.chars)

	def activation(self):
		pass


class EnhancedPDMenu(MultipleChoicesItems):

	def __init__(self, dialog, item_id: int, item_type, chars):
		super().__init__(dialog, item_id, item_type, chars)
		self.show_icon = True

	def run(self):
		vs.CreateEnhancedPullDownMenu(self.dialog.dialog_id, self.item_id, self.chars, self.show_icon)

	def set_icon_visibility(self, show_icon: bool):
		self.show_icon = show_icon

	def activation(self):
		pass
