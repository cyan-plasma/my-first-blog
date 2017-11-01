from django.conf.urls import url
from django.contrib import admin
import web.views
 
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^data.json$', web.views.data_json),
    url(r'^$', web.views.main_page),
]
