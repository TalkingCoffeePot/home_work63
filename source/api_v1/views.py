from rest_framework import viewsets
from django.shortcuts import render
from api_v1.serializers import PostModelSerializer
from feed.models import PostModel
from django.http import JsonResponse


class PostViewSet(viewsets.ModelViewSet):
    queryset = PostModel.objects.all()
    serializer_class = PostModelSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)



def post_like_view(request):
    post = PostModel.objects.get(id=request.POST.get('postid'))
    print(request.path)
    icon = ''
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        icon = '<i class="bi bi-heart text-danger fs-2"></i>'
    else:
        post.likes.add(request.user)
        icon = '<i class="bi bi-heart-fill text-danger fs-2"></i>'
    return JsonResponse({'count': post.likes.count(), 'icon': icon})
