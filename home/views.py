from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Post

def post_list(request):
    posts = Post.objects.all()
    search_query = request.GET.get('search', '')
    category_filter = request.GET.get('category', '')
    
    # Apply search filter
    if search_query:
        posts = posts.filter(title__icontains=search_query) | posts.filter(content__icontains=search_query)
    
    # Apply category filter
    if category_filter:
        posts = posts.filter(category=category_filter)
    
    # Pagination
    paginator = Paginator(posts, 5)  # 5 posts per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    categories = Post.CATEGORY_CHOICES
    
    return render(request, "home/index.html", {
        'page_obj': page_obj,
        'search_query': search_query,
        'category_filter': category_filter,
        'categories': categories,
    })