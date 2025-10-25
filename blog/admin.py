from django.contrib import admin
from .models import Category,News,Flickr,Contact,Newsletter,Email
# Register your models here.
from django.contrib.auth.models import User


admin.site.register(Flickr)
admin.site.register(Contact)
admin.site.register(Newsletter)
admin.site.register(Email)


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'chop_etish', 'category', 'sana')
    list_filter = ('chop_etish','category')
    search_fields = ('title','category__name')
    list_per_page = 10
    readonly_fields = ()
class NewsInline(admin.TabularInline):
    model = News
    extra = 1

    prepopulated_fields = {"slug": ("title",)}
admin.site.unregister(User)
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    Inline = NewsInline
    prepopulated_fields = {"slug": ("name",)}
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'is_staff', 'is_superuser')



