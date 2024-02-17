import numpy as np

class SimilarityAnalyzer:
    def __init__(self, vector1, vector2):
        self.vector1 = vector1
        self.vector2 = vector2

    def cosin_similarity(self):
        """ 
        Calculates the cosine similarity between 2 vectors.

        Args:
            vector1 (list): Vector representation of the first text.
            vector2 (list): Vector representation of the second text.

        Returns:
            float: Cosine similarity between the 2 vectors.
        """
        return np.dot(self.vector1, self.vector2) / (np.linalg.norm(self.vector1) * np.linalg.norm(self.vector2))


