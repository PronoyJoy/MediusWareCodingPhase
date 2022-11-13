from django.views import generic
from django.shortcuts import render,reverse
from product.models import ProductImage,Variant,Product,ProductVariantPrice,ProductVariant
from django.core.paginator import Paginator
from django.http import HttpResponseRedirect
class CreateProductView(generic.TemplateView):
    template_name = 'products/create.html'

    def get_context_data(self, **kwargs):
        context = super(CreateProductView, self).get_context_data(**kwargs)
        variants = Variant.objects.filter(active=True).values('id', 'title')
        context['product'] = True
        context['variants'] = list(variants.all())
        return context

# class ProductListView(generic.ListView):
#     context_object_name = 'variants'
#     model = ProductVariantPrice
#     template_name = 'products/list.html'

class PassVariant(generic.ListView):
    context_object_name = 'variants'
    model = ProductVariant
    template_name = 'products/filter.html'

def ProductListFilter(request): 
    product_data = Product.objects.all()
    variant_data = ProductVariant.objects.values('variant_title').distinct() #for dropdown filter
    product_variant_data = ProductVariantPrice.objects.all()
    product_image = ProductImage.objects.all()
    
    number_of_products = ProductVariant.objects.count()

    paginator = Paginator(product_variant_data,2) # Show 25 contacts per page.

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)


    return render( request, 'products/list.html',
                    
                    {
                        'product_data': product_data,
                        'variant_data' : variant_data,
                        'product_variant_data': product_variant_data,
                        'product_image' : product_image,
                        'number_of_products' : number_of_products,
                        'page_obj': page_obj


                    }

                 )

def ProductFilter(request):
    title =request.GET.get('title')
    variant =request.GET.get('variant')
    price_start =request.GET.get('price_start')
    price_finish =request.GET.get('price_finish')
    date = request.GET.get('date')


    filtered_data = ProductVariantPrice.objects.filter(product__title__contains = 'title')



  
    # filter_variant_one = filter(filtered_data__product_variant_one__contains ='variant[]')
    # filter_variant_two = filter(filtered_data__product_variant_two__contains ='variant[]')
    # filter_variant_three = filter(filtered_data__product_variant_three__contains ='variant[]')

    # if filter_variant_one != None:
    #     filter_price1 = filter(filter_variant_one__price = [ price_start, price_finish])
    #     filter_date1 = filter(filter_price1__date = 'date' )

    # if filter_variant_two != None:
    #     filter_price2 = filter(filter_variant_two__price = [ price_start, price_finish])
    #     filter_date2 = filter(filter_price2__date = 'date' )

    # if filter_variant_three != None:
    #     filter_price3 = filter(filter_variant_three__price = [ price_start, price_finish])
    #     filter_date3 = filter(filter_price3__date = 'date' )
    
    # if filter_date1 != None:
    #     final_data = filter_date1
    # if filter_date1 != None:
    #     final_data = filter_date2
    # if filter_date1 != None:
    #     final_data = filter_date3
    

   
    
    return render(request, 'products/filter.html',
                    
                    {
                        'final_data': final_data,
                    }


    
    
                )

	