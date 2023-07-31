from django.http import HttpResponse
from django.templatetags.static import static
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
    template_name = "accounts/register-page.html"
    form_class = RegisterUserForm
    success_url = reverse_lazy("index")

    def form_valid(self, form):
        result = super().form_valid(form)

        login(self.request, self.object)

        return result

    def form_invalid(self, form):
        return super().form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["next"] = self.request.GET.get("next", "")

        return context

    def get_success_url(self):
        if 'next' in self.request.POST:
            return self.request.POST["next"]
        return self.success_url


class LoginUserView(auth_views.LoginView):
    template_name = "accounts/login-page.html"
    form_class = LoginUserForm


class LogoutUserView(auth_views.LogoutView):
    pass


class ProfileDetailsView(views.DetailView):
    template_name = "accounts/profile-details-page.html"
    model = UserModel

    profile_image = static("images/person02.svg")

    def get_profile_image(self):
        if self.object.profile_picture is not None:
            return self.object.profile_picture
        return self.profile_image

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["profile_image"] = self.get_profile_image()

        return context


class ProfileEditView(views.UpdateView):
    template_name = "accounts/profile-edit-page.html"
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


class ProfileDeleteView(views.DeleteView):
    template_name = "accounts/profile-delete-page.html"
    model = UserModel
    success_url = reverse_lazy("index")