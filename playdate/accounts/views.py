from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.http import HttpResponse
from django.urls import reverse_lazy, reverse
from django.views import generic as views
from django.contrib.auth import views as auth_views, login, get_user_model

from playdate.accounts.forms import RegisterUserForm, LoginUserForm

UserModel = get_user_model()


class OnlyAnonymousMixin:
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return HttpResponse(self.get_success_url())

        return super().dispatch(request, *args, **kwargs)


class RegisterUserView(OnlyAnonymousMixin, views.CreateView):
    template_name = "accounts/register.html"
    form_class = RegisterUserForm
    success_url = reverse_lazy("index")

    def form_valid(self, form):
        result = super().form_valid(form)
        login(self.request, self.object)

        return result

    def form_invalid(self, form):
        return super().form_invalid(form)

    def get_success_url(self):
        return self.success_url


class LoginUserView(auth_views.LoginView):
    template_name = "accounts/login-page.html"
    form_class = LoginUserForm


class LogoutUserView(auth_views.LogoutView):
    pass


@method_decorator(login_required, name='dispatch')
class ProfileDetailsView(views.DetailView):
    template_name = "accounts/profile-details.html"
    model = UserModel


class ProfileDetailsViewVisit(views.DetailView):
    template_name = "accounts/profile-details-visit.html"
    model = UserModel


@method_decorator(login_required, name='dispatch')
class ProfileEditView(views.UpdateView):
    template_name = "accounts/profile-edit.html"
    model = UserModel
    fields = [
        "username",
        "first_name",
        "last_name",
        "email",
        "gender",
        "profile_picture",
    ]

    def get_success_url(self):
        return reverse("profile details", kwargs={"pk": self.object.pk})


@method_decorator(login_required, name='dispatch')
class ProfileDeleteView(views.DeleteView):
    template_name = "accounts/profile-delete.html"
    model = UserModel
    success_url = reverse_lazy("index")
