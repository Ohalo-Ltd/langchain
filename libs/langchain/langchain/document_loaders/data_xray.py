from typing import Iterator, List

import requests
import copy

from langchain.docstore.document import Document
from langchain.document_loaders.base import BaseLoader
from typing import Any, Dict


def create_token_headers(
    default_headers: Dict[str, Any], system_token: str
) -> Dict[str, Any]:
    headers = copy.deepcopy(default_headers)
    session_token = system_token
    headers.update({"Authorization": f"Bearer {session_token}"})

    return headers


class DataXRayLoader(BaseLoader):
    """Load `Data X-Ray` documents."""

    def __init__(self, api_token: str, datasource_id: int, object_id: str):
        """Initialize with API token and the IDs for datasource and object"""
        self.api_token = api_token
        """Data X-Ray API token."""
        self.datasource_id = datasource_id
        """Data X-Ray Datasource ID."""
        self.object_id = object_id
        """Data X-Ray Object ID."""

    def lazy_load(self) -> Iterator[Document]:
        """Lazy load Documents from Data X-Ray."""

        default_headers = {
            "Content-Type": "application/json",
            "Accept": "*/*",
            "Sec-Fetch-Dest": "empty",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Site": "same-origin",
        }

        headers = create_token_headers(default_headers, self.system_token)

        response = requests.get(
            "https://dev-backend.dataxray.io/api/datasources/ingester/{self.datasource_id}/file/extract?objectId={self.object_id}",
            headers=headers,
        )

        print(response.json())

        # table = Table(self.api_token, self.base_id, self.table_id)
        # records = table.all()
        # for record in records:
        #     # Need to convert record from dict to str
        #     yield Document(
        #         page_content=str(record),
        #         metadata={
        #             "source": self.base_id + "_" + self.table_id,
        #             "base_id": self.base_id,
        #             "table_id": self.table_id,
        #         },
        #     )

    def load(self) -> List[Document]:
        """Load Documents from Data X-Ray."""
        return list(self.lazy_load())
