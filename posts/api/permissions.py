from rest_framework.permissions import BasePermission


# custom permission todos puede leer pero solo el admin puede editar, crear y borrar
class IsAdminOrReadOnly(BasePermission):
  def has_permission(self, request, view):
    if request.method == 'GET':
      return True
    else:
      return request.user.is_staff