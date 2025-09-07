from collections import Counter
from django import views
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache

from ..utils.search_api import SearchAPI
from ..forms import ParagraphForm, SearchForm
from ..models import ParagraphSubmission


@method_decorator([login_required, never_cache], name="dispatch")
class SubmitView(views.View):
    def get(self, request):
        return render(request, "search/submit.html", {"form": ParagraphForm()})

    def post(self, request):
        text = request.POST.get("text", "")
        if not text:
            messages.error(request, "Please enter a paragraph.")
            return render(
                request,
                "search/submit.html",
            )
        api = SearchAPI(text)
        for para in api.paras:
            submission = ParagraphSubmission.objects.create(
                user=request.user,
                paragraph=para,
                word_freq_index=dict(Counter(para.strip().split()))
            )
            submission.save()
        messages.success(request, "Paragraphs saved successfully.")
        return render(request, "search/dashboard.html")


class SearchView(views.View):
    def get(self, request):
        return render(request, "search/search.html", {"form": SearchForm()})

    def post(self, request):
        search_term = request.POST.get("search_term", "")
        if not search_term:
            messages.error(request, "Please enter a search term.")
            return render(
                request,
                "search/search.html",
            )
        para_submissions = ParagraphSubmission.objects.filter(
            user=request.user
        )
        results = {}
        for submission in para_submissions:
            results[submission] = submission.word_freq_index.get(
                search_term, 0
            )
        if all(value == 0 for value in results.values()):
            messages.info(request, "No matching paragraphs found.")
            return render(
                request,
                "search/search.html",
                {"form": SearchForm()}
            )
        sorted_results = dict(
            sorted(results.items(), key=lambda item: item[1], reverse=True)
        )
        if len(sorted_results) <= 10:
            top_results = list(
                submission.paragraph for submission in sorted_results.keys()
            )
        else:
            top_results = [
                submission.paragraph
                for submission in list(sorted_results.keys())[:10]
            ]
        return render(request, "search/results.html", {"results": top_results})


@login_required
def view_paragraphs(request):
    submissions = ParagraphSubmission.objects.filter(user=request.user)
    paras = [submission.paragraph for submission in submissions]
    return render(request, "search/view_paragraphs.html", {"paras": paras})
