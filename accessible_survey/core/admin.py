from django.contrib import admin
from .models import Form, Question, Session, Answer


class AnswerInline(admin.TabularInline):
    model = Answer
    extra = 0
    readonly_fields = ('question_text', 'value')
    fields = ('question_text', 'value')

    def question_text(self, obj):
        return obj.question.text
    question_text.short_description = "Вопрос"


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
    list_display = (
        'id',
        'form_title',
        'source',
        'respondent_identifier',
        'contact_info',
        'started_at',
        'completed_at',
    )
    list_filter = ('form', 'source', 'started_at')
    search_fields = ('respondent_identifier',)
    readonly_fields = ('id', 'started_at', 'completed_at')
    inlines = [AnswerInline]

    def form_title(self, obj):
        return obj.form.title
    form_title.short_description = 'Форма'

    def contact_info(self, obj):
        answers = obj.answers.select_related('question')
        info = []
        for ans in answers:
            q_text = ans.question.text.lower()
            if 'телефон' in q_text:
                info.append(f"📞 {ans.value}")
            elif 'телеграм' in q_text or 'ник в телеграм' in q_text:
                info.append(f"💬 {ans.value}")
            elif 'email' in q_text or 'почта' in q_text:
                info.append(f"✉️ {ans.value}")
        return " | ".join(info) if info else "—"
    contact_info.short_description = "Контакты"
