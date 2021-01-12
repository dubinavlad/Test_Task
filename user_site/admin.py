from . import models
from django.contrib import admin
from django.utils.safestring import mark_safe


@admin.register(models.Team)
class TeamAdmin(admin.ModelAdmin):
    def image_tag(self, obj):
        return mark_safe(
            '<img src="%s" width="150" height="150" />' % (obj.logo)
        )

    image_tag.short_description = "Logo"
    list_display = (
        "id",
        "name",
        "tag",
        "rating",
        "wins",
        "losses",
        "last_match_time",
        "opendota_team_id",
        "image_tag",
    )
    search_fields = ("name", "id", "opendota_team_id", "tag")
    ordering = ("rating",)
    sortable_by = (
        "name",
        "rating",
        "wins",
        "losses",
        "last_match_time",
    )
    fields = [
        "name",
        "tag",
        "rating",
        "wins",
        "losses",
        "last_match_time",
        "opendota_team_id",
        "image_tag",
    ]

    readonly_fields = ["image_tag"]
