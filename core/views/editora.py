from rest_framework.viewsets import ModelViewSet

from core.models import Autor, Categoria, Editora, Livro
from core.serializers import (
    AutorSerializer,
    CategoriaSerializer,
    EditoraSerializer,
    LivroDetailSerializer,
    LivroSerializer,
)


class EditoraViewSet(ModelViewSet):
    queryset = Editora.objects.all()
    serializer_class = EditoraSerializer