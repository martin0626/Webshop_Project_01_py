from django.shortcuts import render
import django.views.generic as class_views


def test_view(request):
    return render(request, 'asd.html')
