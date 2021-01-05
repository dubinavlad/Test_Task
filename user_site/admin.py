from . import models
from django.contrib import admin, messages


@admin.register(models.Team)
class TeamAdmin(admin.ModelAdmin):
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
