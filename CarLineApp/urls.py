from django.urls import path     
from . import views


urlpatterns = [
    path("", views.index),
    path("register", views.register),
    path("login", views.login),
    path("riders", views.all_riders),
    path("riders/show_all", views.all_riders),
    path("riders/create", views.create),
    path("riders/add_rider", views.add_rider),
    path("riders/<int:rider_id>/pickup", views.pickup),
    path("riders/<int:rider_id>", views.show_one),
    path("school/carline", views.carline),
    # path('riders/<int:rider_id>', views.edit_rider),
    # path("riders/<int:rider_id>/delete", views.delete),
    path("logout", views.logout),
]