from django.contrib import admin
from reversion.admin import VersionAdmin
from import_export import resources
from import_export.admin import ImportExportModelAdmin

from .models import Hint, Problem


class HintInline(admin.TabularInline):
    model = Hint
    fields = ("number", "keywords", "content")
    extra = 0


class PracticeExamIEResource(resources.ModelResource):
    class Meta:
        skip_unchanged = True
        model = Problem
        fields = (
            "id",
            "puid",
            "hyperlink",
        )


@admin.register(Problem)
class ProblemAdmin(ImportExportModelAdmin):
    list_display = (
        "id",
        "puid",
        "hyperlink",
    )
    list_display_links = (
        "id",
        "puid",
    )

    search_fields = ("puid",)
    list_per_page = 100
    inlines = (HintInline,)


@admin.register(Hint)
class HintAdmin(VersionAdmin):
    list_display = (
        "id",
        "problem",
        "number",
        "keywords",
        "content",
    )
    search_fields = (
        "number",
        "keywords",
        "content",
    )
    autocomplete_fields = ("problem",)
    list_per_page = 30
