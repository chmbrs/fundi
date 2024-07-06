from django.contrib import admin
from .models import Project, Investor, Investment, Update, Payment

admin.site.register(Project)
admin.site.register(Investor)
admin.site.register(Investment)
admin.site.register(Update)
admin.site.register(Payment)
