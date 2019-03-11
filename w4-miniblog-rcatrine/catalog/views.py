from django.shortcuts import render
from django.views import generic

# Create your views here.
from catalog.models import Blog, Author, BlogInstance

def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    num_blogs = Blog.objects.all().count()
    num_instances = BlogInstance.objects.all().count()
    
    # Available books (status = 'a')
    num_instances_available = BlogInstance.objects.filter(status__exact='a').count()
    
    # The 'all()' is implied by default.    
    num_authors = Author.objects.count()

    # Number of visits to this view, as counted in the session variable.
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1
    
    context = {
        'num_blogs': num_blogs,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available,
        'num_authors': num_authors,
        'num_visits': num_visits,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)


class BlogListView(generic.ListView):
    model = Blog
    paginate_by = 3


class BlogDetailView(generic.DetailView):
    model = Blog


class AuthorListView(generic.ListView):
    model = Author
    paginate_by = 3


class AuthorDetailView(generic.DetailView):
    model = Author