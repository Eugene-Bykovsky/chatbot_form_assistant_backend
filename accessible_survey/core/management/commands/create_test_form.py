from django.core.management.base import BaseCommand
from core.models import Form, Question

class Command(BaseCommand):
    help = 'Создаёт тестовую форму по макету хакатона'

    def handle(self, *args, **options):
        Form.objects.all().delete()
        self.stdout.write('Удалены все существующие формы.')

        form = Form.objects.create(
            title="Заявка на содействие в трудоустройстве"
        )
        self.stdout.write(f'Создана форма: {form.title}')

        questions_data = [
            {"text": "Фамилия Имя Отчество", "q_type": "text", "required": True, "hint": "", "options": ""},
            {"text": "Город, район", "q_type": "text", "required": False, "hint": "", "options": ""},
            {"text": "Дата рождения", "q_type": "date", "required": True, "hint": "ДД.ММ.ГГГГ", "options": ""},
            {"text": "Ваш запрос", "q_type": "select", "required": True, "hint": "", "options": "профориентация|поиск работы|обучение,стажировка|консультация|самозанятость"},
            {"text": "Ваш запрос. Комментарии", "q_type": "textarea", "required": False, "hint": "Опишите, какую работу вы ищете...", "options": ""},
            {"text": "Телефон", "q_type": "text", "required": True, "hint": "Начните с +7", "options": ""},
            {"text": "Группа инвалидности", "q_type": "select", "required": True, "hint": "", "options": "1 группа|2 группа|3 группа|Инвадид детства"},
            {"text": "Форма инвалидности", "q_type": "select", "required": True, "hint": "", "options": "Общее заболевание|ПОДА|Передвигается на инвалидной коляске"},
            {"text": "Образование", "q_type": "select", "required": True, "hint": "", "options": "Школа|Среднее специальное|Высшее|Неоконченное высшее"},
            {"text": "Образование. Подробности", "q_type": "textarea", "required": False, "hint": "Где и чему обучались. Специальность. Курсы", "options": ""},
            {"text": "Электронная почта", "q_type": "text", "required": False, "hint": "", "options": ""},
            {"text": "Дополнительная информация", "q_type": "textarea", "required": False, "hint": "Расскажите о своих интересах, увлечениях", "options": ""},
            {"text": "Страница в ВК", "q_type": "text", "required": False, "hint": "", "options": ""},
            {"text": "Ник в Телеграм", "q_type": "text", "required": False, "hint": "", "options": ""},
            {"text": "Принимаю условия обработки персональных данных", "q_type": "checkbox", "required": True, "hint": "", "options": "Да"}
        ]

        for i, q_data in enumerate(questions_data, start=1):
            Question.objects.create(
                form=form,
                text=q_data["text"],
                q_type=q_data["q_type"],
                required=q_data["required"],
                hint=q_data["hint"],
                options=q_data["options"],
                order=i
            )
            self.stdout.write(f'  Добавлен вопрос: {q_data["text"]}')

        self.stdout.write(
            self.style.SUCCESS(
                f'\n✅ Тестовая форма успешно создана!\n'
                f'ID формы: {form.id}\n'
                f'Откройте: http://127.0.0.1:8000/form/{form.id}/'
            )
        )
