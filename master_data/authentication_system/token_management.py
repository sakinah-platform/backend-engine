from typing import Type, Sequence, Optional

from rest_framework.authentication import BaseAuthentication
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_registration.auth_token_managers import AbstractAuthTokenManager, AuthToken
from rest_framework_simplejwt.tokens import RefreshToken
from rest_registration.exceptions import AuthTokenNotRevoked


class SimpleJWTAuthTokenManager(AbstractAuthTokenManager):

    def get_authentication_class(self) -> Type[BaseAuthentication]:

        raise JWTAuthentication

    def get_app_names(self) -> Sequence[str]:
        """
        Return the Django app names which need to be installed so
        this token manager class works properly.

        Overriding this method is not required but recommended as it provides
        additional check during the Django startup.
        """
        return [
            'rest_framework_simplejwt.authentication',
        ]

    def provide_token(self, user: 'AbstractBaseUser'):
        """
        Get or create token for given user.
        If there is no token to provide,
        raise ``rest_registration.exceptions.AuthTokenError``.
        """
        refresh = RefreshToken.for_user(user)

        return {
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }

    def revoke_token(
            self, user: 'AbstractBaseUser', *,
            token: Optional[AuthToken] = None) -> None:

        """
        Revoke the given token for a given user. If the token is not provided,
        revoke all tokens for given user.
        If the provided token is invalid or there is no token to revoke,
        raise ``rest_registration.exceptions.AuthTokenError``.

        This method may not be implemented in all cases - for instance, in case
        when the token is cryptographically generated and not stored
        in the database.
        """

        pass