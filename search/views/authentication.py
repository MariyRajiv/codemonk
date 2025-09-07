from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from django.http import (
    HttpResponse,
    HttpResponsePermanentRedirect,
    HttpResponseRedirect,
)
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.cache import never_cache

from ..forms import (
    EmailForm,
    LoginForm,
    PasswordResetForm,
    RegistrationForm,
    UsernameForm,
)
from ..utils.email_utils import (
    generate_otp,
    send_email_to_user,
    send_verification_otp_email,
)


@method_decorator(never_cache, name="post")
class LoginView(View):
    def get(self, request) -> HttpResponse:
        request.session.flush()
        return render(request, "search/login.html", {"form": LoginForm()})

    def post(
        self, request
    ) -> HttpResponseRedirect | HttpResponsePermanentRedirect:
        form = LoginForm(request.POST)
        if form.is_valid():
            username = request.POST.get("username")
            password = request.POST.get("password")
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect(reverse("search:dashboard"))
            else:
                messages.error(request, "Invalid username or password.")
                return redirect("search:login")
        else:
            messages.error(request, "Invalid form submission.")
            return redirect("search:login")


@method_decorator(never_cache, name="post")
class RegisterView(View):
    def get(self, request) -> HttpResponse:
        if request.session.get("email_otp_sent", None):
            return render(
                request, "search/register.html", {"form": RegistrationForm()}
            )
        else:
            return render(
                request, "search/register.html", {"form": EmailForm()}
            )

    def post(
        self, request
    ) -> HttpResponseRedirect | HttpResponsePermanentRedirect:
        if not request.session.get("email_otp_sent", None):
            email = request.POST.get("email")
            try:
                validate_email(email)
            except ValidationError:
                messages.error(request, "Invalid email address.")
                return redirect("search:register")

            if send_verification_otp_email(email, request):
                request.session["email"] = email
                messages.success(request, "OTP sent to your email.")
                return redirect(reverse("search:register"))

            messages.error(request, "Failed to send OTP.")
            return redirect("search:register")

        else:
            return user_registration(request)


class LogoutView(View):
    def get(
        self, request
    ) -> HttpResponseRedirect | HttpResponsePermanentRedirect:
        logout(request)
        return redirect(reverse("search:login"))


@never_cache
def user_registration(
    request,
) -> HttpResponseRedirect | HttpResponsePermanentRedirect:
    if request.method != "POST":
        return redirect("search:register")

    username = request.POST.get("username")
    email = request.session.get("email")
    otp = request.POST.get("otp")
    session_otp = request.session.get("otp")
    if not session_otp or otp != session_otp:
        messages.error(request, "Invalid OTP.")
        return redirect("search:register")

    password = request.POST.get("password")
    confirm_password = request.POST.get("confirm_password")
    if password == confirm_password:
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists.")
            return redirect("search:register")
        user = User.objects.create_user(
            username=username, password=password, email=email
        )
        user.save()

        messages.success(
            request, "Registration successful. You can now log in."
        )
        return redirect(reverse("search:login"))

    else:
        messages.error(
            request, "Registration failed. Please check your details."
        )
        return redirect("search:register")


@never_cache
def reset_password(request):
    if request.method == "POST":
        form = UsernameForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            user = User.objects.filter(username=username).first()
            if not user:
                messages.error(request, "User not found.")
                return redirect(reverse("search:reset_password"))
            request.session["user"] = user.username
            user_email = user.email
            print(f"User email: {user_email}")

            otp = generate_otp()
            status = send_email_to_user(
                "Password Reset OTP",
                f"Your OTP for password reset is: {otp}",
                [user_email],
            )
            if status:
                request.session["otp"] = otp
                request.session["email_otp_sent"] = True
                messages.success(request, f"OTP sent to {user_email}.")
                return redirect(reverse("search:reset_password"))
            else:
                messages.error(request, "Failed to send email.")
        else:
            messages.error(request, "Invalid form submission.")
    else:
        if request.session.get("email_otp_sent", None):
            form = PasswordResetForm()
        else:
            form = UsernameForm()
    return render(request, "search/password_reset.html", {"form": form})


@never_cache
def verify_otp(request):
    if request.method != "POST":
        return redirect("search:reset_password")

    otp = request.POST.get("otp")
    if otp != request.session.get("otp"):
        messages.error(request, "Invalid OTP.")
        return redirect("search:reset_password")

    user = get_object_or_404(User, username=request.session.get("user"))

    new_password = request.POST.get("new_password")
    confirm_password = request.POST.get("confirm_password")
    if new_password == confirm_password:
        user.set_password(new_password)
        user.save()

        messages.success(
            request, "Password reset successful. You can now log in."
        )
        request.session.flush()
        return redirect(reverse("search:login"))
    else:
        messages.error(request, "Passwords do not match.")
        return redirect("search:reset_password")
