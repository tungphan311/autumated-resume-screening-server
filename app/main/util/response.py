from datetime import datetime

def response_object(code = 200, message = "Thành công.", data = [], pagination = None):
    if not pagination:
        return {
            'code': code,
            'message': message,
            'data': data,
        }
    else:
        return {
            'code': code,
            'message': message,
            'data': data,
            'pagination': pagination
        }

def json_serial(obj):
    if isinstance(obj, datetime):
        return obj.isoformat()