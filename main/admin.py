from django_summernote.admin import SummernoteModelAdmin
from modeltranslation.admin import TabbedTranslationAdmin

class TabbedDjangoJquerySummernoteTranslationAdmin(SummernoteModelAdmin, TabbedTranslationAdmin):
    pass
