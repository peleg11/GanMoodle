from django.core.exceptions import ValidationError

def file_size(value):
    filesize=value.size
    if filesize>30000000:
        raise ValidationError("max size of file is 30 MB")
