from django.shortcuts import render
from django.http import HttpResponse
import csv
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.utils import timezone
from .models import Form, Question, Session, Answer
from .serializers import QuestionSerializer


def form_view(request, form_id):
    form_obj = Form.objects.get(id=form_id)
    questions = form_obj.questions.all()
    return render(request, 'form.html',
                  {'questions': questions, 'form_id': form_id})


def export_answers(request, form_id):
    response = HttpResponse(content_type='text/csv')
    response[
        'Content-Disposition'] = f'attachment; filename="form_{form_id}_answers.csv"'
    writer = csv.writer(response)

    questions = Question.objects.filter(form_id=form_id).order_by('order')
    writer.writerow(['Сессия ID', 'Источник'] + [q.text for q in questions])

    sessions = Session.objects.filter(form_id=form_id,
                                      completed_at__isnull=False)
    for sess in sessions:
        answers = {a.question_id: a.value for a in sess.answers.all()}
        row = [sess.id, sess.source] + [answers.get(q.id, '') for q in
                                        questions]
        writer.writerow(row)

    return response


@api_view(['GET'])
def get_form_questions(request, form_id):
    questions = Question.objects.filter(form_id=form_id)
    serializer = QuestionSerializer(questions, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def submit_answers(request, form_id):
    session = Session.objects.create(
        form_id=form_id,
        source=request.data.get('source', 'web'),
        respondent_identifier=request.data.get('respondent_identifier', '')
    )

    answers = request.data.get('answers', [])
    for ans in answers:
        Answer.objects.create(
            session=session,
            question_id=int(ans['question_id']),
            value=ans['value']
        )

    session.completed_at = timezone.now()
    session.save()
    return Response({"status": "success", "session_id": session.id})
