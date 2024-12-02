from crawl4ai import AsyncWebCrawler
from pprint import pprint

async def main(url:str):
    async with AsyncWebCrawler(verbose=True) as crawler:
        result = await crawler.arun(url)
        pprint(result, indent=2)

        return result

if __name__ == '__main__':
    import asyncio
    url = "https://cookbook.openai.com/examples/orchestrating_agents"
    response = asyncio.run(main(url))

    # save the response.markdown to a file
    with open(f'{url.split('/')[-1]}.md', 'w') as f:
        f.write(response.markdown)