from django.core.management.base import BaseCommand
from django.utils import timezone

from polls.models import Question

SAMPLE_POLLS = {
    "What's your favorite programming language?": [
        "Python",
        "JavaScript",
        "Java",
        "Go",
    ],
    "Which CI tool do you prefer?": ["Travis CI", "GitHub Actions", "Jenkins"],
    "How do you deploy your apps?": [
        "AWS Elastic Beanstalk",
        "Heroku",
        "Docker on a VM",
    ],
}


class Command(BaseCommand):
    help = "Create sample polls if the database has no questions."

    def handle(self, *args, **options):
        if Question.objects.exists():
            self.stdout.write("Polls already exist; nothing to seed.")
            return
        for question_text, choices in SAMPLE_POLLS.items():
            question = Question.objects.create(
                question_text=question_text, pub_date=timezone.now()
            )
            for choice_text in choices:
                question.choice_set.create(choice_text=choice_text)
        self.stdout.write(f"Seeded {len(SAMPLE_POLLS)} polls.")
