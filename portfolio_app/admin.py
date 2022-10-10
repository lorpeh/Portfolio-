from django.contrib import admin
from .models import Category, Home,About,Profile, Skill,Portfolio

# Register your models here.
#Home Section
admin.site.register(Home)

#About Section
class Profileinline(admin.TabularInline):
    model = Profile
    extra: 1 #----This gives extra fields on my database
    
@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    inlines = [Profileinline,
    ]

#Skills
class Skillinline(admin.TabularInline):
    model = Skill
    extra: 2 #----This gives extra fields on my database
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    inlines = [Skillinline,
    ]

#portfolio
admin.site.register(Portfolio)

