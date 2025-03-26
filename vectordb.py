import numpy as np
from collections import defaultdict

class VectorDatabase:
  """
  A simple in-memory vector database.
  """

  def __init__(self):
    self.vectors = []
    self.metadata = []
    self.index = defaultdict(list)

  def insert(self, vector, metadata={}):
    """
    Inserts a vector and its associated metadata into the database.

    Args:
      vector: A numpy array representing the vector.
      metadata: A dictionary containing metadata associated with the vector.
    """
    self.vectors.append(vector)
    self.metadata.append(metadata)
    self.index[tuple(vector)].append(len(self.vectors) - 1)

  def search(self, query_vector, top_k=1):
    """
    Searches the database for the nearest vectors to the query vector.

    Args:
      query_vector: A numpy array representing the query vector.
      top_k: The number of nearest vectors to return.

    Returns:
      A list of tuples, where each tuple contains the metadata and distance
      of a nearest vector.
    """
    distances = [np.linalg.norm(query_vector - v) for v in self.vectors]
    indices = np.argsort(distances)[:top_k]
    return [(self.metadata[i], distances[i]) for i in indices]

# Example usage:
db = VectorDatabase()

# Insert some vectors with metadata
db.insert(np.array([1, 2, 3]), {"id": 1, "name": "vector1"})
db.insert(np.array([4, 5, 6]), {"id": 2, "name": "vector2"})
db.insert(np.array([7, 8, 9]), {"id": 3, "name": "vector3"})

# Search for the nearest vector to a query vector
query_vector = np.array([20, 30, 40])
results = db.search(query_vector, top_k=1)

# Print the results
for metadata, distance in results:
  print(f"Metadata: {metadata}, Distance: {distance}")