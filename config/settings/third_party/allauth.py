# ACCOUNT_CHANGE_EMAIL = True
# ACCOUNT_EMAIL_NOTIFICATIONS = True
# ACCOUNT_FORMS = {
#     "login": "apps.accounts.forms.CustomLoginForm",
# }

LOGIN_URL = "/accounts/login/"
LOGIN_REDIRECT_URL = "/dashboard/staff/"
ACCOUNT_ADAPTER = "apps.accounts.adapters.MyAccountAdapter"
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_AUTHENTICATION_METHOD = "email"
ACCOUNT_LOGOUT_ON_PASSWORD_CHANGE = True
ACCOUNT_EMAIL_CONFIRMATION_EXPIRE_DAYS = 1
ACCOUNT_EMAIL_VERIFICATION = "mandatory"
ACCOUNT_LOGOUT_ON_PASSWORD_CHANGE = True
ACCOUNT_EMAIL_CONFIRMATION_EXPIRE_DAYS = 1
ACCOUNT_UNIQUE_EMAIL = True
ACCOUNT_SESSION_REMEMBER = True
# ACCOUNT_SIGNUP_FORM_CLASS = "apps.accounts.forms.CustomSignupForm"
