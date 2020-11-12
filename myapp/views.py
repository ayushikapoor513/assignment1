from django.views.generic.base import TemplateView

from myapp.models import Article

class HomePageView(TemplateView):

    template_name = "home.html"

    def get_context_data(self, *args, **kwargs):
        context = super(HomePageView,self).get_context_data(*args,**kwargs)
        context['latest_articles'] = self.get_data()
        return context

    def get_data(self):
      latest_articles = Article.objects.all()[:5]
      return latest_articles
        