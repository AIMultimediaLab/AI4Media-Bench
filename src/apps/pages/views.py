import os
from datetime import timedelta, datetime
from django.http import HttpResponse
from django.utils.timezone import now
from django.views.generic import TemplateView
from django.db.models import Count, Q

from competitions.models import Competition, Submission, CompetitionParticipant
from profiles.models import User
from announcements.models import Announcement, NewsPost

from django.shortcuts import render


class HomeView(TemplateView):
    template_name = 'pages/home.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        data = Competition.objects.aggregate(
            count=Count('*'),
            published_comps=Count('pk', filter=Q(published=True)),
            unpublished_comps=Count('pk', filter=Q(published=False)),
        )

        total_competitions = data['count']
        public_competitions = data['published_comps']
        users = User.objects.all().count()
        competition_participants = CompetitionParticipant.objects.all().count()
        submissions = Submission.objects.all().count()

        context['general_stats'] = [
            {'label': "Total Competitions", 'count': total_competitions},
            {'label': "Public Competitions", 'count': public_competitions},
            {'label': "Users", 'count': users},
            {'label': "Competition Participants", 'count': competition_participants},
            {'label': "Submissions", 'count': submissions},
        ]

        announcement = Announcement.objects.all().first()
        context['announcement'] = announcement.text if announcement else None

        news_posts = NewsPost.objects.all().order_by('-id')
        context['news_posts'] = news_posts

        return context


class OrganizeView(TemplateView):
    template_name = 'pages/organize.html'


class SearchView(TemplateView):
    template_name = 'search/form.html'


class ServerStatusView(TemplateView):
    template_name = 'pages/server_status.html'

    def get_context_data(self, *args, **kwargs):

        show_child_submissions = self.request.GET.get('show_child_submissions', False)

        # Get all submissions
        qs = Submission.objects.all()

        # If user is not super user then:
        # filter this user's own submissions
        # and
        # submissions running on queue which belongs to this user
        if not self.request.user.is_superuser:
            qs = qs.filter(
                Q(owner=self.request.user) |
                Q(phase__competition__queue__isnull=False, phase__competition__queue__owner=self.request.user)
            )

        # filter for fetching last 2 days submissions
        qs = qs.filter(created_when__gte=now() - timedelta(days=2))

        # filter out child submissions i.e. submission has no parent
        if not show_child_submissions:
            qs = qs.filter(parent__isnull=True)

        qs = qs.order_by('-created_when')
        qs = qs.select_related('phase__competition', 'owner')

        context = super().get_context_data(*args, **kwargs)
        context['submissions'] = qs[:250]
        context['show_child_submissions'] = show_child_submissions

        for submission in context['submissions']:
            # Get filesize from each submissions's data
            submission.file_size = self.format_file_size(submission.data.file_size)
            # Get queue from each submission
            queue_name = "*" if submission.queue is None else submission.queue.name
            submission.competition_queue = queue_name

        return context

    def format_file_size(self, file_size):
        """
        A custom function to convert file size to KB, MB, GB and return with the unit
        """
        try:
            n = float(file_size)
        except ValueError:
            return ""

        units = ['KB', 'MB', 'GB']
        i = 0
        while n >= 1000 and i < len(units) - 1:
            n /= 1000
            i += 1

        return f"{n:.1f} {units[i]}"


def page_not_found_view(request, exception):
    print(request)
    return render(request, '404.html', status=404)

def get_file_content(file_path):
    with open(file_path, 'r') as file:
        return file.read()

def render_text_response(content, filename):
    response = HttpResponse(content, content_type='text/plain')
    response['Content-Disposition'] = f'inline; filename={filename}'
    return response

def license_view(request):
    # Get the absolute path to the LICENSE.txt file
    file_path = os.path.join(os.path.dirname(__file__), '../../../', 'LICENSE.TXT')
    license_content = get_file_content(file_path)

    # Render the response with the content of the text file
    return render_text_response(license_content, 'LICENSE.TXT')

def notice_view(request):
    current_year = datetime.now().year
    copyright_owner = "AIMultimediaLab (https://www.aimultimedialab.ro/)"

    # Get the absolute path to the NOTICE.txt file
    file_path = os.path.join(os.path.dirname(__file__), '../../../', 'NOTICE.TXT')
    notice_content = get_file_content(file_path)

    # Replace placeholders with current year and copyright owner in NOTICE.txt content
    notice_content = notice_content.replace('[yyyy]', str(current_year))
    notice_content = notice_content.replace('[name of copyright owner]', copyright_owner)

    # Render the response with the content of the text file
    return render_text_response(notice_content, 'NOTICE.TXT')
