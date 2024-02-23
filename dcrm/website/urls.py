from django.urls import path
from . import views
# გამოვიძახეთ home მეთოდი views ფოლდერიდან. მისამართი არ მივანიჭეთ ანუ საწყის მისამართზე.
urlpatterns = [
    path('',views.home,name='home'),
    # path('login/',views.login_user,name='login'),
    path('logout',views.logout_user,name='logout'),
]
