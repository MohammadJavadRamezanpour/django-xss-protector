def silent_delete_from_dictioary(dictionary, removing_keys):
    """this function delets removing_keys from dictionary without any error if any key error"""
    for key in removing_keys:
        try:
            del dictionary[key]
        except:
            pass

    return dictionary
