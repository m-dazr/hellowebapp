from django.forms import ModelForm
from collection.models import Post


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'text',)