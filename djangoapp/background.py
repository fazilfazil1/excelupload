async def get_project_results(projects: list):
    results = await asyncio.gather(*(do_request(project) for project in projects))
    return results

def aggregate_results(projects: list):
    results = asyncio.run(get_project_results(projects))
    return zip(projects, results)