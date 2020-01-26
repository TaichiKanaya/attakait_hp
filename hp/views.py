from django.views import generic


class LoginView(generic.TemplateView):
    template_name = 'login.html'


class HomeView(generic.TemplateView):
    template_name = 'home.html'


class SelfIntroductionView(generic.TemplateView):
    template_name = 'self_introduction.html'


class PortfoliosView(generic.TemplateView):
    template_name = 'portfolios.html'


class SkillsView(generic.TemplateView):
    template_name = 'skills.html'
