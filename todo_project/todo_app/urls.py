from django.urls import path, include
from todo_app import views

urlpatterns = [

    path('', views.index, name='index'),
    path('delete/<int:id>', views.delete, name='delete'),
    # path('update/<int:id>', views.update, name='update'),
    path('cbvtask/', views.TaskListView.as_view(), name='cbvtask'),
    path('cbvdetail/<int:pk>/', views.TaskDetailView.as_view(), name='cbvdetail'),
    path('cbvupdate/<int:pk>/', views.TaskUpdateView.as_view(), name='cbvupdate'),
    path('cbvdelete/<int:pk>/', views.TaskDeleteView.as_view(), name='cbvdelete')

]
