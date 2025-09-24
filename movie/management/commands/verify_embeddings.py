
from django.core.management.base import BaseCommand
from movie.models import Movie
import numpy as np

class Command(BaseCommand):
    help = "Verifica que los embeddings de las películas se almacenaron correctamente."

    def handle(self, *args, **kwargs):
        for movie in Movie.objects.all():
            # Convertimos el campo binario a un array de numpy
            embedding_vector = np.frombuffer(movie.emb, dtype=np.float32)

            # Mostramos los primeros 5 valores del embedding
            self.stdout.write(
                f"{movie.title} -> {embedding_vector[:5]}"
            )
