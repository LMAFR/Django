from django.http import HttpResponse, JsonResponse
from snippets.serializers import SnippetSerializer
from snippets.models import Snippet
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import Http404
from rest_framework import generics, mixins

# Create your views here.

class snippet_list(mixins.CreateModelMixin,
                   mixins.ListModelMixin,
                   generics.GenericAPIView):
    """
    List all code snippets, or create a new snippet.
    """

    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class snippet_detail(APIView):
    """
    Retrieve, update or delete a code snippet.
    """

    def get_object(self, pk):
        try:
            return Snippet.objects.get(pk=pk)
        except:
            raise Http404
    
    def get(self, request, pk, format=None):
        snippet = self.get_object(pk=pk)
        serializer = SnippetSerializer(snippet)
        return JsonResponse(serializer.data)

    def put(self, request, pk, format=None):
        snippet = self.get_object(pk=pk)
        # In the line below, first we tell the serializer what snippet instance we want to modify and then we pass it the new data for that instance.
        serializer = SnippetSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk=pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)