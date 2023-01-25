from django.urls import path

from libraryapp import views

urlpatterns=[
    path('',views.lof_fun,name='log'),
    path('log_read',views.log_read_fun),
    path('studentreg',views.studentreg_fun,name='stureg'),
    path('s_data',views.student_read_fun),
    path('adminreg',views.adminreg_fun,name='adreg'),
    path('a_data',views.adminreg_read_fun),
    path('addbook',views.addbook_fun,name='add'),
    path('addbook_read',views.addbook_read_fun),
    path('display',views.display_fun,name='dis'),
    path('update/<int:id>',views.updatebook_fun,name='up'),
    path('delete/<int:id>',views.deletebook_fun,name='del'),
    path('assignbook',views.assignbooks_fun ,name='assign'),
    path('readsemcourse',views.readsemcourse_fun),
    path('readstdbook',views.readstdbook_fun),
    path('displaybooks',views.displaybook_fun,name='disbooks'),
    path('updateibook/<int:id>',views.updateibook_fun,name='ibup'),
    path('deleteibook/<int:id>',views.deleteibook_fun,name='ibdel'),
    path('stubooks',views.stubooks,name='stubooks'),
    path('stdhome',views.stdhome,name='stdhome')
]