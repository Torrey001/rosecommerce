from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

#model import
from .models import Product

# Create your views here.

def getProduct(request):
    if request.method =='GET':
        product=Product.objects.all()

        # converting the queryest called prodct to product_list
        product_list = list(product.values())

        print(product.values())

        return JsonResponse({
            "message": "Get product route is active",
             "data" : product_list               
                             })
    else:
        return JsonResponse({"message": "Invalid method"},status=405)
    
@csrf_exempt
def add_product(request):
    if request.method == "POST":
        #model syntax for adding products

        json_data = request.body.decode("utf-8")
        data_dict = json.loads(json_data)

        # Extract the product name from the data
        product_name =data_dict.get("name")

        # check if a product with the given name already exists
        existing_product = Product.objects.filter(name=product_name).first()
        if existing_product:
            # if the product exists, return a message indicting do
            return JsonResponse({"message": "Product with this name already exists" },status=405)
        else:
            Product.objects.create(**data_dict)

        return JsonResponse({
            "message": "Product added successfully"})
    else:
        return JsonResponse({"message": "invalidmethod"},status=405)
            
        # Product.objects.create(
        # name = data_dict["name"],
        # image_url = data_dict["image_url"],
        # description = data_dict["description"],
        # type = data_dict["type"],
        # brand = data_dict["brand"],
        # price = data_dict["price"],
        # available =data_dict["available"]
        # )

    #     Product.objects.create(**data_dict)

    #     return JsonResponse({
    # "message": "Post added successfully"})
# else:
#         return JsonResponse({"message": "invalidmethod"},status=405)
        # Product.objects.create(
        #     name = "Apple Watch Series 8",
        #     image_url ="https://www.ebay.com/itm/325984258982?chn=ps&norover=1&mkevt=1&mkrid=711-153320-877651-5&mkcid=2&itemid=325984258982&targetid=293946777986&device=c&mktype=pla&googleloc=1010294&poi=&campaignid=20797223261&mkgroupid=156754070580&rlsatarget=pla-293946777986&abcId=&merchantid=6296724&gad_source=1&gclid=CjwKCAjwvIWzBhAlEiwAHHWgvZlMdkTM40vCvpzX_M8XnvSOBjl3h7HDo64m5hwuyOa4NHMW7sdgNBoCYoEQAvD_BwE",
        #     description = "A trial will convince you",
        #     type = "Smart watch",
        #     brand = "Apple",
        #     price = 180000,
        #     available = "True",
        # )
    #     return JsonResponse({ "message": "post added successfully"})

    # else:
    #     return JsonResponse({"message": "invalid method"},status=405)



@csrf_exempt
def update_Product(request, pk):
    if request.method == "PUT":
        
        json_data = request.body.decode("utf-8")
        data_dict = json.loads(json_data)
        
        # product_id = data_dict.get(pk)

        existing_product = Product.objects.filter(id=pk).first()
        
        if existing_product:
            existing_product.name = data_dict.get("name", existing_product.name)
            existing_product.image_url = data_dict.get("image_url", existing_product.image_url)
            existing_product.type = data_dict.get("type", existing_product.type)
            existing_product.brand = data_dict.get("brand", existing_product.brand)
            existing_product.price = data_dict.get("price", existing_product.price)
            existing_product.description = data_dict.get("description", existing_product.description)
            existing_product.available = data_dict.get("available", existing_product.available)
            existing_product.save()
            
            return JsonResponse({"Message": "Product updated successfully"})
        else:
            return JsonResponse({"Message": "Product with this ID does not exist"})
    else:
        return JsonResponse({"ERROR": "Invalid Method"},status=405)
    

@csrf_exempt
def delete_Product(request, pk):
    if request.method == "DELETE":

        existing_product = Product.objects.filter(id=pk).first()
        
        if existing_product:
            existing_product.delete()
            
            return JsonResponse({"Message": "Product deleted successfully"})
        else:
            return JsonResponse({"Message": "Product with this ID does not exist"})
    else:
        return JsonResponse({"ERROR": "Invalid Method"},status=405)