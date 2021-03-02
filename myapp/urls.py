from myapp import views
from django.urls import path

urlpatterns = [
    path("", views.PurchaseListView.as_view(), name="purchase_list"),
    path("about/", views.AboutView.as_view(), name="about"),
    path("purchase/new/", views.CreatePurchaseView.as_view(), name="purchase_new"),
    path("purchase/<int:pk>", views.PurchaseDetailView.as_view(), name="purchase_detail"),
    path("purchase/<int:pk>/cancel/<str:person>", views.cancel_debt, name="cancel_debt"),
    path("purchase/<int:pk>/comment/", views.add_comment_to_purchase, name="add_comment_to_purchase"),
    path("summary/", views.summary, name="summary"),
]
