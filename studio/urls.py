from django.urls import path
from studio.views import (index,
                          JewelryTypeListView,
                          JewelryListView,
                          MasterListView,
                          MasterDetailView,
                          JewelryDetailView, JewelryTypeCreateView, JewelryTypeUpdateView, JewelryTypeDeleteView,
                          JewelryCreateView, JewelryUpdateView, MasterCreateView,
                          )

urlpatterns = [
    path('', index),
    path('jewelry_types/', JewelryTypeListView.as_view(), name='jewelry-type-list'),
    path('jewelry_types/create/', JewelryTypeCreateView.as_view(), name='jewelry-type-create'),
    path('jewelry_types/<int:pk>/update/', JewelryTypeUpdateView.as_view(), name='jewelry-type-update'),
    path('jewelry_types/<int:pk>/delete/', JewelryTypeDeleteView.as_view(), name='jewelry-type-delete'),
    path("jewelrys/", JewelryListView.as_view(), name='jewelry-list'),
    path("jewelrys/<int:pk>/", JewelryDetailView.as_view(), name='jewelry-detail'),
    path("jewelrys/create/", JewelryCreateView.as_view(), name='jewelry-create'),
    path("jewelrys/<int:pk>/update/", JewelryUpdateView.as_view(), name='jewelry-update'),
    path('masters/', MasterListView.as_view(), name='master-list'),
    path('masters/<int:pk>/', MasterDetailView.as_view(), name='master-detail'),
    path('masters/create/', MasterCreateView.as_view(), name='master-create'),
]

app_name = 'studio'