from django.contrib import admin
from creation.models import *
# Register your models here.

admin.site.register(Writer)
admin.site.register(Branch)


class VoteAdmin(admin.ModelAdmin):
    list_display = ('writer_vote', 'branch_vote')

admin.site.register(Vote, VoteAdmin)