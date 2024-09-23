from django.core.exceptions import ValidationError
from urllib.parse import urlparse

def validate_youtube_link(value):
    parsed_url = urlparse(value)
    if 'youtube.com' not in parsed_url.netloc:
        raise ValidationError("Ссылка должна вести на youtube.com")