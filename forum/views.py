from django.utils import timezone
from django.shortcuts import render, redirect, get_object_or_404
from django.http import Http404
from django.urls import reverse
from . import models
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from django.views.generic import View, UpdateView
from django.utils.decorators import method_decorator

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .forms import NewTopicForm, NewThreadForm, NewPostForm

# Create your views here.
# TODO:
# create post view + edit + delete
# tak samo thread i topic
# user view
# login, register etc

# home with topic boards to choose from
def home_view(request):
    topics = models.Topic.objects.all()

    queryset = topics.order_by('-date_created')
    paginator = Paginator(queryset, 10)
    page = request.GET.get('page', 1)

    try:
        topics = paginator.page(page)
    except PageNotAnInteger:
        #not a number
        #fallback to first page
        topics = paginator.page(1)
    except EmptyPage:
        # page number too large
        #fallback to last page
        topics = paginator.page(paginator.num_pages)

    # element do wyswietlania genric elementu paginacji
    paginate = topics
    
    context = {'topics': topics,
               'paginate': paginate}

    return render(request, "forum/home.django-html", context)

def about_view(request):
    context = {'links': [
                   {
                       'name': 'About',
                       'link': reverse('forum:about')
                   }
               ]}
    return render(request, "forum/about.django-html",
           context)

def topic_view(request, topic_slug):
    try:
        topic = get_object_or_404(models.Topic, slug=topic_slug)
    except Http404:
        return redirect('forum:home')
    link_string = reverse('forum:topic', kwargs={'topic_slug':topic_slug})

    # threads = list(topic.threads.all())
    queryset = topic.threads.order_by('-date_created')
    
    paginator = Paginator(queryset, 10)
    page = request.GET.get('page', 1)

    try:
        threads = paginator.page(page)
    except PageNotAnInteger:
        #not a number
        #fallback to first page
        threads = paginator.page(1)
    except EmptyPage:
        # page number too large
        #fallback to last page
        threads = paginator.page(paginator.num_pages)

    # element do wyswietlania genric elementu paginacji
    paginate = threads

    links = [{
        'name': topic.name,
        'link': link_string
    }]
    context = {'topic': topic,
               'links': links,
               'threads': threads,
               'paginate': paginate}
    return render(request, "forum/topic.django-html", context)

def thread_view(request, topic_slug, thread_slug):
    try:
        topic = get_object_or_404(models.Topic, slug=topic_slug)
    except Http404:
        return redirect('forum:home')
    topic_link_string = reverse('forum:topic', kwargs={'topic_slug':topic_slug})

    try:
        thread = get_object_or_404(models.Thread, slug=thread_slug)
    except Http404:
        return redirect('forum:home')
    thread_link_string = reverse('forum:thread', kwargs={'topic_slug':topic_slug, 'thread_slug': thread_slug})
    
    posts = thread.posts.all()
    # print(posts[0].author.profile.bio)

    thread.view_count+=1
    thread.save()

    # pagination
    queryset = thread.posts.order_by('-date_created')
    
    paginator = Paginator(queryset, 10)
    page = request.GET.get('page', 1)

    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    # element do wyswietlania genric elementu paginacji
    paginate = posts

    # breadcrumbs links
    links = [{
        'name': topic.name,
        'link': topic_link_string
        },
        {
        'name': thread.name,
        'link': thread_link_string
        }
        ]
    context = {'thread': thread,
               'links': links,
               'posts': posts,
               'paginate': paginate
               }
    return render(request, "forum/thread.django-html", context)

@login_required(login_url='accounts:login')
def new_topic(request):
    if request.method == 'POST':
        form = NewTopicForm(request.POST)
        user = User.objects.first()

        if form.is_valid():
            topic = form.save(commit=False)
            #wlasne pole, z modelu z related field
            topic.author = user
            topic.save()

            request.user.profile.post_count += 1
            request.user.save()

            return redirect('forum:home')
    else:
        form = NewTopicForm()
    return render(request, 'forum/new_topic_form_crispy.django-html', {'form': form})


