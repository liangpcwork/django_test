#!/usr/bin/env python
from django.shortcuts import render


def hello(request):
    print("path:", request.path)
    print("method:", request.method)
    print("post:", request.POST)
    print("get:", request.GET)
    print("cookies:", request.COOKIES)
    print("files:", request.FILES)
    print("meta:", request.META)
    print("user:", request.user.is_authenticated)

    print("session:", request.session)


    context = dict()
    context["hello"] = "the context of hello_key"
    context["is_equal"] = "people"
    context["is_show"] = True
    context["friends_names"] = ["Curry", "Thomas", "KD", "James", "Rose"]
    return render(request, "hello.html", context)
