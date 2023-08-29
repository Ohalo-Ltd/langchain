
from unittest.mock import MagicMock, patch

import pytest

from langchain.document_loaders import DataXRayLoader

@pytest.fixture
def test_lazy_load(mock_feature_layer, mock_gis):  # type: ignore
    # loader = DataXRayLoader(layer=mock_feature_layer, gis=mock_gis)
    # loader.BEAUTIFULSOUP = None

    # documents = list(loader.lazy_load())
    # print(documents)
    # assert len(documents) == 1
    # assert documents[0].metadata["url"] == "https://example.com/layer_url"
    # # Add more assertions based on your expected behavior