@login_required(login_url='accounts:login')
class NewTopicView(View):
    def render(self, request):
        return render(request, 'forum/new_topic_form_crispy.django-html', {'form': form})
    def post(self, request):
        form = NewTopicForm(request.POST)
        user = User.objects.first()

        if form.is_valid():
            topic = form.save(commit=False)
            #wlasne pole, z modelu z related field
            topic.author = user
            topic.save()

            request.user.profile.post_count += 1
            request.user.save()

            return redirect('forum:home')
        return self.render(request)
    
    def get(self, request):
        form = NewTopicForm()
        return self.render(request)
        # return render(request, 'forum/new_topic_form_crispy.django-html', {'form': form})

@login_required(login_url='accounts:login')
def new_thread(request, topic_slug):
    try:
        topic = get_object_or_404(models.Topic, slug=topic_slug)
    except Http404:
        return redirect('forum:home')
    
    # user = User.objects.first()
    if request.method == 'POST':
        form = NewThreadForm(request.POST)
        if form.is_valid():
            thread = form.save(commit=False)
            #wlasne pola, z modelu z related field
            thread.author = request.user
            thread.topic = topic
            thread.save()

            #dodatkowo tworzony initial obiekt post w thread
            post = models.Post.objects.create(
                author = request.user,
                content = form.cleaned_data.get('content'),
                thread=thread
            )

            # oraz aktualizacja zliczania
            topic.thread_count += 1
            topic.last_thread_date = timezone.now()
            topic.save()
            request.user.profile.thread_count += 1
            request.user.profile.save()

            return redirect('forum:thread', topic_slug=topic_slug, thread_slug=thread.slug)
    else:
        form = NewThreadForm()
    return render(request, 'forum/new_thread.django-html', {'form': form})

@login_required
def new_post(request, topic_slug, thread_slug):
    try:
        thread = get_object_or_404(models.Thread, slug=thread_slug)
    except Http404:
        return redirect('forum:home')
    
    posts = list(reversed(thread.posts.all()))[:10]

    if request.method == 'POST':
        form = NewPostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.thread = thread
            post.save()

            #aktualizacja zliczen
            thread.post_count +=1
            thread.last_reply_date = timezone.now()
            thread.save()
            request.user.profile.post_count += 1
            request.user.profile.save()

            return redirect('forum:thread', topic_slug=thread.topic.slug, thread_slug=thread_slug)
    else:
        form = NewPostForm()
    return render(request, 'forum/new_post.django-html', {'form': form,
                                                          'thread': thread,
                                                          'posts': posts})

@method_decorator(login_required, name='dispatch')
class PostUpdateView(UpdateView):
    model = models.Post
    fields = ('content', )
    template_name = 'forum/edit_post.django-html'
    slug_url_kwarg = 'post_slug'
    context_object_name = 'post'

    # backendowe zabezpiecznie przed uzytkownikami edytujacymi nie swoje posty?
    # mimo ze nie maja takiej mozliwosci frontendowo oferowanej
    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(author=self.request.user)

    def form_valid(self, form):
        post = form.save(commit=False)
        post.date_updated = timezone.now()
        post.save()
        return redirect('forum:thread',
                         topic_slug=post.thread.topic.slug,
                         thread_slug=post.thread.slug,
                        #  post_slug=post.topic.board.slug
                         )

@login_required()
def like_post_view(request, topic_slug, thread_slug, post_slug):
    try:
        post = get_object_or_404(models.Post, slug=post_slug)
    except Http404:
        return redirect('forum:home')
    try:
        thread = get_object_or_404(models.Post, slug=post_slug)
    except Http404:
        return redirect('forum:home')
    user = request.user
    if request.method == 'POST':
        post_slug = request.POST.get('slug')
        
        if user in post.liked_by.all():
            post.liked_by.remove(user)
            post.like_count -=1
            post.author.profile.reputation -=1
        else:
            post.liked_by.add(user)
            post.like_count +=1
            post.author.profile.reputation +=1
        
        # print('post_liked_by: ', post.liked_by.all())
        post.save()
        user.profile.save()
        return redirect('forum:thread',
                        topic_slug=topic_slug,
                        thread_slug=thread_slug)
@login_required()
def delete_post_view(request, post_slug):
    try:
        post = get_object_or_404(models.Post, slug=post_slug)
    except Http404:
        return redirect('forum:home')
    topic_slug = post.thread.topic.slug
    thread_slug = post.thread.slug
    post.delete()
    return redirect('forum:thread',
                    topic_slug=topic_slug,
                    thread_slug=thread_slug)
    