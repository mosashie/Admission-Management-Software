from django.urls import path
from main import views

app_name='main'

urlpatterns = [
    path('', views.selected_view,name='selected_view'),
    path('All/', views.list_view,name='list_view'),
    path('add/',views.add_std,name='add'),
    path('medical/',views.medical_std,name='medical_std'),
    path('med_slct/',views.med_slct,name='slct_med'),
    path('engineering/',views.Engr_std,name='Engr_std'),
    path('eng_slct/',views.eng_slct,name='slct_eng'),
    path('CS/',views.cs_std,name='cs_std'),
    path('cs_slct/',views.cs_slct,name='slct_cs'),
    path('Hum/',views.hum_std,name='hum_std'),
    path('hum_slct/',views.hum_slct,name='slct_hum'),

    # start local select #
    path('all_local_slct/',views.all_local_slct,name='all_local_slct'),
    path('med_local_slct/',views.med_local_slct,name='med_local_slct'),
    path('eng_local_slct/',views.eng_local_slct,name='eng_local_slct'),
    path('cs_local_slct/',views.cs_local_slct,name='cs_local_slct'),
    path('hum_local_slct/',views.hum_local_slct,name='hum_local_slct'),


    # end local select#
    #path('Disabled/'views.Disabled_stsd,name='Disabled_std'),
    #path('Sports/'views.Sports_std,name='Sports_std'),
    #start of local
    path('local_Hum/',views.local_hum,name='local_hum'),

    path('delete9/<int:pk>/',views.delete9,name='delete9'),
    path('select8/<int:pk>/',views.select8,name='select8'),


    path('local_CS/',views.local_comp,name='local_cs'),
    path('delete8/<int:pk>/',views.delete8,name='delete8'),
    path('select7/<int:pk>/',views.select7,name='select7'),

    path('local_Med/',views.local_med,name='local_med'),
    path('delete7/<int:pk>/',views.delete7,name='delete7'),
    path('select6/<int:pk>/',views.select6,name='select6'),

    path('local_Eng/',views.local_eng,name='local_eng'),
    path('delete6/<int:pk>/',views.delete6,name='delete6'),
    path('select5/<int:pk>/',views.select5,name='select5'),

    #this is end of local
    path('select1/<int:pk>/',views.select1,name='select1'),
    path('select2/<int:pk>/',views.select2,name='select2'),
    path('select3/<int:pk>/',views.select3,name='select3'),
    path('select4/<int:pk>/',views.select4,name='select4'),
    #for list and selected
    path('delete1/<int:pk>/',views.delete1,name='delete1'),
    #for medical
    path('delete2/<int:pk>/',views.delete2,name='delete2'),
    #for engr
    path('delete3/<int:pk>/',views.delete3,name='delete3'),
    #for cs
    path('delete4/<int:pk>/',views.delete4,name='delete4'),
    #for Humanite
    path('delete5/<int:pk>/',views.delete5,name='delete5'),

    path('search/',views.search,name='search'),
]
