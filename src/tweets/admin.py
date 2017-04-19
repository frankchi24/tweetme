from django.contrib import admin
from .models import Tweet
from .forms import TweetModelForm

class TweetModelAdmin(admin.ModelAdmin):
    form = TweetModelForm



# Register your models here.
admin.site.register(Tweet,TweetModelAdmin)
