from __future__ import annotations

import unittest

from cordada.pe_sunat.ruc import entities as ruc_entities


class RucTestCase(unittest.TestCase):
    """
    Tests for :class:`Ruc`.
    """

    valid_ruc_canonical: str
    valid_ruc_check_digit: str
    valid_ruc_digits: str
    valid_ruc_with_hyphen: str
    valid_ruc_with_dots_hyphen: str

    invalid_ruc_canonical: str
    invalid_ruc_check_digit: str
    invalid_ruc_check_digit_valid: str

    valid_ruc_instance: ruc_entities.Ruc
    invalid_ruc_instance: ruc_entities.Ruc
    valid_ruc_instance_copy: ruc_entities.Ruc

    valid_ruc_2_canonical: str
    valid_ruc_2_instance: ruc_entities.Ruc
    valid_ruc_3_canonical: str
    valid_ruc_3_instance: ruc_entities.Ruc

    @classmethod
    def setUpClass(cls) -> None:
        cls.valid_ruc_canonical = '20131312955'
        cls.valid_ruc_check_digit = '5'
        cls.valid_ruc_digits = '2013131295'
        cls.valid_ruc_with_hyphen = '2013131295-5'
        cls.valid_ruc_with_dots_hyphen = '2.013.131.295-5'

        cls.invalid_ruc_canonical = '20131312950'
        cls.invalid_ruc_check_digit = '0'
        cls.invalid_ruc_check_digit_valid = '5'

        cls.valid_ruc_instance = ruc_entities.Ruc(cls.valid_ruc_canonical)
        cls.invalid_ruc_instance = ruc_entities.Ruc(cls.invalid_ruc_canonical)
        cls.valid_ruc_instance_copy = ruc_entities.Ruc(cls.valid_ruc_canonical)

        cls.valid_ruc_2_canonical = '20604702811'
        cls.valid_ruc_2_instance = ruc_entities.Ruc(cls.valid_ruc_2_canonical)
        cls.valid_ruc_3_canonical = '20604763500'
        cls.valid_ruc_3_instance = ruc_entities.Ruc(cls.valid_ruc_3_canonical)

    ########################################################################
    # Instance
    ########################################################################

    def test_fail_type_error(self) -> None:
        for value in [object(), 1, None]:
            with self.assertRaises(TypeError):
                ruc_entities.Ruc(value)  # type: ignore[arg-type]

    def test_ok_same_type(self) -> None:
        self.assertEqual(
            ruc_entities.Ruc(ruc_entities.Ruc('20131312955')),  # type: ignore[arg-type]
            ruc_entities.Ruc('20131312955'),
        )

    def test_instance_empty_string(self) -> None:
        ruc_value = ''
        with self.assertRaises(ValueError) as assert_raises_cm:
            ruc_entities.Ruc(ruc_value)

        exception = assert_raises_cm.exception
        message, value = exception.args
        self.assertEqual(message, 'Syntactically invalid RUC')
        self.assertEqual(value, ruc_value, 'Different RUC value')

    def test_instance_invalid_ruc_format(self) -> None:
        ruc_value = 'invalid ruc format'
        with self.assertRaises(ValueError) as assert_raises_cm:
            ruc_entities.Ruc(ruc_value)

        exception = assert_raises_cm.exception
        message, value = exception.args
        self.assertEqual(message, 'Syntactically invalid RUC')
        self.assertEqual(value, ruc_value, 'Different RUC value')

    def test_instance_validate_check_digit_ok(self) -> None:
        ruc_entities.Ruc(self.valid_ruc_canonical, validate_check_digit=True)

    def test_instance_validate_check_digit_raise_exception(self) -> None:
        with self.assertRaises(ValueError) as assert_raises_cm:
            ruc_entities.Ruc(self.invalid_ruc_canonical, validate_check_digit=True)

        exception = assert_raises_cm.exception
        message, value, check_digit, expected_check_digit = exception.args
        self.assertEqual(message, 'Check digit of RUC is incorrect')
        self.assertEqual(value, self.invalid_ruc_canonical, 'Different RUC value')
        self.assertEqual(check_digit, self.invalid_ruc_check_digit)
        self.assertEqual(expected_check_digit, self.invalid_ruc_check_digit_valid)

    ########################################################################
    # Properties
    ########################################################################

    def test_canonical(self) -> None:
        self.assertEqual(self.valid_ruc_instance.check_digit, self.valid_ruc_check_digit)

    def test_canonical_with_hyphen(self) -> None:
        self.assertEqual(self.valid_ruc_instance.canonical_with_hyphen, self.valid_ruc_with_hyphen)

    def test_digits(self) -> None:
        self.assertEqual(self.valid_ruc_instance.digits, self.valid_ruc_digits)

    def test_check_digit(self) -> None:
        self.assertEqual(self.valid_ruc_instance.check_digit, self.valid_ruc_check_digit)

    ########################################################################
    # Magic methods
    ########################################################################

    def test_str(self) -> None:
        self.assertEqual(str(self.valid_ruc_instance), self.valid_ruc_canonical)

    def test_repr(self) -> None:
        ruc_repr = f"Ruc('{self.valid_ruc_canonical}')"
        self.assertEqual(repr(self.valid_ruc_instance), ruc_repr)

    def test__lt__true(self) -> None:
        # "<"
        self.assertLess(self.valid_ruc_instance, self.valid_ruc_2_instance)
        self.assertLess(self.valid_ruc_2_instance, self.valid_ruc_3_instance)

    def test__lt__false(self) -> None:
        # ">"
        self.assertFalse(self.valid_ruc_2_instance < self.valid_ruc_instance)
        self.assertFalse(self.valid_ruc_3_instance < self.valid_ruc_2_instance)

        # "="
        self.assertFalse(self.valid_ruc_instance < self.valid_ruc_instance_copy)

    def test__lt__not_ruc_instance(self) -> None:
        self.assertIs(self.valid_ruc_instance.__lt__(self.valid_ruc_canonical), NotImplemented)

    def test__le__true(self) -> None:
        # "<"
        self.assertLessEqual(self.valid_ruc_instance, self.valid_ruc_2_instance)
        self.assertLessEqual(self.valid_ruc_2_instance, self.valid_ruc_3_instance)

        # "="
        self.assertLessEqual(self.valid_ruc_instance, self.valid_ruc_instance_copy)

    def test__le__false(self) -> None:
        # ">"
        self.assertFalse(self.valid_ruc_2_instance <= self.valid_ruc_instance)
        self.assertFalse(self.valid_ruc_3_instance <= self.valid_ruc_2_instance)

    def test__le__not_ruc_instance(self) -> None:
        self.assertIs(self.valid_ruc_instance.__le__(self.valid_ruc_canonical), NotImplemented)

    def test__eq__true(self) -> None:
        ruc_instance = ruc_entities.Ruc(self.valid_ruc_canonical)
        self.assertTrue(self.valid_ruc_instance.__eq__(ruc_instance))

    def test__eq__false(self) -> None:
        self.assertFalse(self.valid_ruc_instance.__eq__(self.invalid_ruc_instance))

    def test__eq__not_ruc_instance(self) -> None:
        self.assertFalse(self.valid_ruc_instance.__eq__(self.valid_ruc_canonical))

    def test__gt__true(self) -> None:
        # ">"
        self.assertGreater(self.valid_ruc_2_instance, self.valid_ruc_instance)
        self.assertGreater(self.valid_ruc_3_instance, self.valid_ruc_2_instance)

    def test__gt__false(self) -> None:
        # "<"
        self.assertFalse(self.valid_ruc_instance > self.valid_ruc_2_instance)
        self.assertFalse(self.valid_ruc_2_instance > self.valid_ruc_3_instance)

        # "="
        self.assertFalse(self.valid_ruc_instance > self.valid_ruc_instance_copy)

    def test__gt__not_ruc_instance(self) -> None:
        self.assertIs(
            self.valid_ruc_instance.__gt__(self.valid_ruc_canonical),  # type: ignore[operator]
            NotImplemented,
        )

    def test__ge__true(self) -> None:
        # ">"
        self.assertGreaterEqual(self.valid_ruc_2_instance, self.valid_ruc_instance)
        self.assertGreaterEqual(self.valid_ruc_3_instance, self.valid_ruc_2_instance)

        # "="
        self.assertGreaterEqual(self.valid_ruc_instance, self.valid_ruc_instance_copy)

    def test__ge__false(self) -> None:
        # "<"
        self.assertFalse(self.valid_ruc_instance >= self.valid_ruc_2_instance)
        self.assertFalse(self.valid_ruc_2_instance >= self.valid_ruc_3_instance)

    def test__ge__not_ruc_instance(self) -> None:
        self.assertIs(
            self.valid_ruc_instance.__ge__(self.valid_ruc_canonical),  # type: ignore[operator]
            NotImplemented,
        )

    def test__hash__(self) -> None:
        ruc_hash = hash(self.valid_ruc_instance.canonical)
        self.assertEqual(self.valid_ruc_instance.__hash__(), ruc_hash)

    ########################################################################
    # Class methods
    ########################################################################

    def test_clean_str(self) -> None:
        ruc_value = f'  {self.valid_ruc_with_dots_hyphen}  '
        clean_ruc = ruc_entities.Ruc.clean_str(ruc_value)
        self.assertEqual(clean_ruc, self.valid_ruc_canonical)

    def test_clean_type_error(self) -> None:
        with self.assertRaises(AttributeError) as assert_raises_cm:
            ruc_entities.Ruc.clean_str(1)  # type: ignore[arg-type]

        exception = assert_raises_cm.exception
        self.assertEqual(len(exception.args), 1)
        message = exception.args[0]
        self.assertEqual(message, "'int' object has no attribute 'strip'")

    def test_calc_check_digit_ok(self) -> None:
        check_digit = ruc_entities.Ruc.calc_check_digit(self.valid_ruc_digits)
        self.assertEqual(check_digit, self.valid_ruc_check_digit)

    def test_calc_check_digit_string_uppercase(self) -> None:
        digits = 'A'
        with self.assertRaises(ValueError) as assert_raises_cm:
            ruc_entities.Ruc.calc_check_digit(digits)

        self.assertEqual(list(assert_raises_cm.exception.args), ["Must be a sequence of digits."])

    def test_calc_check_digit_string_lowercase(self) -> None:
        digits = 'a'
        with self.assertRaises(ValueError) as assert_raises_cm:
            ruc_entities.Ruc.calc_check_digit(digits)

        self.assertEqual(list(assert_raises_cm.exception.args), ["Must be a sequence of digits."])
