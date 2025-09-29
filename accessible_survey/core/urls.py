from django.urls import path
from . import views

urlpatterns = [
    path('form/<int:form_id>/', views.form_view, name='form'),
    path('form/<int:form_id>/export/', views.export_answers,
         name='export_answers'),
    path('api/form/<int:form_id>/questions/', views.get_form_questions,
         name='get_questions'),
    path('api/form/<int:form_id>/submit/', views.submit_answers,
         name='submit_answers'),
]