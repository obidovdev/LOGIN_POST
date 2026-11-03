from django.shortcuts import render , get_object_or_404 , redirect
from .models import Post , Comments
from django.contrib.auth.decorators import login_required
from .forms import PostForm , CommentForm

@login_required
def post_list(request):
    posts = Post.objects.filter(is_active=True,).order_by('-created_at')
    context = {
        'posts': posts
    }
    return render(request, 'post_list.html', context)

@login_required
def post_detail(request, id):
    post = Post.objects.get(id=id)
    comments = Comments.objects.filter(post=post,is_active=True)
    if request.method == "POST":
        form = CommentForm(request.POST or None)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('post_detail', id=post.id)
    form = CommentForm()
    context = {
        'post': post,
        'form': form,
        'comments': comments
    }
    return render(request,'post_detail.html', context)





@login_required
def post_edit(request, id):
    user = request.user
    post = Post.objects.get(id=id)
    if request.method == 'POST':
        form = PostForm(request.POST or None, instance=post)
        if post.created_by != user:
            return render(request,'permission_denied.html')
        if form.is_valid():
            form.save()
            return render(request,'post_updated.html')
    else:
        form = PostForm(instance=post)
    context = {
        'form': form
    }
    return render(request,'post_edit.html', context)


@login_required
def post_delete(request,id):
    post = get_object_or_404(Post, id=id)
    if request.method == 'POST':
        post.is_active = False
        post.save()
        return redirect('post_list')
    context = {
        'post': post
    }
    return render(request,'post_delete.html', context)





