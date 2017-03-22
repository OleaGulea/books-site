from django import forms
from ckeditor.widgets import CKEditorWidget

from books_site.books.models import Chapter


class ChapterForm(forms.ModelForm):
    title = forms.CharField()
    text = forms.CharField(widget=CKEditorWidget())
    order = forms.IntegerField()

    class Meta:
        model = Chapter
        fields = ['title', 'text', 'order']
