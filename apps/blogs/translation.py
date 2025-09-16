from modeltranslation.decorators import register
from modeltranslation.translator import TranslationOptions

from apps.blogs.models import BlogModel, BlogTagModel, BlogCategoryModel, BlogAuthorModel


@register(BlogModel)
class BlogTranslationOptions(TranslationOptions):
    fields = ('title', 'content',)


@register(BlogTagModel)
class BlogTagTranslationOptions(TranslationOptions):
    fields = ('title',)


@register(BlogCategoryModel)
class BlogCategoryTranslationOptions(TranslationOptions):
    fields = ('title',)


@register(BlogAuthorModel)
class BlogAuthorTranslationOptions(TranslationOptions):
    fields = ('full_name', 'bio',)
