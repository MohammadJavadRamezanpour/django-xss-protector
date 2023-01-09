def silent_delete_from_dictionary(removing_fields, removing_keys):
    """this function delets removing_keys from dictionary without any error if any KeyError"""
    cleared_fields = []
    for dictionary in removing_fields:
        for key in removing_keys:
            try:
                del dictionary[key]
            except:
                pass

        cleared_fields.append(dictionary)
    return cleared_fields
