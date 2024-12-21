from django.contrib.auth import get_user_model, login
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import FormView, ListView

from rest_framework import generics
from rest_framework.permissions import IsAdminUser

from app.settings import LOGIN_REDIRECT_URL
from app.mixins import DataMixin, FormMixin
from .forms import RegisterForm, SettingsForm
from .utils import save_user_data, get_data, get_cookie_data
from .serializers import UserSerializer


# Create your views here.
class Login(FormMixin, LoginView):
    template_name = "users/form.html"
    title = "Страница входа"
    button_text = "Войти"

    class Meta:
        model = get_user_model()
        fields = ["login", "password"]


class Register(FormMixin, FormView):
    form_class = RegisterForm

    template_name = "users/form.html"
    title = "Страница регистрации"
    button_text = "Зарегистрироваться"

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return super().form_valid(form)

    success_url = LOGIN_REDIRECT_URL


class Logout(LoginRequiredMixin, LogoutView):
    http_method_names = ["get"]

    def get(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)


class UserList(LoginRequiredMixin, PermissionRequiredMixin, DataMixin, ListView):
    permission_required = "auth.view_user"
    template_name = "users/user_list.html"
    title = "Список пользователей"

    queryset = get_user_model().objects.all()
    context_object_name = "users"


class SettingsView(LoginRequiredMixin, FormMixin, FormView):
    template_name = "users/settings.html"
    title = "Настройки пользователя"
    button_text = "Применить"

    success_url = reverse_lazy("users:settings")

    form_class = SettingsForm

    def get_initial(self):
        initial = super().get_initial()
        initial["theme"], initial["lang"] = get_data(self.request.user.username)
        return initial

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["userdata"] = context["form"].initial
        context["cookiedata"] = get_cookie_data(self.request)
        return context

    def form_valid(self, form):
        save_user_data(
            self.request.user.username,
            form.cleaned_data["theme"],
            form.cleaned_data["lang"],
        )
        return super().form_valid(form)


class UserAPIListCreateView(generics.ListCreateAPIView):
    permission_classes = [IsAdminUser]

    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer


class UserAPIView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAdminUser]

    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
