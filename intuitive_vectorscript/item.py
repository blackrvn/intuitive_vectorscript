import vs


# Super Class Item, basic variables for all items in dialog
class Item:
	def __init__(self, dialog, item_id: int, item_type, chars):
		self.dialog = dialog
		self.item_id = item_id
		self.item_type = item_type
		self.chars = chars
		self.bounding_right = {"fixed_binding": True, "prop_binding": False}
		self.bounding_left = {"fixed_binding": True, "prop_binding": False}
		self.bounding_bottom = {"fixed_binding": False, "prop_binding": True}
		self.bounding_top = {"fixed_binding": False, "prop_binding": False}

	def activation(self):
		pass

	def set_alignment(self, alignment="r", mode="resize", alignment_id: int = 1):

		if alignment == "r":
			alignment = 1
		elif alignment == "bottom":
			alignment = 2
		elif alignment == "left":
			alignment = 3

		if mode == "resize":
			mode = 0
		else:
			mode = 1

		vs.AlignItemEdge(self.dialog.dialog_id, self.item_id, alignment, alignment_id, mode)

	def set_bounding(self, right: dict = None, left: dict = None, bottom: dict = None,
					 top: dict = None):
		if right is None:
			self.bounding_right = {"fixed_binding": True, "prop_binding": False}
		else:
			self.bounding_right = right
		if left is None:
			self.bounding_left = {"fixed_binding": True, "prop_binding": False}
		else:
			self.bounding_left = left
		if bottom is None:
			self.bounding_bottom = {"fixed_binding": False, "prop_binding": True}
		else:
			self.bounding_bottom = bottom
		if top is None:
			self.bounding_top = {"fixed_binding": False, "prop_binding": False}
		else:
			self.bounding_top = top

	def bounding(self):
		vs.SetEdgeBinding(self.dialog.dialog_id, self.item_id, self.bounding_left["fixed_binding"],
						  self.bounding_right["fixed_binding"], self.bounding_top["fixed_binding"],
						  self.bounding_bottom["fixed_binding"])
		vs.SetProportionalBinding(self.dialog.dialog_id, self.item_id, self.bounding_left["prop_binding"],
						  self.bounding_right["prop_binding"], self.bounding_top["prop_binding"],
						  self.bounding_bottom["prop_binding"])