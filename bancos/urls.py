from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from bancos.views import AddBancoView

urlpatterns = {
        url(r'^add_banco/$', AddBancoView.as_view(), name='add_banco'),
        }

urlpatterns = format_suffix_patterns(urlpatterns)
