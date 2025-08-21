from django.views.generic import TemplateView

class IndexView(TemplateView):
    template_name = 'home.html'

class PreplannedSafarisView(TemplateView):
    template_name = 'preplanned.html'

class LuxuryLodges(TemplateView):
    template_name = 'luxuryLodges.html'