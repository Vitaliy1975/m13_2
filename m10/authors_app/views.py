from django.shortcuts import render,redirect,get_object_or_404
from .forms import TagForm,AuthorForm,QuoteForm
from django.contrib.auth.decorators import login_required
from .models import Author,Quote

# Create your views here.
def main(request):
    authors = Author.objects.all()
    return render(request, 'authors_app/index.html',{"authors":authors})

@login_required
def tag(request):
    if request.method == 'POST':
        form = TagForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(to='authors_app:main')
        else:
            return render(request, 'authors_app/tag.html', {'form': form})

    return render(request, 'authors_app/tag.html', {'form': TagForm()})


@login_required
def author(request):
    if request.method=="POST":
        form=AuthorForm(request.POST)
        if form.is_valid():
            author=form.save(commit=False)
            author.save()
            return redirect(to="authors_app:main")
        else:
            return render(request,"authors_app/author.html",{"form":form})
    return render(request,"authors_app/author.html",{"form":AuthorForm()})


@login_required
def quote(request):
    authors = Author.objects.all()

    if request.method == 'POST':
        form = QuoteForm(request.POST)
        if form.is_valid():
            new_quote = form.save(commit=False)
            choice_aut = Author.objects.filter(fullname__in=request.POST.getlist('authors'))
            new_quote.author = choice_aut.first()
            new_quote.save()
            return redirect(to='authors_app:main')
        else:
            return render(request, 'authors_app/quote.html', {"authors": authors, 'form': form})
    return render(request, 'authors_app/quote.html', {"authors": authors, 'form': QuoteForm()})


def author_details(request,pk):
    author = get_object_or_404(Author, pk=pk)
    quotes=Quote.objects.filter(author_id=author.id)
    context = {
        'fullname': author.fullname,
        'born_date': author.born_date,
        'born_location': author.born_location,
        'description': author.description,
        'quotes':quotes
    }
    return render(request, 'authors_app/author_detail.html', context)