from django.contrib import admin
from .models import (Question, Option, Category, Quiz,CustomUser,QuizAttempt)

# 1. Setup Options to appear inside Questions
class OptionInline(admin.TabularInline):
    model = Option
    extra = 4  # Show 4 blank option rows by default

class QuestionAdmin(admin.ModelAdmin):
    inlines = [OptionInline]  # Connect Options to Question
    list_display = ('text', 'quiz', 'marks')# Columns to show in the list
    search_fields = ('text',) # Add a search bar
    list_filter = ('quiz',) # Add a filter sidebar

# 2. Setup Questions to appear inside Quizzes
class QuestionInline(admin.TabularInline):
    model = Question
    extra = 1
    show_change_link = True # Adds a link to edit the question fully

class QuizAdmin(admin.ModelAdmin):
    inlines = [QuestionInline] # Connect Questions to Quiz
    list_display = ('title', 'category', 'total_marks', 'time_limit')
    list_filter = ('category',)
    search_fields = ('title',)

# 3. Register the models
admin.site.register(CustomUser)
admin.site.register(Category)
admin.site.register(Option)
admin.site.register(Question,QuestionAdmin)
admin.site.register(Quiz,QuizAdmin) 
admin.site.register(QuizAttempt)
