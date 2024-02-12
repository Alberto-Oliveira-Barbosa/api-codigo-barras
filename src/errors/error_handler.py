from src.views.http_types.http_response import HttpResponse
from .error_types.http_unprocessable_entity import HttpUnprocessableEntityError

def handle_errors(error: Exception) -> HttpResponse:
    if isinstance(error, HttpUnprocessableEntityError):
        return HttpResponse(
            status_code=error.status_code,
            body={
                "title": error.name,
                "details": error.message
            }
        )

    return HttpResponse(
        status_code=500,
        body={
                "title": "Server Error",
                "details": str(error)
        }
    )
