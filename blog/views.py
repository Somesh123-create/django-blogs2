from django.shortcuts import render, get_object_or_404
from .models import Post, Comment
from django.views.generic import ListView, DetailView, CreateView
from .forms import CommentForm
from django.views import View
from django.http import HttpResponseRedirect
from django.urls import reverse
# Create your views here.


class StartingPageView(ListView):
    template_name = 'blog/home.html'
    model = Post
    queryset = Post.objects.all().order_by('-date')[:3]
    context_object_name = 'post'


# class StartingPageView(TemplateView):
#     template_name = 'blog/home.html'
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         latest_posts = Post.objects.all().order_by('-date')[:3]
#         context['post'] = latest_posts
#         return context


# def starting_page(request):
#     latest_posts = Post.objects.all().order_by('-date')[:3]
#     return render(request, 'blog/home.html', {'post':latest_posts})


class AllPostsView(ListView):
    model = Post
    template_name = 'blog/all_post.html'
    ordering = ('-date')
    context_object_name = 'post'


# def posts_page(request):
#     latest_post = Post.objects.all().order_by('-date')
#     return render(request, 'blog/all_post.html', {'post':latest_post})


class PostDetailView(View):

    def get(self, request, slug):
        posts = Post.objects.get(slug=slug)
        form = CommentForm
        context = {}

        stored_posts = request.session.get('stored_posts')
        if posts.id in stored_posts:
            context['stored'] = True
        else:
            context['stored'] = False

        context['posts'] = posts
        context['form'] = form
        context['comments'] = posts.comments.all().order_by('-id')
        return render(request, 'blog/post_detail.html', context)

    def post(self, request, slug):
        form = CommentForm(request.POST)
        posts = Post.objects.get(slug=slug)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.user_name = request.user
            comment.user_email = request.user.email
            comment.post = posts
            comment.save()
            return HttpResponseRedirect(reverse('post_detail_page', args=[slug]))

        context = {
            'posts': posts,
            'form': form,
            'form' : form,
            'comments': posts.comments.all().order_by('-id')
        }
        return render(request, 'blog/post_detail.html', context)



class ReadLaterView(View):

    def get(self, request):
        stored_posts = request.session.get('stored_posts')
        print(stored_posts)
        context = {}
        if stored_posts is None or len(stored_posts) == 0 :
            context['posts'] = []
            context['has_posts'] = False
        else:
            posts = Post.objects.filter(id__in=stored_posts)
            context['posts'] = posts
            context['has_posts'] = True
        return render(request, 'blog/stored_post.html', context)


    def post(self, request):
        stored_posts = request.session.get('stored_posts')
        if stored_posts is None:
            stored_posts = []
        post_id = int(request.POST["post_id"])

        if post_id not in stored_posts:
            stored_posts.append(post_id)

        else:
            stored_posts.remove(post_id)
        request.session['stored_posts'] = stored_posts
        print(post_id)
        print(stored_posts)
        return HttpResponseRedirect('/')




# def posts_deatail_page(request, slug):
#     identified_post = get_object_or_404(Post, slug=slug)
#     return render(request, 'blog/post_detail.html', {'posts':identified_post})
