from django.urls import path
from main.views import show_json, show_json_by_id, show_main, show_xml, show_xml_by_id, add_item_barang, show_items

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('items/', show_items, name='show_items'),
    path('add/', add_item_barang, name='add_item_barang'),
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
    path('xml/<uuid:id>/', show_xml_by_id, name='show_xml_by_id'),  # Changed to uuid
    path('json/<uuid:id>/', show_json_by_id, name='show_json_by_id'),  # Changed to uuid
]
