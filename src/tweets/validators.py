from django.core.exceptions import ValidationError

def validate_content(value):
	content = value
	if content == 'fuck':
		raise ValidationError('Don\'t Swear man')
	return value
