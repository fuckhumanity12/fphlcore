from django.shortcuts import render, redirect
from django.views import View
from .models import *
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator


class QuestList(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        quests = QuestionSet.objects.all().order_by("-date")

        return render(request, "questions/list.html", {"questions": quests, })


@method_decorator(csrf_exempt, name='dispatch')
class QuestionDetail(LoginRequiredMixin, View):
    def get(self, request, pk, *args, **kwargs):
        if QuestionSet.objects.filter(id=pk).exists():
            qset = QuestionSet.objects.get(id=pk)
            if qset.private:
                if request.user in qset.choose_users.all():
                    pass
                else:
                    messages.warning(request, "This Is A Private Exam")
                    return redirect("questions-list")
            else:
                pass
            if not qset.repeat_solves:
                if request.user in qset.solves.all():
                    messages.warning(
                        request, "This Is A One-Solve Only Exam, And You Did Solve It")
                    return redirect("questions-list")
                else:
                    pass
            else:
                pass
        else:
            messages.warning(request, "Question Set Doesn't Exist")
            return redirect("home")
        return render(request, "questions/quest-detail.html", {"questions": qset, })

    def post(self, request, pk, *args, **kwargs):
        if QuestionSet.objects.filter(id=pk).exists():
            qset = QuestionSet.objects.get(id=pk)
            if qset.private:
                if request.user in qset.choose_users.all():
                    pass
                else:
                    messages.warning(request, "This Is A Private Exam")
                    return redirect("questions-list")
            else:
                pass
            if not qset.repeat_solves:
                if request.user in qset.solves.all():
                    messages.warning(request, "This Is A One-Solve Only Exam")
                    return redirect("questions-list")
                else:
                    pass
            else:
                pass
            score = 0
            for q in qset.questions.all():
                ans = request.POST.get(str(q.id))
                if ans == q.ans:
                    score += 1
            newscore = Score.objects.create(user=request.user, score=(
                score/qset.questions.count())*100, questset=qset)
            qset.solves.add(request.user)
            return redirect("score-page", pk)
        else:
            messages.warning(request, "Question Set Doesn't Exist")
            return redirect("home")


class ScorePage(LoginRequiredMixin, View):
    def get(self, request, pk, *args, **kwargs):
        if QuestionSet.objects.filter(id=pk).exists():
            qset = QuestionSet.objects.get(id=pk)
            if Score.objects.filter(user=request.user, questset=qset).exists():
                score = Score.objects.filter(
                    user=request.user, questset=qset).latest("date")
            else:
                messages.warning(
                    request, "you haven't solved this question set yet")
                return redirect("questions-list")
        else:
            messages.warning(request, "this question set does not exist")
            return redirect("questions-list")
        return render(request, "questions/score-page.html", {"quests": score})


class ListScore(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        userscores = Score.objects.filter(user=request.user).order_by("-date")
        return render(request, "questions/list-scores.html", {"scores": userscores, })
