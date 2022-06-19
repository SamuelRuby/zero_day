from django.apps import AppConfig


class BlogConfig(AppConfig):
    name = 'blog'
"""
a means of communicating, by telling django  that there is an app called blog
1. tells settings file about this activity, by including the name of the app in installed apps
2. tells manage.py about this activity, because then it calls settings.py
"""