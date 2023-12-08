from django.urls import path

from to_do_list_app import views as to_do_list_app_views


urlpatterns = [
    path('', to_do_list_app_views.render_index, name='index'),
    path('tasks/create', to_do_list_app_views.create, name='create'),
    path('task/<int:pk>', to_do_list_app_views.render_detailed, name='detailed'),
    path('task/<int:pk>/update/', to_do_list_app_views.update, name='update'),
    path('task/<int:pk>/delete/', to_do_list_app_views.delete_view, name='task_delete')
]

