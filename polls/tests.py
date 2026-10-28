import datetime

from django.test import TestCase
from django.urls import reverse
from django.utils import timezone

from .models import Choice, Question


def create_question(question_text, days):
    """Create a question published `days` offset from now."""
    time = timezone.now() + datetime.timedelta(days=days)
    return Question.objects.create(question_text=question_text, pub_date=time)


class QuestionModelTests(TestCase):
    def test_was_published_recently_with_future_question(self):
        future_question = create_question("Future", days=30)
        self.assertIs(future_question.was_published_recently(), True)

    def test_was_published_recently_with_old_question(self):
        old_question = create_question("Old", days=-2)
        self.assertIs(old_question.was_published_recently(), False)

    def test_was_published_recently_with_recent_question(self):
        recent_question = create_question("Recent", days=0)
        self.assertIs(recent_question.was_published_recently(), True)

    def test_str(self):
        question = create_question("What's up?", days=0)
        choice = Choice.objects.create(question=question, choice_text="Not much")
        self.assertEqual(str(question), "What's up?")
        self.assertEqual(str(choice), "Not much")


class PollsViewTests(TestCase):
    def test_index_no_questions(self):
        response = self.client.get(reverse("polls:index"))
        self.assertEqual(response.status_code, 200)
        self.assertQuerySetEqual(response.context["latest_question_list"], [])

    def test_index_lists_question(self):
        question = create_question("Past question", days=-1)
        response = self.client.get(reverse("polls:index"))
        self.assertQuerySetEqual(response.context["latest_question_list"], [question])

    def test_detail_and_results(self):
        question = create_question("Detail question", days=-1)
        for name in ("polls:detail", "polls:results"):
            response = self.client.get(reverse(name, args=(question.id,)))
            self.assertContains(response, question.question_text)

    def test_vote_without_choice_shows_error(self):
        question = create_question("Vote question", days=-1)
        response = self.client.post(reverse("polls:vote", args=(question.id,)))
        self.assertContains(response, "You didn&#x27;t select a choice.")

    def test_vote_with_choice_redirects_and_counts(self):
        question = create_question("Vote question", days=-1)
        choice = Choice.objects.create(question=question, choice_text="Yes")
        response = self.client.post(
            reverse("polls:vote", args=(question.id,)), {"choice": choice.id}
        )
        self.assertRedirects(response, reverse("polls:results", args=(question.id,)))
        choice.refresh_from_db()
        self.assertEqual(choice.votes, 1)
