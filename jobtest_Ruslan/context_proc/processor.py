from django.conf import settings
def cont_settings(request):
    """
    Get context settings from settings file
    """
    
    return {"settings":settings}
