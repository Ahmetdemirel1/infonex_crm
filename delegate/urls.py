from django.conf.urls import url
from . import views

app_name = 'delegate'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^update_crm_match_list/$', views.update_crm_match_list,
        name='update_crm_match_list'),
    url(r'^link_new_crm_record/$', views.link_new_crm_record,
        name='link_new_crm_record'),
    url(r'^update_tax_information/$', views.update_tax_information,
        name='update_tax_information'),
    url(r'^update_fx_conversion/$', views.update_fx_conversion,
        name='update_fx_conversion'),
    url(r'^update_cxl_info/$', views.update_cxl_info, name='update_cxl_info'),
    url(r'^update_payment_details/$', views.update_payment_details,
        name='update_payment_details'),
    url(r'^swap_sidebar/$', views.swap_sidebar, name='swap_sidebar'),
    url(r'^link_new_company_record/$', views.link_new_company_record,
        name='link_new_company_record'),
    url(r'^add_new_company/$', views.add_new_company, name='add_new_company'),
]
