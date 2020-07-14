from django.http import HttpResponseRedirect
from django.urls import reverse


class superUserMixin(object):

  def dispatch(self, request, *args, **kwargs):
    if request.user.has_perm('is_Socio'):
      return super().dispatch(request, *args, **kwargs)
    return HttpResponseRedirect(reverse('home_app:panel-socio'))


class userSocioMixin():
  pass


class userUsuarioMixin():
  pass

