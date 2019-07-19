from rest_framework import serializers
from .models import Article, Reporter

class ReporterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reporter
        #fields= ('id','name','n_articles')
        fields="__all__"

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        #fields = ('id','heading','body','image',)
        depth=2
        fields="__all__"
