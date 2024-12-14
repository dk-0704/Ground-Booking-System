"""GroundBookingsystem URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls.static import static
from django.urls import path
from groundapp import views as v
from customerapp import views as c
from ownerapp import views as o

from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', v.index, name="index"),
    path('about/', v.about, name="about"),
    path('gallery/', v.gallery, name="gallery"),
    path('events/', v.events, name="events"),
    path('contact/', v.contact, name="contact"),
    path('single/', v.single, name="single"),
    path('players/', v.players, name="players"),
    path('customer_login/', v.customer_login, name="customer_login"),
    path('customer_register/', v.customer_register, name="customer_register"),
    path('owner_login/', v.owner_login, name="owner_login"),
    path('owner_register/', v.owner_register, name="owner_register"),
    path('reg/', v.reg, name="reg"),
    path('owner_reg/', v.owner_reg, name="owner_reg"),
    path('insert_contact/', v.insert_contact, name="insert_contact"),

    # (customer_urls)
    path('customer_home/', c.customer_home, name="customer_home"),
    path('customer_change_password/', c.customer_change_password, name="customer_change_password"),
    path('customer_details/', c.customer_details, name="customer_details"),
    path('customer_edit/<str:email>', c.customer_edit, name="customer_edit"),
    path('customer_delete/<str:email>', c.customer_delete, name="customer_delete"),
    path('customer_update/', c.customer_update, name="customer_update"),
    path('customer_logout/', c.customer_logout, name="customer_logout"),
    path('grounds/', c.grounds, name="grounds"),
    path('ground_booking/<int:id>', c.ground_booking, name="ground_booking"),
    path('view_bookings/', c.view_bookings, name="view_bookings"),

    # (owner views)
    path('owner_home/', o.owner_home, name="owner_home"),
    path('owner_change_password/', o.owner_change_password, name="owner_change_password"),
    path('owner_details/', o.owner_details, name="owner_details"),
    path('owner_edit/<str:email>', o.owner_edit, name="owner_edit"),
    path('owner_delete/<str:email>', o.owner_delete, name="owner_delete"),
    path('owner_update/', o.owner_update, name="owner_update"),
    path('owner_logout/', o.owner_logout, name="owner_logout"),
    path('add_grounds/', o.add_grounds, name="add_grounds"),
    path('view_grounds/', o.view_grounds, name="view_grounds"),
    path('ground_edit/<int:id>', o.ground_edit, name="ground_edit"),
    path('ground_delete/<int:id>', o.ground_delete, name="ground_delete"),
    path('ground_update/', o.ground_update, name="ground_update"),
    path('booked_slots/<int:id>', o.booked_slots, name="booked_slots"),
    path('booking_approve/<str:book_id>', o.booking_approve, name="booking_approve"),
    path('booking_reject/<str:book_id>', o.booking_reject, name="booking_reject"),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
