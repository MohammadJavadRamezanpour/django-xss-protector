def filter_fields(fields, keys):
    """this function filters fields based on keys, 
    only those fields with mentioned keys will be included"""

    if not keys:
        return fields

    filtered_fields = []

    for dictionary in fields:
        filtered_dictionary = dict()
        for key in keys:
            if key in dictionary:
                filtered_dictionary[key] = dictionary[key]
        if filtered_dictionary:
            filtered_fields.append(filtered_dictionary)
    return filtered_fields
