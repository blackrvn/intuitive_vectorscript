import vs


def add_handle(criteria, obj):
	lst = []

	def create_instances(handle):
		lst.append(obj(handle))

	vs.ForEachObject(create_instances, criteria)
	return lst
