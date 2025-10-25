
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse



from akkount.models import Profile
from blog.forms import EmailForm
from blog.models import News, Category, Flickr, ViewCount

from django.views.generic import CreateView,UpdateView,DeleteView

# Create your views here.
def index(request):
    is_admin = False
    if request.user.is_authenticated:
        profile = Profile.objects.get(user=request.user)
        if profile.role == 'admin':
            is_admin = True
    if request.method == 'POST':
        form = EmailForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("email qabul qilindi")
        else:
            return HttpResponse("email qabul qilinmadi")



    news = News.objects.all().filter(chop_etish=True).order_by('-sana')
    category = Category.objects.all()
    flickr = Flickr.objects.all()
    car = news.filter(joylash='car')
    right = news.filter(joylash='right')
    feat = news.filter(joylash='feat')
    lat = news.filter(joylash='lat')
    tran = news.filter(joylash='tran')
    lat2 = lat[4:6]
    lat3 = lat[6:8]
    lat4 = lat[8:10]
    lat5 = lat[10:12]

    context = {
        'cat': categoriya,

        'news': news,
        'category': category,
        'flickr': flickr,
        'car': car,
        'right': right,
        'feat': feat,
        'lat': lat,
        'tran': tran,
        'lat2': lat2,
        'lat3': lat3,
        'lat4': lat4,
        'lat5': lat5,
        'is_admin': is_admin,
    }

    return render(request, 'index.html', context=context)

def category(request):
    categoriya = "News"
    news = News.objects.all().filter(chop_etish=True).order_by('-sana').filter(joylash='lat')
    tran = News.objects.all().filter(chop_etish=True).order_by('-sana').filter(joylash='tran')
    category = Category.objects.all()
    context = {
        'categoriya': categoriya,
        'lat': news,
        'tran': tran,
        'category': category,
    }

    return render(request, 'category.html',context=context)
def contact(request):
    return render(request, 'contact.html',context={})
def single(request):
    return render(request, 'single.html',context={})
@login_required
def detail(request, slug):

    news = get_object_or_404(News, slug=slug)
    comments = news.comments.all().order_by('-created_at')


    user = request.user
    if not ViewCount.objects.filter(user=user, news=news).exists():
        ViewCount.objects.create(user=user, news=news)
        news.view_count += 1
        news.save()


    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.news = news
            comment.user = request.user
            comment.save()
            return redirect('news_detail', pk=news.pk)
    else:
        form = CommentForm()

    context = {
        'object': news,
        'comments': comments,
        'form': form,
    }



    return render(request, 'detail.html',context=context)
class NewsCreateView(CreateView):
        model = News
        template_name = "crud/news_create.html"
        fields = "__all__"
        success_url = "/"

class NewsUpdateView(UpdateView):
        model = News
        template_name = "crud/news_update.html"
        fields = "__all__"
        success_url = "/"

class NewsDeleteView(DeleteView):
        model = News
        template_name = "crud/news_delete.html"
        success_url = "/"

from django.shortcuts import render, get_object_or_404, redirect
from .models import News, Comment
from .forms import CommentForm

def news_detail(request, pk):
    news = get_object_or_404(News, pk=pk)
    comments = news.comments.all().order_by('-created_at')

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.news = news
            comment.user = request.user
            comment.save()
            return redirect('news_detail', pk=news.pk)
    else:
        form = CommentForm()

    context = {
        'object': news,
        'comments': comments,
        'form': form,
    }
    return render(request, 'detail.html', context)

def search_news(request):
    yangilik = News.objects.all().filter(chop_etish=True).order_by('-sana')
    query = request.GET.get('q')
    news = []

    if query:
        news = yangilik.filter(
            title__icontains=query
        ) | yangilik.filter(
            text__icontains=query
        ) | yangilik.filter(
            category__name__icontains=query
        )
        is_admin = False
        if request.user.is_authenticated:
            profile = Profile.objects.get(user=request.user)
            if profile.role == 'admin':
                is_admin = True
        if request.method == 'POST':
            form = EmailForm(request.POST)
            if form.is_valid():
                form.save()
                return HttpResponse("email qabul qilindi")
            else:
                return HttpResponse("email qabul qilinmadi")




        category = Category.objects.all()
        flickr = Flickr.objects.all()
        car = news.filter(joylash='car')
        right = news.filter(joylash='right')
        feat = news.filter(joylash='feat')
        lat = news.filter(joylash='lat')
        tran = news.filter(joylash='tran')
        lat2 = lat[4:6]
        lat3 = lat[6:8]
        lat4 = lat[8:10]
        lat5 = lat[10:12]

        context = {
            'cat': categoriya,

            'category': category,
            'flickr': flickr,
            'car': car,
            'right': right,
            'feat': feat,
            'lat': lat,
            'tran': tran,
            'lat2': lat2,
            'lat3': lat3,
            'lat4': lat4,
            'lat5': lat5,
            'is_admin': is_admin,
            'query': query,
            'news': news
        }

    return render(request, 'index.html', context={})
def categoriya(request, slug):
    categoriya = Category.objects.get(slug=slug)
    news = News.objects.filter(category=categoriya)
    lat = news.filter(joylash='lat')
    tran = news.filter(joylash='tran')
    categoriya = categoriya.name
    category = Category.objects.all()
    context = {
        'categoriya': categoriya,
        'lat':lat,
        'tran': tran,
        'category': category,
    }

    return render(request, 'category.html', context=context)
