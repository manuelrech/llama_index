"""Vector-store based data structures."""

from llama_index.indices.multi_modal.base import MultiModalVectorStoreIndex
from llama_index.indices.multi_modal.retrievers import (
    MultiModalVectorIndexRetriever,
)

__all__ = [
    "MultiModalVectorStoreIndex",
    "MultiModalVectorIndexRetriever",
]