from django.contrib.sites.models import Site
from django.core.urlresolvers import reverse
from zinnia.settings import PROTOCOL

def backend(entry):
    return '%s://%s%s' % (PROTOCOL, Site.objects.get_current().domain,
                          reverse('zinnia_entry_shortlink', args=[entry.pk]))
