import vs


def AddChoiceSample():
	# control IDs
	global kCreatePullDownMenu
	global kCreatePullDownMenu2
	global SetupDialogC
	global kCreateEditText
	kCreatePullDownMenu = 33
	kCreatePullDownMenu2 = 34
	kCreateEditText = 35
	SetupDialogC = 12255


def Dialog_Handler(item, data):
	if item == SetupDialogC:
		for index, database in enumerate(parameter.keys()):
			vs.AddChoice(dialog, kCreatePullDownMenu, database, index)
	elif item == kCreatePullDownMenu:
		vs.DeleteAllItems(dialog, kCreatePullDownMenu2)
		for field in parameter.get(vs.GetItemText(dialog, kCreatePullDownMenu)):
			vs.AddChoice(dialog, kCreatePullDownMenu2, field.field_name, 0)


def CreateMyDialog():
	global dialog
	dialog = vs.CreateResizableLayout('Add Choice Sample', 1, 'OK', 'Cancel', True, True)

	# {create controls}

	vs.CreatePullDownMenu(dialog, kCreatePullDownMenu, 24)
	vs.CreatePullDownMenu(dialog, kCreatePullDownMenu2, 24)
	vs.CreateEditText(dialog, kCreateEditText, "", 24)
	vs.CreateEditText(dialog, kCreateEditText, "", 24)

	# {set relations}
	vs.SetFirstLayoutItem(dialog, kCreatePullDownMenu)
	vs.SetBelowItem(dialog, kCreatePullDownMenu, kCreatePullDownMenu2, 25, -9)
	vs.SetBelowItem(dialog, kCreatePullDownMenu2, kCreateEditText, 25, -9)
	vs.NotifyPullDownClicked(dialog, kCreatePullDownMenu)
	vs.NotifyPullDownClicked(dialog, kCreatePullDownMenu2)

	if vs.RunLayoutDialog(dialog, Dialog_Handler) == 1:
		pass


kCreatePullDownMenu = 0
kCreatePullDownMenu2 = 0
kCreateEditText = 0
SetupDialogC = 0
dialog = 0


def main(data):
	global parameter
	parameter = data
	vs.AlrtDialog(str(data))
	AddChoiceSample()
	CreateMyDialog()
