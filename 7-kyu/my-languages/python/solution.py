def my_languages(results):
    sorted_results = sorted({k: v for k, v in results.items() if v >= 60}, key=results.__getitem__, reverse=True)
    return sorted_results