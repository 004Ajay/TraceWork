import asyncio
import httpx

from main.config import GRAPHQL_ENDPOINT, REQUEST_TIMEOUT, MAX_CONCURRENT_REQUESTS


class GitLabGraphQLClient:
    def __init__(self, base_url: str, token: str):

        self.url = base_url.rstrip("/") + GRAPHQL_ENDPOINT

        self.headers = {"Authorization": f"Bearer {token}"}

        self.semaphore = asyncio.Semaphore(MAX_CONCURRENT_REQUESTS)

    async def execute(self, query: str, variables: dict):

        async with self.semaphore:
            async with httpx.AsyncClient(timeout=REQUEST_TIMEOUT) as client:
                response = await client.post(
                    self.url,
                    headers=self.headers,
                    json={"query": query, "variables": variables},
                )

                response.raise_for_status()

                data = response.json()

                if "errors" in data:
                    raise Exception(data["errors"])

                return data["data"]
