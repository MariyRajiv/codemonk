from django.urls import path
from .views import authentication, views, search_views


app_name = "search"

urlpatterns = [
    path("", authentication.LoginView.as_view(), name="login"),
    path("register/", authentication.RegisterView.as_view(), name="register"),
    path("dashboard/", views.dashboard, name="dashboard"),
    path("logout/", authentication.LogoutView.as_view(), name="logout"),
    path(
        "reset_password/", authentication.reset_password, name="reset_password"
    ),
    path("verify_otp/", authentication.verify_otp, name="verify_otp"),
    path("submit/", search_views.SubmitView.as_view(), name="submit"),
    path("search/", search_views.SearchView.as_view(), name="search"),
    path("results/", search_views.SearchView.as_view(), name="results"),
    path("view_paragraphs/", search_views.view_paragraphs, name="view_paragraphs"),
]
