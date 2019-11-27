from django.conf import settings

def site(request):
    return {
        'SITE_URL': settings.SITE_URL,
        'MEDIA_PATH': settings. SITE_URL + settings.MEDIA_URL
    }