import os

django_settings_module = os.environ.get("DJANGO_SETTINGS_MODULE")
if django_settings_module is not None:
    django_settings_module = django_settings_module.split(".")[-1]
else:
    django_settings_module = "development"
