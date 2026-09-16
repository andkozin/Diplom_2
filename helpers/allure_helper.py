# helpers/allure_helper.py

import json
import allure

def attach_api_call(payload, response, url, prefix=""):
    if prefix:
        prefix += " "

    # URL
    allure.attach(
        url,
        name=f"{prefix}URL",
        attachment_type=allure.attachment_type.TEXT,
    )

    # Payload 
    if payload is not None:
        payload_str = json.dumps(payload, indent=2, ensure_ascii=False)
        allure.attach(
            payload_str,
            name=f"{prefix}Payload",
            attachment_type=allure.attachment_type.JSON,  
        )

    # Response 
    try:
        body_obj = response.json()
        body_formatted = json.dumps(body_obj, indent=2, ensure_ascii=False)
        attachment_type = allure.attachment_type.JSON
    except (json.JSONDecodeError, ValueError):
       
        body_formatted = response.text
        attachment_type = allure.attachment_type.TEXT

    response_text = (
        f"{prefix}Status: {response.status_code}\n"
        f"{prefix}Body:\n{body_formatted}"
    )
    allure.attach(
        response_text,
        name=f"{prefix}Response",
        attachment_type=attachment_type,
    )

