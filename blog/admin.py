from django.contrib import admin
from .models import Post, Comment, Category

from django.utils.text import Truncator

class PostAdmin(admin.ModelAdmin):
    list_display   = ('title', 'slug', 'author', 'created_date', 'apercu_post')
    list_filter    = ('author','category',)
    date_hierarchy = 'created_date'
    ordering       = ('created_date', )
    search_fields  = ('title', 'text')
    prepopulated_fields = {'slug': ('title',), }

    #fields = ('title', 'author', 'category', 'text', 'created_date', 'published_date')
    # redondant avec fieldsets
    fieldsets = (
        # Fieldset 1 : meta-info (titre, auteur…)
        ('Meta datas', {
            'classes': ['collapse', ],
            'fields': ('title', 'slug', 'author', 'category', 'created_date', 'published_date')
        }),
        # Fieldset 2 : contenu de l'article
        ('Post text', {
            'classes': ['wide', ],
            'description': 'You can use html tags, enjoy ;) !',
            'fields': ('text',)
        }),
    )

    def apercu_post(self, post):
        """
        Retourne les 40 premiers caractères du contenu de l'article,
        suivi de points de suspension si le texte est plus long.
        """
        return Truncator(post.text).chars(40, truncate='...')

    apercu_post.short_description = 'Post preview'


admin.site.register(Post, PostAdmin)
admin.site.register(Comment)
admin.site.register(Category)