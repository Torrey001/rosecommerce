from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

from .models import User

def getUser(request):
    if request.method =='GET':
        user=User.objects.all()

        # converting the queryest called prodct to user_list
        user_list = list(user.values())

        print(user.values())

        return JsonResponse({
            "message": "Get user route is active",
             "data" : user_list               
        })
    else:
        return JsonResponse({"message": "Invalid method"},status=405)

# Create your views here.
@csrf_exempt
def create_user(request):
    if request.method == "POST":
        #model syntax for adding products

        json_data = request.body.decode("utf-8")
        data_dict = json.loads(json_data)

        # Extract the product name from the data
        first_name = data_dict.get("first_name")
        last_name = data_dict.get("last_name")
        image = data_dict.get("image")

        # Validate the required fields
        if not first_name or not last_name:
            return JsonResponse({"message": "Missing required fields"}, status=400)

        # check if a product with the given name already exists
        existing_user = User.objects.filter(first_name=first_name, last_name=last_name).first()
        if existing_user:
            # if the product exists, return a message indicting do
            return JsonResponse({"message": "User with this details already exists" },status=405)
        else:
            # User.objects.create(**data_dict)
            # Create a new user
            User.objects.create(first_name=first_name, last_name=last_name, image=image)

        return JsonResponse({
            "message": "User added successfully"})
    else:
        return JsonResponse({"message": "invalidmethod"},status=405)
    

@csrf_exempt
def update_user(request, pk):
    if request.method == "PUT":
        
        json_data = request.body.decode("utf-8")
        data_dict = json.loads(json_data)

        existing_user = User.objects.filter(id=pk).first()
        
        if existing_user:

            new_first_name = data_dict.get("first_name", existing_user.first_name)
            new_last_name = data_dict.get("last_name", existing_user.last_name)
            new_image = data_dict.get("image", existing_user.image)

            if User.objects.filter(first_name=new_first_name, last_name=new_last_name).exclude(id=pk).exists():
                return JsonResponse({"Message": "User with this first name and last name already exists"}, status=409)

            # Update the user with the new data
            existing_user.first_name = new_first_name
            existing_user.last_name = new_last_name
            existing_user.image = new_image
            existing_user.save()
            
            return JsonResponse({"Message": "User updated successfully"})
        else:
            return JsonResponse({"Message": "User with this ID does not exist"})
    else:
        return JsonResponse({"ERROR": "Invalid Method"},status=405)
    

@csrf_exempt
def delete_user(request, pk):
    if request.method == "DELETE":

        existing_user = User.objects.filter(id=pk).first()
        
        if existing_user:
            existing_user.delete()
            
            return JsonResponse({"Message": "User deleted successfully"})
        else:
            return JsonResponse({"Message": "User with this ID does not exist"})
    else:
        return JsonResponse({"ERROR": "Invalid Method"},status=405)