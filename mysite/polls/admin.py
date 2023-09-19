from django.contrib import admin

from .models import Choice, Question


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {"fields": ["question_text"]}),
        ("Date information", {"fields": ["pub_date"], "classes": ["collapse"]}),
    ]
    # Makes choice objects to be editable within their Question admin page.
    inlines = [ChoiceInline]
    # adds properties of Question that will be displayed in the summary admin view of all questions.
    list_display = ["question_text", "pub_date", "was_published_recently"]
    # adds a filter sidebar
    list_filter = ["pub_date"] 
    # adds search box and searches question_text field to find user input.
    search_fields = ["question_text"]


admin.site.register(Question, QuestionAdmin)