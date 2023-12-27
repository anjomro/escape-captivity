from abc import ABC, abstractmethod
from urllib.parse import ParseResult


class BaseSolver(ABC):
    """
    Base class for captive portal solvers.
    """

    @abstractmethod
    def applicable(self, portal_url: ParseResult) -> bool:
        """
        Method to check if solver is applicable for given captive portal.
        :param portal_url: URL of captive portal
        :return: True if solver is applicable and can be used, False otherwise
        """
        pass

    @abstractmethod
    def solve(self, portal_url: ParseResult) -> bool:
        """
        Method to solve captive portal.
        :param portal_url: URL of captive portal
        :return: True on success, False otherwise
        """
        pass
