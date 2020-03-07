from django.views import generic


class LoginView(generic.TemplateView):
    template_name = 'login.html'


class HomeView(generic.TemplateView):
    template_name = 'home.html'


class AboutMeView(generic.TemplateView):
    template_name = 'about_me.html'


class PortfoliosView(generic.TemplateView):
    template_name = 'portfolios.html'


class SkillsView(generic.TemplateView):
    template_name = 'skills.html'


class ContactView(generic.TemplateView):
    template_name = 'contact.html'

class LpManaManaView(generic.TemplateView):
    template_name = 'manamana.html'