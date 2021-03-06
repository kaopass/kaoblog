from django.apps import AppConfig as BaseConfig
from django.utils.translation import gettext_lazy as _


class TagsAppConfig(BaseConfig):
    name = "tags"
    verbose_name = _("Tags")
    default_auto_field = "django.db.models.AutoField"