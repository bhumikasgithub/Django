from django.contrib import admin
from .models import chaiVarity, chaiReveiw, Store, chacertificte

# Register your models here.

class chaiReveiwInline(admin.TabularInline):
    model = chaiReveiw
    extra = 2


class chaiVarityAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'date_added')
    inlines = [chaiReveiwInline]

class storeAdmin(admin.ModelAdmin):
    list_display = ('name', 'location')
    filter_horizontal = ('chai_varities',)

class chacertificteAdmin(admin.ModelAdmin):
    list_display = ('chai', 'certificate_number', 'issue_date', 'valid_until')

admin.site.register(chaiVarity, chaiVarityAdmin)
admin.site.register(chaiReveiw)
admin.site.register(Store, storeAdmin)
admin.site.register(chacertificte, chacertificteAdmin)
