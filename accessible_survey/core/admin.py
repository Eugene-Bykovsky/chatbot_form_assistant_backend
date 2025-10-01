from django.contrib import admin

from .models import Form, Question, Session, Answer


@admin.register(Form)
class FormAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('form', 'text', 'q_type', 'required', 'order')
    list_filter = ('form', 'q_type', 'required')
    ordering = ('form', 'order')


@admin.register(Session)
class SessionAdmin(admin.ModelAdmin):
    list_display = ('form', 'source', 'respondent_identifier', 'started_at', 'completed_at')
    list_filter = ('form', 'source')
    search_fields = ('respondent_identifier',)


@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = ('get_respondent_id', 'question', 'value', 'get_form_title')
    list_filter = ('session__form', 'question',
                   'session__respondent_identifier')
    search_fields = ('session__respondent_identifier', 'value')

    def get_respondent_id(self, obj):
        return obj.session.respondent_identifier
    get_respondent_id.short_description = 'Респондент ID'

    def get_form_title(self, obj):
        return obj.session.form.title
    get_form_title.short_description = 'Форма'
