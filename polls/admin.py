from django.contrib import admin
from .models import Question, Choice


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 0


class QuestionAdmin(admin.ModelAdmin):
    model = Question
    list_display = ('question_text', 'published_date', 'was_recently_published', 'author')
    list_filter = ('published_date', 'author')
    search_fields = ('question_text',)
    inlines = [
        ChoiceInline,
    ]


admin.site.register(Question, QuestionAdmin)
