# helpers/data_generator.py

import random
import string

def _generate_random_string(length):
    letters = string.ascii_lowercase + string.digits
    return ''.join(random.choice(letters) for _ in range(length))

# генератор пользователя
def get_user_payload() -> dict:
    return {
        "email": f"{_generate_random_string(5)}@{_generate_random_string(5)}.ru",
        "password": _generate_random_string(6),
        "name": _generate_random_string(6)
    }

# payload меняем поле
def modify_payload_for_field(base_payload, field_name, field_value):
    modified = base_payload.copy()
    if field_value is None:
        modified.pop(field_name, None)
    else:
        modified[field_name] = field_value
    return modified

