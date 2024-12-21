from django import forms
from .models import File


class FileForm(forms.ModelForm):
    class Meta:
        model = File
        fields = ("file",)
        labels = {"file": "Выберите файл"}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.label_suffix = ""

    file_accept = [".pdf"]

    def clean_file(self):
        file = self.cleaned_data["file"]
        if file:
            ext = "." + file.content_type.split("/")[1]
            if ext not in self.file_accept:
                raise forms.ValidationError("Файл должен иметь тип .pdf")
            if File.objects.filter(name=file.name).exists():
                raise forms.ValidationError("Данный файл уже был загружен")
        return file

    def save(self, commit=...):
        model = super().save(commit=False)
        file = self.cleaned_data["file"]
        model.name = file.name
        return super().save(commit)
