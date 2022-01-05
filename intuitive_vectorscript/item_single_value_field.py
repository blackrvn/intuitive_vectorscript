from intuitive_vectorscript.item import Item
import vs


# Super class for value field, inherited of class 'Item'
class ValueField(Item):

	def __init__(self, dialog, item_id: int, item_type, chars):
		super().__init__(dialog, item_id, item_type, chars)
		self.default_value = ""
		self.is_editable = True

	def set_editable(self, is_editable: bool):
		self.is_editable = is_editable

	def activation(self):
		vs.EnableTextEdit(self.dialog.dialog_id, self.item_id, self.is_editable)


# class TextField for field items with string as input
class TextField(ValueField):

	@staticmethod
	def set_default_value(default_value: str):
		ValueField.default_value = default_value

	def run(self):
		vs.CreateEditText(self.dialog.dialog_id, self.item_id, self.default_value, self.chars)


# class IntegerField for field items with integer as input
class IntegerField(ValueField):

	@staticmethod
	def set_default_value(default_value: int):
		ValueField.default_value = default_value

	def run(self):
		vs.CreateEditInteger(self.dialog.dialog_id, self.item_id, self.default_value, self.chars)
