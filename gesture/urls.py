from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

from . import views

from gesture.views import TagListView

app_name = 'gesture'
urlpatterns = [
        path('reference/<int:ref_id>', views.reference ,name='reference'),
        path('tag/<int:tag_id>', views.tag ,name='tag'),
        path('', views.index ,name='index'),
        path('session', views.session ,name='session'),
        path('tag_list', TagListView.as_view(),name='tag_list'),
        path('add_tag_to_ref/<int:ref_id>', views.add_tag_to_ref ,name='add_tag_to_ref'),
        path('remove_tag_from_ref/<int:ref_id>', views.remove_tag_from_ref ,name='remove_tag_from_ref'),
        path('untagged_refs', views.untagged_refs, name='untagged_refs'),
        path('add_new_tag', views.add_new_tag ,name='add_new_tag'),
] 
#+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
