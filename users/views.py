from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, DestroyAPIView, UpdateAPIView
from rest_framework.viewsets import ModelViewSet

from users.models import User, Location
from users.serializers import UserCreateSerializer, LocationSerializer, UserSerializer, UserDeleteSerializer, \
    UserUpdateSerializer


class LocationViewSet(ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer


# class UserListView(ListView):
#     model = User
#     queryset = User.objects.all()
#
#     def get(self, request, *args, **kwargs):
#         super().get(self, *args, **kwargs)
#         self.object_list = self.object_list.order_by("username")
#         paginator = Paginator(object_list=self.object_list, per_page=settings.TOTAL_ON_PAGE)
#         page = request.GET.get('page')
#         page_obj = paginator.get_page(page)
#         result = []
#         for user in page_obj:
#             result.append(
#                 {"id": user.id,
#                  "username": user.username,
#                  "first_name": user.first_name,
#                  "last_name": user.last_name,
#                  "role": user.role,
#                  "ads_count": user.ads.count()
#                  })
#         return JsonResponse({'ads': result, 'page': page_obj.number, 'total': page_obj.paginator.count}, safe=False,
#                             json_dumps_params={'ensure_ascii': False})


# @method_decorator(csrf_exempt, name='dispatch')
# class UserCreateView(CreateView):
#     model = User
#     fields = ['username', 'password', 'first_name', 'last_name', 'role', 'locations']
#
#     def post(self, request, *args, **kwargs):
#         data = json.loads(request.body)
#
#         user = User.objects.create(
#             username=data['username'],
#             password=data['password'],
#             first_name=data['first_name'],
#             last_name=data['last_name'],
#             role=data['role']
#         )
#         for loc in data['locations']:
#             location, _ = Location.objects.get_or_create(name=loc)
#             user.location.add(location)
#
#         return JsonResponse({'id': user.id,
#                              'username': user.username,
#                              'first_name': user.first_name,
#                              'last_name': user.last_name,
#                              'role': user.role,
#                              'locations': [str(u) for u in user.location.all()]
#                              })

class UserCreateView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserCreateSerializer


class UserUpdateView(UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserUpdateSerializer


class UserListView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetailView(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDeleteView(DestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserDeleteSerializer
