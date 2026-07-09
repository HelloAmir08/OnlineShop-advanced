from django.shortcuts import render, redirect, get_object_or_404
from .models import Category, SubCategory, Product
from .forms import ReviewForm
from django.core.paginator import Paginator


def homepage_view(request):
    products = (
        Product.objects
        .select_related('subcategory')
        .prefetch_related('images')
        .order_by('-created_at')
    )
    categories = Category.objects.all()
    subcategories = SubCategory.objects.all()

    subcategory_id = request.GET.get('subcategory')
    if subcategory_id:
        products = products.filter(subcategory_id=subcategory_id)

    q = request.GET.get('q', '').strip()
    if q:
        products = products.filter(name__icontains=q)

    sort = request.GET.get('sort')
    if sort == 'expensive':
        products = products.order_by('-price')
    elif sort == 'new':
        products = products.order_by('-created_at')
    elif sort == 'cheap':
        products = products.order_by('price')

    paginator = Paginator(products, 8)
    page_number = request.GET.get('page')
    products = paginator.get_page(page_number)

    context = {
        'products': products,
        'categories': categories,
        'subcategories': subcategories,
        'q': q,
        'sort': sort,
    }
    return render(request, 'shop/home.html', context)


def product_detail_view(request, pk):
    product = get_object_or_404(
        Product.objects.prefetch_related("images"),
        pk=pk,
    )
    reviews = product.reviews.order_by('-created_at')
    paginator = Paginator(reviews, 3)
    page_number = request.GET.get('page')
    reviews = paginator.get_page(page_number)
    if request.method == 'POST':
        form = ReviewForm(request.POST, user=request.user)
        if form.is_valid():
            review = form.save(commit=False)
            review.product = product

            if request.user.is_authenticated:
                review.user = request.user

            review.save()
            return redirect('product_detail', pk=pk)
    else:
        form = ReviewForm(user=request.user)

    context = {
        "product": product,
        'reviews': reviews,
        'form': form
    }

    return render(request, 'shop/product_detail.html', context)
