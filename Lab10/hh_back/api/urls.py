
from django.urls import path
from . import views

urlpatterns = [
    # Class-based views
    path('companies/', views.CompanyList.as_view(), name='company-list'),
    path('companies/<int:pk>/', views.CompanyDetail.as_view(), name='company-detail'),
    path('vacancies/', views.VacancyList.as_view(), name='vacancy-list'),
    path('vacancies/<int:pk>/', views.VacancyDetail.as_view(), name='vacancy-detail'),
    path('companies/<int:id>/vacancies/', views.VacancyByCompanyList.as_view(), name='vacancy-by-company'),
    path('vacancies/top_ten/', views.TopTenVacancies.as_view(), name='top-ten-vacancies'),
    # Function-based views
    path('fb/companies/', views.company_list_fb, name='company-list-fb'),
    path('fb/companies/<int:pk>/', views.company_detail_fb, name='company-detail-fb'),
    path('fb/vacancies/', views.vacancy_list_fb, name='vacancy-list-fb'),
    path('fb/vacancies/<int:pk>/', views.vacancy_detail_fb, name='vacancy-detail-fb'),
]