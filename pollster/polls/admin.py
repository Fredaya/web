from django.contrib import admin

from .models import Question, Choice

admin.site.site_header ="HOT QUESTIONS"
admin.site.site_title ="QWINS Admin Area"
admin.site.index_title ="Welcome to QWINS Admin area"

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    search_fields = ['title', 'content']
    fieldsets = [(None, {'fields': ['question_text']}),
    ('Date Information', {'fields': ['pub_date'], 'classes': ['collapse']}),]
    inlines = [ChoiceInline]

# admin.site.register(Question)
# admin.site.register(Choice)
admin.site.register(Question, QuestionAdmin)
