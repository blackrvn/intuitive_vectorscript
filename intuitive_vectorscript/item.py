import vs


# Super Class Item, basic variables for all items in dialog
class Item:
	def __init__(self, dialog, item_id: int, item_type, chars):
		self.dialog = dialog
		self.item_id = item_id
		self.item_type = item_type
		self.chars = chars

	def activation(self):
		pass

	def set_alignment(self, alignment="r", mode="resize"):

		if alignment == "r":
			alignment = 1
		elif alignment == "b":
			alignment = 2
		elif alignment == "l":
			alignment = 3

		if mode == "resize":
			mode = 0
		else:
			mode = 1

		vs.AlignItemEdge(self.dialog.dialog_id, self.item_id, 1, 1, 0)
