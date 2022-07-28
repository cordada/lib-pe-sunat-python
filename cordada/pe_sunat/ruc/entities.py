"""
Utilities for dealing with Peru’s RUC (“Registro Único de Contribuyente”).

RUC "canonical format": No dots ('.'), no hyphen ('-'). Example: ``'20131312955'``.
"""

from __future__ import annotations

import itertools
from typing import ClassVar

from . import constants


class Ruc:
    """
    Representation of a RUC.

    It verifies that the input is syntactically valid and, optionally, that the check digit is
    correct.

    It does NOT check that the value is within boundaries deemed acceptable by the SUNAT (although
    the regular expression used does implicitly impose some) nor that the RUC has actually been
    assigned to some person or entity.

    >>> Ruc('20131312955')
    Ruc('20131312955')
    >>> str(Ruc('20131312955'))
    '20131312955'
    >>> Ruc('20131312955').digits
    '2013131295'
    >>> Ruc('20131312955').check_digit
    '5'
    >>> Ruc('20131312955').canonical
    '20131312955'
    >>> Ruc('20131312955').canonical_with_hyphen
    '2013131295-5'

    >>> Ruc('20131312955') == Ruc('2013131295-5')
    True
    >>> Ruc('20131312955') == Ruc('20.13131295-5')
    True
    """

    INVALID_RUC_MSG: ClassVar[str] = 'Syntactically invalid RUC'

    def __init__(self, value: str, validate_check_digit: bool = False) -> None:
        """
        Constructor.

        :param value: A string that represents a syntactically valid RUC.
        :param validate_check_digit: Whether to validate that the RUC’s check digit
            (“dígito verificador”) is correct.

        :raises ValueError:
        :raises TypeError:
        """

        if isinstance(value, Ruc):
            value = value.canonical
        if not isinstance(value, str):
            raise TypeError('Invalid type')

        clean_value = Ruc.clean_str(value)
        match_obj = constants.RUC_CANONICAL_STRICT_REGEX.match(clean_value)
        if match_obj is None:
            raise ValueError(self.INVALID_RUC_MSG, value)

        match_groups = match_obj.groupdict()
        self._digits = match_groups['digits']
        self._check_digit = match_groups['check_digit']

        if validate_check_digit:
            calculated_check_digit = self.calc_check_digit(self.digits)
            if calculated_check_digit != self.check_digit:
                raise ValueError(
                    'Check digit of RUC is incorrect',
                    value,
                    self.check_digit,
                    calculated_check_digit,
                )

    ########################################################################
    # Properties
    ########################################################################

    @property
    def canonical(self) -> str:
        return f'{self.digits}{self.check_digit}'

    @property
    def canonical_with_hyphen(self) -> str:
        return f'{self.digits}-{self.check_digit}'

    @property
    def digits(self) -> str:
        return self._digits

    @property
    def check_digit(self) -> str:
        return self._check_digit

    ########################################################################
    # Magic methods
    ########################################################################

    def __str__(self) -> str:
        return self.canonical

    def __repr__(self) -> str:
        return f"Ruc('{self.canonical}')"

    def __lt__(self, other: object) -> bool:
        if isinstance(other, Ruc):
            return int(self.digits) < int(other.digits)
        else:
            return NotImplemented

    def __le__(self, other: object) -> bool:
        return self.__lt__(other) or self.__eq__(other)

    def __eq__(self, other: object) -> bool:
        if isinstance(other, Ruc):
            return self.canonical == other.canonical
        return False

    def __hash__(self) -> int:
        # Objects are hashable so they can be used in hashable collections.
        return hash(self.canonical)

    ########################################################################
    # Class methods
    ########################################################################

    @classmethod
    def clean_str(cls, value: str) -> str:
        # Note: Unfortunately `value.strip('.')` does not remove all the occurrences of '.' in
        #   'value' (only the leading and trailing ones).
        clean_value = value.strip().replace('.', '').replace('-', '').upper()
        return clean_value

    @classmethod
    def calc_check_digit(cls, ruc_digits: str) -> str:
        """
        Calculate the check digit (“dígito verificador”) of a RUC’s digits.

        >>> Ruc.calc_check_digit('2013131295')
        '5'
        >>> Ruc.calc_check_digit('2015998121')
        '6'
        >>> Ruc.calc_check_digit('2060470281')
        '1'
        >>> Ruc.calc_check_digit('2060476350')
        '0'
        """
        if not ruc_digits.strip().isdigit():
            raise ValueError("Must be a sequence of digits.")

        # Based on:
        #   - https://gist.github.com/rbonvall/464824/4b07668b83ee45121345e4634ebce10dc6412ba3
        #   - https://es.stackoverflow.com/a/42958/296572
        s = sum(d * f for d, f in zip(map(int, reversed(ruc_digits)), itertools.cycle(range(2, 8))))
        result_alg = 11 - (s % 11)

        CHECK_DIGIT_SPECIAL_CASES = {10: '0', 11: '1'}

        return CHECK_DIGIT_SPECIAL_CASES.get(result_alg, str(result_alg))

    @classmethod
    def random(cls) -> Ruc:
        """
        Generate a random RUC.

        Value will be within proper boundaries and check digit will be calculated appropriately
        (i.e. it will not random).
        """
        raise NotImplementedError
