from concurrent.futures import ThreadPoolExecutor


def runInParallel(*tasks):
    results = []
    with ThreadPoolExecutor() as executor:
        running_tasks = [executor.submit(task) for task in tasks]
        for running_task in running_tasks:
            results.append(running_task.result())

    return results
