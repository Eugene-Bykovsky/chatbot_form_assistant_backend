from django.db import models


class Form(models.Model):
    title = models.CharField(max_length=200,
                             default='Заявка на содействие в трудоустройстве')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Question(models.Model):
    TEXT = 'text'
    TEXTAREA = 'textarea'
    SELECT = 'select'
    CHECKBOX = 'checkbox'
    DATE = 'date'

    TYPE_CHOICES = [
        (TEXT, 'Текст'),
        (TEXTAREA, 'Текстовое поле'),
        (SELECT, 'Выпадающий список'),
        (CHECKBOX, 'Галочка'),
        (DATE, 'Дата'),
    ]

    form = models.ForeignKey(Form, related_name='questions',
                             on_delete=models.CASCADE)
    text = models.CharField(max_length=500)
    q_type = models.CharField(max_length=20, choices=TYPE_CHOICES,
                              default=TEXT)
    options = models.TextField(blank=True, help_text='Варианты через |')
    required = models.BooleanField(default=False)
    order = models.PositiveIntegerField(default=0)
    hint = models.CharField(max_length=500, blank=True)

    class Meta:
        ordering = ['order']

    def get_options_list(self):
        if self.q_type in ['select', 'checkbox'] and self.options:
            return [opt.strip() for opt in self.options.split('|')]
        return []


class Session(models.Model):
    form = models.ForeignKey(Form, on_delete=models.CASCADE)
    started_at = models.DateTimeField(auto_now_add=True)
    completed_at = models.DateTimeField(null=True, blank=True)
    source = models.CharField(max_length=20, default='web')
    respondent_identifier = models.CharField(
        max_length=255,
        blank=True,
        help_text='Идентификатор респондента (Telegram ID, UUID, email и т.д.)'
    )


class Answer(models.Model):
    session = models.ForeignKey(Session, related_name='answers',
                                on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    value = models.TextField()
