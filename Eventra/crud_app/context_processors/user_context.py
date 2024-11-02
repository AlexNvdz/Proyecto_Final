
from django.shortcuts import get_object_or_404
from ..models import Usuario

def get_usuario_context(request):
    if request.session.get('user_id'):
        usuario_actual = get_object_or_404(Usuario, pk=request.session['user_id'])
        return {'usuario_actual': usuario_actual}
    return {}
