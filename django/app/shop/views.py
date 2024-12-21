from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import FormView, ListView, DetailView

from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.renderers import JSONRenderer

from app.mixins import DataMixin, FormMixin
from .models import Material, Sell, Chart, File
from .forms import FileForm
from .factories import SellFactory
from .charts import generate_charts
from .serializers import MaterialSerializer


# Create your views here.
class MaterialListView(DataMixin, ListView):
    model = Material
    template_name = "shop/mat_list.html"
    context_object_name = "mats"

    title = "Список услуг"


class MaterialDetailView(DataMixin, DetailView):
    model = Material
    template_name = "shop/mat_detail.html"
    context_object_name = "mat"

    title = "Описание материала"
    back_url = "shop:mat-list"


class SellListView(DataMixin, ListView):
    model = Sell
    template_name = "shop/sells_list.html"
    context_object_name = "sells"

    title = "Фикстуры"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if not context["sells"].exists():
            context["sells"] = SellFactory.create_batch(50)
        return context


class ChartListView(DataMixin, ListView):
    model = Chart
    template_name = "shop/charts_list.html"
    context_object_name = "charts"

    title = "Графики"
    back_url = "shop:fixtures"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if not context["charts"].exists():
            context["charts"] = generate_charts()
        return context


class FileCreateView(FormMixin, FormView):
    form_class = FileForm
    template_name = "shop/files_form.html"
    success_url = reverse_lazy("shop:files-list")

    title = "Загрузка PDF файла"
    button_text = "Загрузить"

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class FileListView(DataMixin, ListView):
    model = File
    template_name = "shop/files_list.html"
    context_object_name = "files"

    title = "Список файлов"


def download_file(request, name):
    obj = get_object_or_404(File, name=name)
    response = HttpResponse(obj.file, content_type="application/force-download")
    response["Content-Disposition"] = f"attachment; filename={obj.file.name}"
    return response


class MaterialAPIListView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]

    queryset = Material.objects.all()
    serializer_class = MaterialSerializer


class MaterialAPIOneView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]

    queryset = Material.objects.all()
    serializer_class = MaterialSerializer
