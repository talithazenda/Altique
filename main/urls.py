from django.urls import path
from main.views import show_json, show_json_by_id, show_main, show_xml, show_xml_by_id, add_item_barang, show_items, register, login, logout, edit_item_barang, delete_item_barang, add_item_barang_ajax, items_list, create_item_flutter

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('items/', show_items, name='show_items'),
    path('add/', add_item_barang, name='create_item'), 
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
    path('xml/<uuid:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<uuid:id>/', show_json_by_id, name='show_json_by_id'),
    path('register/', register, name='register'),
    path('edit-item/<uuid:id>/', edit_item_barang, name='edit_item_barang'),
    path('delete-item/<uuid:id>/', delete_item_barang, name='delete_item_barang'),
    path('add-item-ajax/', add_item_barang_ajax, name='add_item_barang_ajax'),  # Consolidate AJAX handling here
    path('register/', register, name='register'),
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),
    path('items/', items_list, name='items_list'),
    path('create-flutter/', create_item_flutter, name='create_flutter'),

]
