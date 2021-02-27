from exam import views
from django.conf.urls import url

urlpatterns = [
url('test',views.showTest),
url('signup',views.sign_up),
url('login',views.user_login),
url('complete',views.exam_complete),
url('logout',views.userLogout),
url('profile',views.user_profile),
url('feedback',views.userFeedback),
url('Leader_Board',views.userLeaderBoard),
url('changePass',views.userChangePassword),
]
