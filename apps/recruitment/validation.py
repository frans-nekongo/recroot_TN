from django.http import HttpResponse

from apps.utils import validators


# Name validations
def first_name_validation(request) -> HttpResponse:
    """
    Validates the 'first_name' field in the request.

    Args:
        request (HttpRequest): The HTTP request containing the data to validate.

    Returns:
        HttpResponse: A response indicating whether the validation was successful or failed.
    """
    return validators.validate_name(request, "first_name")


def middle_name_validation(request) -> HttpResponse:
    """
    Validates the 'middle_name' field in the request.

    Args:
        request (HttpRequest): The HTTP request containing the data to validate.

    Returns:
        HttpResponse: A response indicating whether the validation was successful or failed.
    """
    return validators.validate_name(request, "middle_name")


def last_name_validation(request) -> HttpResponse:
    """
    Validates the 'last_name' field in the request.

    Args:
        request (HttpRequest): The HTTP request containing the data to validate.

    Returns:
        HttpResponse: A response indicating whether the validation was successful or failed.
    """
    return validators.validate_name(request, "last_name")


# Contact validations
def primary_contact_validation(request) -> HttpResponse:
    """
    Validates the 'primary_contact' field in the request.

    Args:
        request (HttpRequest): The HTTP request containing the data to validate.

    Returns:
        HttpResponse: A response indicating whether the validation was successful or failed.
    """
    return validators.validate_contact(request, "primary_contact")


def secondary_contact_validation(request) -> HttpResponse:
    """
    Validates the 'secondary_contact' field in the request.

    Args:
        request (HttpRequest): The HTTP request containing the data to validate.

    Returns:
        HttpResponse: A response indicating whether the validation was successful or failed.
    """
    return validators.validate_contact(request, "secondary_contact")

# def tertiary_institution_validation(request) -> HttpResponse:
#     """
#     Validates the 'tertiary_institution' field in the request.
#
#     Args:
#         request (HttpRequest): The HTTP request containing the data to validate.
#
#     Returns:
#         HttpResponse: A response indicating whether the validation was successful or failed.
#     """
#     return validators.validate_name(request, "tertiary_institution")
#
#
# def field_of_study_validation(request) -> HttpResponse:
#     """
#     Validates the 'field_of_study' field in the request.
#
#     Args:
#         request (HttpRequest): The HTTP request containing the data to validate.
#
#     Returns:
#         HttpResponse: A response indicating whether the validation was successful or failed.
#     """
#     return validators.validate_name(request, "field_of_study")
#
#
# def trade_speciality_validation(request) -> HttpResponse:
#     """
#     Validates the 'trade_specialty' field in the request.
#
#     Args:
#         request (HttpRequest): The HTTP request containing the data to validate.
#
#     Returns:
#         HttpResponse: A response indicating whether the validation was successful or failed.
#     """
#     return validators.validate_name(request, "trade_speciality")
#
#
# def NQF_level_or_level_validation(request) -> HttpResponse:
#     """
#     Validates the 'NQF_level_or_level' field in the request.
#
#     Args:
#         request (HttpRequest): The HTTP request containing the data to validate.
#
#     Returns:
#         HttpResponse: A response indicating whether the validation was successful or failed.
#     """
#     return validators.validate_number(request, "NQF_level_or_level_validation")



# def applicable_role_validation(request) -> HttpResponse:
#     """
#     Validates the 'applicable_role' field in the request.
#
#     Args:
#         request (HttpRequest): The HTTP request containing the data to validate.
#
#     Returns:
#         HttpResponse: A response indicating whether the validation was successful or failed.
#     """
#     return validators.validate_name(request, "applicable_role")
#
#
# def non_applicable_role_validation(request) -> HttpResponse:
#     """
#     Validates the 'non_applicable_role' field in the request.
#
#     Args:
#         request (HttpRequest): The HTTP request containing the data to validate.
#
#     Returns:
#         HttpResponse: A response indicating whether the validation was successful or failed.
#     """
#     return validators.validate_number(request, "non_applicable_role")
#
#
# def applicable_experience_validation(request) -> HttpResponse:
#     """
#     Validates the 'applicable_experience' field in the request.
#
#     Args:
#         request (HttpRequest): The HTTP request containing the data to validate.
#
#     Returns:
#         HttpResponse: A response indicating whether the validation was successful or failed.
#     """
#     return validators.validate_number(request, "applicable_experience")
#
#
# def non_applicable_experience_validation(request) -> HttpResponse:
#     """
#     Validates the 'non_applicable_experience' field in the request.
#
#     Args:
#         request (HttpRequest): The HTTP request containing the data to validate.
#
#     Returns:
#         HttpResponse: A response indicating whether the validation was successful or failed.
#     """
#     return validators.validate_number(request, "non_applicable_experience")
#
#
# def references_name_validation(request) -> HttpResponse:
#     """
#     Validates the 'references_name' field in the request.
#
#     Args:
#         request (HttpRequest): The HTTP request containing the data to validate.
#
#     Returns:
#         HttpResponse: A response indicating whether the validation was successful or failed.
#     """
#     return validators.validate_name(request, "references_name")
#
#
# def references_position_validation(request) -> HttpResponse:
#     """
#     Validates the 'references_position' field in the request.
#
#     Args:
#         request (HttpRequest): The HTTP request containing the data to validate.
#
#     Returns:
#         HttpResponse: A response indicating whether the validation was successful or failed.
#     """
#     return validators.validate_name(request, "references_position")
#
#
# def references_company_validation(request) -> HttpResponse:
#     """
#     Validates the 'references_company' field in the request.
#
#     Args:
#         request (HttpRequest): The HTTP request containing the data to validate.
#
#     Returns:
#         HttpResponse: A response indicating whether the validation was successful or failed.
#     """
#     return validators.validate_name(request, "references_company")
#
#
# def references_email_validation(request) -> HttpResponse:
#     """
#     Validates the 'references_email' field in the request.
#
#     Args:
#         request (HttpRequest): The HTTP request containing the data to validate.
#
#     Returns:
#         HttpResponse: A response indicating whether the validation was successful or failed.
#     """
#     return validators.validate_name(request, "references_email")


