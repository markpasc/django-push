from django.dispatch import Signal

updated = Signal(providing_args=['notification'])
updated_xml = Signal(providing_args=['notification'])
