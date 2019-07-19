from .serializers import ArticleSerializer
from .serializers import ReporterSerializer
from .models import Article
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.db.models import Q

@api_view(['GET'])
def api_get_one_article(request):
    obj = Article.objects.first()

    if obj:
    	serializer = ArticleSerializer(obj)
    	return Response(serializer.data)
    else:
    	return Response({"Message": 'Article Not Foud'})

@api_view(['GET'])
def api_all_articles(request):
    all_articles = Article.objects.all()
    if all_articles:
    	serializer = ArticleSerializer(all_articles, many=True)
    	return Response(serializer.data)
    else:
    	return Response({"Message": 'Article Not Foud'})


@api_view(['GET'])
def api_get_article_id(request, _id):

    obj = Article.objects.filter(id = _id)[0]
    if obj:
    	serializer = ArticleSerializer(obj)
    	return Response(serializer.data)
    else:
    	return Response({"Message": 'Article Not Foud'})

@api_view(['GET'])
def api_get_articles_range(request, _range):
    print('===================>',_range)

    if ',' in _range:
        ids = [int(x) for x in _range.split(',')]
        all_articles = Article.objects.filter(id__in=ids)
        print(ids, len(all_articles))
    else:
        start, end = [int(x) for x in _range.split('-')]
        all_articles = Article.objects.filter(Q(id__lte = end) & Q(id__gte = start))


    if all_articles:
    	serializer = ArticleSerializer(all_articles, many=True)
    	return Response(serializer.data)
    else:
    	return Response({"Message": 'Article Not Foud'})
    


@api_view(['POST'])
def api_add_article(request):
    heading = request.POST.get("heading", None)
    body = request.POST.get("body", None)
    reporter_id = request.POST.get("reporter_id", None)
    article = Article.objects.create(heading=heading,
                                     body=body,
                                     reporter_id = reporter_id,
                                     image=request.FILES['image'])

    return Response({'message': 'article {:d} created'.format(article.id)}, status=301)
