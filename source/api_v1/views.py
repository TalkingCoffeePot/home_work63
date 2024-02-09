from rest_framework import viewsets
from django.shortcuts import render
from api_v1.serializers import PostModelSerializer
from feed.models import PostModel
from django.http import JsonResponse
from rest_framework.permissions import BasePermission

class IsAllowed(BasePermission):

    def find_post(self, id):
        return PostModel.objects.get(id=id)

    def url_parse(self, str):
        return int(str.split('/')[3])

    def has_permission(self, request, view):
        if request.user and request.user.is_authenticated:
            if view.action == 'partial_update' or view.action == 'destroy':
                if self.find_post(self.url_parse(request.path)) in request.user.usr_posts.all():
                    return True
                else: return False
            else: return True
        elif view.action == 'list' or view.action == 'retrieve':
            return True
        else: return False


class PostViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAllowed]
    queryset = PostModel.objects.all()
    serializer_class = PostModelSerializer

    def current_object(self):
        return self.get_object()

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
