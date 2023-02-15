from django.contrib import admin

# Register your models here.
from MovieApp.models import Movies;
class MoviesAdmin(admin.ModelAdmin):
    list_display = ['releasedate','moviename','actor','actress','ratings'];

admin.site.register(Movies,MoviesAdmin);