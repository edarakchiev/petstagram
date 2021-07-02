from django.contrib import admin

from petstagram_2.pets.models import Pet


class PetAdmin(admin.ModelAdmin):
    list_display = ['type', 'name', 'description']

    # def likes_count(self, obj):
    #     return obj.like_set.count()


admin.site.register(Pet, PetAdmin)