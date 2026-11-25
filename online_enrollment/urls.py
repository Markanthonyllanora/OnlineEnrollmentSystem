
from django.urls import path
from . import views

urlpatterns = [
    path(
        "",
        views.login_view,
        name="login"
    ),

    path(
        "skip-registration/",
        views.skip_registration,
        name="skip_registration"
    ),

    path(
        "dashboard/",
        views.dashboard_view,
        name="dashboard"
    ),

    path(
        "student/<int:student_id>/",
        views.student_detail,
        name="student_detail"
    ),

    path(
        "student/<int:student_id>/edit/",
        views.edit_student,
        name="edit_student"
    ),

    path(
        "logout/",
        views.logout_view,
        name="logout"
    ),
]
