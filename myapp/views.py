from myapp.models import Purchase, NUM_OF_OCCUPANTS
from myapp.forms import PurchaseForm, CommentForm
from django.views.generic import ListView, TemplateView, CreateView, DetailView
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.forms import PasswordChangeForm


class AboutView(TemplateView):
    template_name = "myapp/about.html"


class PurchaseListView(ListView):
    paginate_by = 30
    model = Purchase

    def get_queryset(self):
        return Purchase.objects.order_by("-date")


class PurchaseDetailView(DetailView):
    model = Purchase


class CreatePurchaseView(LoginRequiredMixin, CreateView):
    login_url = "/login/"
    redirect_field_name = "myapp/purchase_list.html"
    model = Purchase
    fields = ["item", "price"]


    def form_valid(self, form):
        users = User.objects.all().exclude(username__in=["admin", self.request.user.username])
        form.instance.debts = {k.username: round(form.instance.price/NUM_OF_OCCUPANTS, 2) for k in users}
        form.instance.author = self.request.user
        return super().form_valid(form)


@login_required
def add_comment_to_purchase(request, pk):
    purchase = get_object_or_404(Purchase, pk=pk)

    if request.method == "POST":
        form = CommentForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.purchase = purchase
            comment.author = request.user
            comment.save()
            return redirect("purchase_detail", pk=purchase.pk)

    else:
        form = CommentForm()

    return render(request, "myapp/comment_form.html", {"form": form})


@login_required
def summary(request):
    purchases = Purchase.objects.all()
    values = {}
    for purchase in purchases:
        if purchase.author != request.user:
            values[purchase.author.username] = values.get(purchase.author.username, 0) + purchase.debts[request.user.username]
    return render(request, "myapp/summary.html", {"values": values})


@login_required
def cancel_debt(request, pk, person):
    purchase = get_object_or_404(Purchase, pk=pk)
    if purchase.author == request.user:
        purchase.debts[person] = 0
        purchase.save()
    return redirect("purchase_detail", pk=pk)


@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            return redirect('logout')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'profile_update.html', {
        'form': form
    })
