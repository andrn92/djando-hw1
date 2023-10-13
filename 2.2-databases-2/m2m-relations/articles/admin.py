from django.contrib import admin
from django.forms import BaseInlineFormSet
from django.core.exceptions import ValidationError

from .models import Article, Tag, Scope


class ScopeInlineFormset(BaseInlineFormSet):
    def clean(self):
        list_values = []

        for form in self.forms:
            # В form.cleaned_data будет словарь с данными
            # каждой отдельной формы, которые вы можете проверить
            # form.cleaned_data:
            value = form.cleaned_data.get('is_main', 0)
            # вызовом исключения ValidationError можно указать админке о наличие ошибки
            # таким образом объект не будет сохранен,
            # а пользователю выведется соответствующее сообщение об ошибке
            if value:
                list_values.append(value)
        if not list_values or list_values.count(True) > 1:
            raise ValidationError('Error')
        return super().clean()  # вызываем базовый код переопределяемого метода


@admin.register(Scope)
class ScopeAdmin(admin.ModelAdmin):
    # list_display = ['article', 'tag', 'is_main']
    pass


class ScopeInline(admin.TabularInline):
    model = Scope
    extra = 1
    formset = ScopeInlineFormset


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    # list_display = ['title', 'text', 'published_at']
    # list_editable = ['text']
    inlines = (ScopeInline,)


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    inlines = (ScopeInline,)




