from rest_framework.permissions import BasePermission
from comments.models import Comment

class IsOwnerOrReadAndCreateOnly(BasePermission):
  def has_permission(self, request, view):
    if request.method == "GET" or request.method == "POST":
      return True
    else:
      comment = Comment.objects.get(pk=view.kwargs['pk'])
      user_id = request.user.pk
      comment_user_id = comment.user_id
      if user_id == comment_user_id:
        return True
      
      return False