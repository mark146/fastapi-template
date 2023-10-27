def to_json(obj):
    obj_dict = {k: v for k, v in obj.__dict__.items() if v is not None}
    return obj_dict  # Return dictionary directly
