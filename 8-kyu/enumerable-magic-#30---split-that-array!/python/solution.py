def partition(arr, classifier_method):
    return ([elem for elem in arr if classifier_method(elem)], [elem for elem in arr if not classifier_method(elem)])
