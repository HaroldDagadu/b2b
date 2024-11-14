# b2bpost/views.py
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from .models import B2BPost
from .serializers import B2BPostSerializer

from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication
from .models import B2BPost
from .serializers import B2BPostSerializer
from rest_framework.decorators import api_view, permission_classes

from rest_framework_simplejwt.exceptions import InvalidToken, TokenError

# views.py
from rest_framework import viewsets
from .models import B2BPost
from .serializers import B2BPostSerializer
from rest_framework.permissions import IsAuthenticated

class B2BPostViewSet(viewsets.ModelViewSet):
    queryset = B2BPost.objects.all()
    serializer_class = B2BPostSerializer

    def perform_create(self, serializer):
        serializer.save()  # Do not pass 'user' here; it's handled in the serializer

    @action(detail=True, methods=['post'])
    def fact(self, request, pk=None):
        post = self.get_object()
        post.facts += 1
        post.save()
        return Response(B2BPostSerializer(post).data)

    @action(detail=True, methods=['post'])
    def nah_bro(self, request, pk=None):
        post = self.get_object()
        post.nah_bro += 1
        post.save()
        return Response(B2BPostSerializer(post).data)


from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from .serializers import B2BPostSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def createpost(request):
    jwt_auth = JWTAuthentication()
    try:
        validated_token = jwt_auth.get_validated_token(
            request.COOKIES.get("access_token")
        )
        user = jwt_auth.get_user(validated_token)
    except (InvalidToken, TokenError):
        return Response(
            {
                "isAuthenticated": False,
                "error": "Unauthorized. Token is invalid or missing.",
            },
            status=status.HTTP_401_UNAUTHORIZED,
        )

    # Initialize the serializer with the request data
    serializer = B2BPostSerializer(data=request.data)

    if serializer.is_valid():
        # Save the job with the authenticated user
        serializer.save(user=user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
