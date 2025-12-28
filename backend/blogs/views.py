from django.shortcuts import render,HttpResponse
from .models import Blogs, Category
from django.shortcuts import get_object_or_404
from django.db.models import Q


def posts_by_category(request, category_id):
    # Fetch the posts that belong to the category with id category_id
    posts = Blogs.objects.filter(status='public', category=category_id)
    try:
     category = Category.objects.get(id=category_id)
    except:
        pass
    # category = get_object_or_404(Category, id=category_id)
    context = {
        'posts' : posts,
        'category' : category
    }
    return render(request, 'posts_by_category.html', context)


# blogs
def blogs(request, slug):
   single_post = get_object_or_404(Blogs, slug=slug, status='public')
   context = {
      'single_post' :single_post
   }
   return render(request, 'blogs.html', context)



#  search function
def search(request):
    keyword = request.GET.get('keyword')
    blogs = Blogs.objects.filter(Q(title__icontains=keyword) | Q(short_description__icontains=keyword) | Q(blog_body__icontains=keyword), status='public')
    content = {
        'blogs': blogs,
        'keyword': keyword
    }

    return render(request, 'search.html', content)