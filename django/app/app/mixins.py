from django.views.generic.base import ContextMixin


class DataMixin(ContextMixin):
    title = None
    back_url = None

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.title is not None:
            context.update({"title": self.title})
        if self.back_url is not None:
            context.update({"back_url": self.back_url})
        return context


class FormMixin(DataMixin):
    button_text = None

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.button_text is not None:
            context.update({"button_text": self.button_text})
        return context
