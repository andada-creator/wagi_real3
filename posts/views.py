from rest_framework import viewsets, filters
from .models import Post, PostImage
from .serializers import PostSerializer
from django.shortcuts import render, get_object_or_404, redirect

# posts/views.py




class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by('-created_at')
    serializer_class = PostSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['title']  # 제목에 대해 검색 가능하게 설정



def post_list(request):
    search_query = request.GET.get('search', '')  # GET 파라미터에서 'search' 값을 받아옴

    if search_query:
        posts = Post.objects.filter(title__icontains=search_query).order_by('-created_at')
    else:
        posts = Post.objects.all().order_by('-created_at')

    return render(request, 'posts/post_list.html', {'posts': posts})


#def post_list(request):
    #posts = Post.objects.all().order_by('-created_at')
    #return render(request, 'posts/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'posts/post_detail.html', {'post': post})

def post_create(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        post = Post.objects.create(title=title, content=content)
        
        images = request.FILES.getlist('images')
        for image in images:
            PostImage.objects.create(post=post, image=image)
        
        return redirect('post_list')
    return render(request, 'posts/post_create.html')


def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        post.title = request.POST.get('title')
        post.content = request.POST.get('content')
        post.save()
        return redirect('post_detail', pk=post.pk)
    return render(request, 'posts/post_edit.html', {'post': post})

def post_delete(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        post.delete()
        return redirect('post_list')
    return redirect('post_detail', pk=post.pk)
