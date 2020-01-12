import unittest
from board import UBoard


class UBoardTest(unittest.TestCase):
    def test_board_constructor(self):
        b = UBoard([])
        self.assertEqual(b.moves, [])
        b_sup = b.super_board
        binary = [[[0, 0], [0, 0], [0, 0]],
                  [[0, 0], [0, 0], [0, 0]],
                  [[0, 0], [0, 0], [0, 0]]]
        self.assertEqual(b_sup.get_binary_board('X'), binary)
        b_subs = b.sub_boards
        for key in b_subs.keys():
            self.assertEqual(b_subs[key].get_binary_board('X'), binary)

    def test_ternary_to_decimal1(self):
        actual_output = UBoard._UBoard__ternary_to_decimal('00')
        expected_output = 0
        self.assertEqual(expected_output, actual_output)

    def test_ternary_to_decimal2(self):
        actual_output = UBoard._UBoard__ternary_to_decimal('01')
        expected_output = 1
        self.assertEqual(expected_output, actual_output)

    def test_ternary_to_decimal3(self):
        actual_output = UBoard._UBoard__ternary_to_decimal('02')
        expected_output = 2
        self.assertEqual(expected_output, actual_output)

    def test_ternary_to_decimal4(self):
        actual_output = UBoard._UBoard__ternary_to_decimal('10')
        expected_output = 3
        self.assertEqual(expected_output, actual_output)

    def test_ternary_to_decimal5(self):
        actual_output = UBoard._UBoard__ternary_to_decimal('11')
        expected_output = 4
        self.assertEqual(expected_output, actual_output)

    def test_ternary_to_decimal6(self):
        actual_output = UBoard._UBoard__ternary_to_decimal('12')
        expected_output = 5
        self.assertEqual(expected_output, actual_output)

    def test_ternary_to_decimal7(self):
        actual_output = UBoard._UBoard__ternary_to_decimal('20')
        expected_output = 6
        self.assertEqual(expected_output, actual_output)

    def test_ternary_to_decimal8(self):
        actual_output = UBoard._UBoard__ternary_to_decimal('21')
        expected_output = 7
        self.assertEqual(expected_output, actual_output)

    def test_ternary_to_decimal9(self):
        actual_output = UBoard._UBoard__ternary_to_decimal('22')
        expected_output = 8
        self.assertEqual(expected_output, actual_output)

    def test_get_sub_board_square0(self):
        actual_output = UBoard._UBoard__get_sub_board_square(0)
        expected_output = 0
        self.assertEqual(expected_output, actual_output)

    def test_get_sub_board_square1(self):
        actual_output = UBoard._UBoard__get_sub_board_square(1)
        expected_output = 1
        self.assertEqual(expected_output, actual_output)

    def test_get_sub_board_square2(self):
        actual_output = UBoard._UBoard__get_sub_board_square(2)
        expected_output = 2
        self.assertEqual(expected_output, actual_output)

    def test_get_sub_board_square3(self):
        actual_output = UBoard._UBoard__get_sub_board_square(3)
        expected_output = 0
        self.assertEqual(expected_output, actual_output)

    def test_get_sub_board_square4(self):
        actual_output = UBoard._UBoard__get_sub_board_square(4)
        expected_output = 1
        self.assertEqual(expected_output, actual_output)

    def test_get_sub_board_square5(self):
        actual_output = UBoard._UBoard__get_sub_board_square(5)
        expected_output = 2
        self.assertEqual(expected_output, actual_output)

    def test_get_sub_board_square6(self):
        actual_output = UBoard._UBoard__get_sub_board_square(6)
        expected_output = 0
        self.assertEqual(expected_output, actual_output)

    def test_get_sub_board_square7(self):
        actual_output = UBoard._UBoard__get_sub_board_square(7)
        expected_output = 1
        self.assertEqual(expected_output, actual_output)

    def test_get_sub_board_square8(self):
        actual_output = UBoard._UBoard__get_sub_board_square(8)
        expected_output = 2
        self.assertEqual(expected_output, actual_output)

    def test_get_sub_board_square9(self):
        actual_output = UBoard._UBoard__get_sub_board_square(9)
        expected_output = 3
        self.assertEqual(expected_output, actual_output)

    def test_get_sub_board_square10(self):
        actual_output = UBoard._UBoard__get_sub_board_square(10)
        expected_output = 4
        self.assertEqual(expected_output, actual_output)

    def test_get_sub_board_square11(self):
        actual_output = UBoard._UBoard__get_sub_board_square(11)
        expected_output = 5
        self.assertEqual(expected_output, actual_output)

    def test_get_sub_board_square12(self):
        actual_output = UBoard._UBoard__get_sub_board_square(12)
        expected_output = 3
        self.assertEqual(expected_output, actual_output)

    def test_get_sub_board_square13(self):
        actual_output = UBoard._UBoard__get_sub_board_square(13)
        expected_output = 4
        self.assertEqual(expected_output, actual_output)

    def test_get_sub_board_square14(self):
        actual_output = UBoard._UBoard__get_sub_board_square(14)
        expected_output = 5
        self.assertEqual(expected_output, actual_output)

    def test_get_sub_board_square15(self):
        actual_output = UBoard._UBoard__get_sub_board_square(15)
        expected_output = 3
        self.assertEqual(expected_output, actual_output)

    def test_get_sub_board_square16(self):
        actual_output = UBoard._UBoard__get_sub_board_square(16)
        expected_output = 4
        self.assertEqual(expected_output, actual_output)

    def test_get_sub_board_square17(self):
        actual_output = UBoard._UBoard__get_sub_board_square(17)
        expected_output = 5
        self.assertEqual(expected_output, actual_output)

    def test_get_sub_board_square18(self):
        actual_output = UBoard._UBoard__get_sub_board_square(18)
        expected_output = 6
        self.assertEqual(expected_output, actual_output)

    def test_get_sub_board_square19(self):
        actual_output = UBoard._UBoard__get_sub_board_square(19)
        expected_output = 7
        self.assertEqual(expected_output, actual_output)

    def test_get_sub_board_square20(self):
        actual_output = UBoard._UBoard__get_sub_board_square(20)
        expected_output = 8
        self.assertEqual(expected_output, actual_output)

    def test_get_sub_board_square21(self):
        actual_output = UBoard._UBoard__get_sub_board_square(21)
        expected_output = 6
        self.assertEqual(expected_output, actual_output)

    def test_get_sub_board_square22(self):
        actual_output = UBoard._UBoard__get_sub_board_square(22)
        expected_output = 7
        self.assertEqual(expected_output, actual_output)

    def test_get_sub_board_square23(self):
        actual_output = UBoard._UBoard__get_sub_board_square(23)
        expected_output = 8
        self.assertEqual(expected_output, actual_output)

    def test_get_sub_board_square24(self):
        actual_output = UBoard._UBoard__get_sub_board_square(24)
        expected_output = 6
        self.assertEqual(expected_output, actual_output)

    def test_get_sub_board_square25(self):
        actual_output = UBoard._UBoard__get_sub_board_square(25)
        expected_output = 7
        self.assertEqual(expected_output, actual_output)

    def test_get_sub_board_square26(self):
        actual_output = UBoard._UBoard__get_sub_board_square(26)
        expected_output = 8
        self.assertEqual(expected_output, actual_output)

    def test_get_sub_board_square27(self):
        actual_output = UBoard._UBoard__get_sub_board_square(27)
        expected_output = 0
        self.assertEqual(expected_output, actual_output)

    def test_get_sub_board_square28(self):
        actual_output = UBoard._UBoard__get_sub_board_square(28)
        expected_output = 1
        self.assertEqual(expected_output, actual_output)

    def test_get_sub_board_square29(self):
        actual_output = UBoard._UBoard__get_sub_board_square(29)
        expected_output = 2
        self.assertEqual(expected_output, actual_output)

    def test_get_sub_board_square30(self):
        actual_output = UBoard._UBoard__get_sub_board_square(30)
        expected_output = 0
        self.assertEqual(expected_output, actual_output)

    def test_get_sub_board_square31(self):
        actual_output = UBoard._UBoard__get_sub_board_square(31)
        expected_output = 1
        self.assertEqual(expected_output, actual_output)

    def test_get_sub_board_square32(self):
        actual_output = UBoard._UBoard__get_sub_board_square(32)
        expected_output = 2
        self.assertEqual(expected_output, actual_output)

    def test_get_sub_board_square33(self):
        actual_output = UBoard._UBoard__get_sub_board_square(33)
        expected_output = 0
        self.assertEqual(expected_output, actual_output)

    def test_get_sub_board_square34(self):
        actual_output = UBoard._UBoard__get_sub_board_square(34)
        expected_output = 1
        self.assertEqual(expected_output, actual_output)

    def test_get_sub_board_square35(self):
        actual_output = UBoard._UBoard__get_sub_board_square(35)
        expected_output = 2
        self.assertEqual(expected_output, actual_output)

    def test_get_sub_board_square36(self):
        actual_output = UBoard._UBoard__get_sub_board_square(36)
        expected_output = 3
        self.assertEqual(expected_output, actual_output)

    def test_get_sub_board_square37(self):
        actual_output = UBoard._UBoard__get_sub_board_square(37)
        expected_output = 4
        self.assertEqual(expected_output, actual_output)

    def test_get_sub_board_square38(self):
        actual_output = UBoard._UBoard__get_sub_board_square(38)
        expected_output = 5
        self.assertEqual(expected_output, actual_output)

    def test_get_sub_board_square39(self):
        actual_output = UBoard._UBoard__get_sub_board_square(39)
        expected_output = 3
        self.assertEqual(expected_output, actual_output)

    def test_get_sub_board_square40(self):
        actual_output = UBoard._UBoard__get_sub_board_square(40)
        expected_output = 4
        self.assertEqual(expected_output, actual_output)

    def test_get_sub_board_square41(self):
        actual_output = UBoard._UBoard__get_sub_board_square(41)
        expected_output = 5
        self.assertEqual(expected_output, actual_output)

    def test_get_sub_board_square42(self):
        actual_output = UBoard._UBoard__get_sub_board_square(42)
        expected_output = 3
        self.assertEqual(expected_output, actual_output)

    def test_get_sub_board_square43(self):
        actual_output = UBoard._UBoard__get_sub_board_square(43)
        expected_output = 4
        self.assertEqual(expected_output, actual_output)

    def test_get_sub_board_square44(self):
        actual_output = UBoard._UBoard__get_sub_board_square(44)
        expected_output = 5
        self.assertEqual(expected_output, actual_output)

    def test_get_sub_board_square45(self):
        actual_output = UBoard._UBoard__get_sub_board_square(45)
        expected_output = 6
        self.assertEqual(expected_output, actual_output)

    def test_get_sub_board_square46(self):
        actual_output = UBoard._UBoard__get_sub_board_square(46)
        expected_output = 7
        self.assertEqual(expected_output, actual_output)

    def test_get_sub_board_square47(self):
        actual_output = UBoard._UBoard__get_sub_board_square(47)
        expected_output = 8
        self.assertEqual(expected_output, actual_output)

    def test_get_sub_board_square48(self):
        actual_output = UBoard._UBoard__get_sub_board_square(48)
        expected_output = 6
        self.assertEqual(expected_output, actual_output)

    def test_get_sub_board_square49(self):
        actual_output = UBoard._UBoard__get_sub_board_square(49)
        expected_output = 7
        self.assertEqual(expected_output, actual_output)

    def test_get_sub_board_square50(self):
        actual_output = UBoard._UBoard__get_sub_board_square(50)
        expected_output = 8
        self.assertEqual(expected_output, actual_output)

    def test_get_sub_board_square51(self):
        actual_output = UBoard._UBoard__get_sub_board_square(51)
        expected_output = 6
        self.assertEqual(expected_output, actual_output)

    def test_get_sub_board_square52(self):
        actual_output = UBoard._UBoard__get_sub_board_square(52)
        expected_output = 7
        self.assertEqual(expected_output, actual_output)

    def test_get_sub_board_square53(self):
        actual_output = UBoard._UBoard__get_sub_board_square(53)
        expected_output = 8
        self.assertEqual(expected_output, actual_output)

    def test_get_sub_board_square54(self):
        actual_output = UBoard._UBoard__get_sub_board_square(54)
        expected_output = 0
        self.assertEqual(expected_output, actual_output)

    def test_get_sub_board_square55(self):
        actual_output = UBoard._UBoard__get_sub_board_square(55)
        expected_output = 1
        self.assertEqual(expected_output, actual_output)

    def test_get_sub_board_square56(self):
        actual_output = UBoard._UBoard__get_sub_board_square(56)
        expected_output = 2
        self.assertEqual(expected_output, actual_output)

    def test_get_sub_board_square57(self):
        actual_output = UBoard._UBoard__get_sub_board_square(57)
        expected_output = 0
        self.assertEqual(expected_output, actual_output)

    def test_get_sub_board_square58(self):
        actual_output = UBoard._UBoard__get_sub_board_square(58)
        expected_output = 1
        self.assertEqual(expected_output, actual_output)

    def test_get_sub_board_square59(self):
        actual_output = UBoard._UBoard__get_sub_board_square(59)
        expected_output = 2
        self.assertEqual(expected_output, actual_output)

    def test_get_sub_board_square60(self):
        actual_output = UBoard._UBoard__get_sub_board_square(60)
        expected_output = 0
        self.assertEqual(expected_output, actual_output)

    def test_get_sub_board_square61(self):
        actual_output = UBoard._UBoard__get_sub_board_square(61)
        expected_output = 1
        self.assertEqual(expected_output, actual_output)

    def test_get_sub_board_square62(self):
        actual_output = UBoard._UBoard__get_sub_board_square(62)
        expected_output = 2
        self.assertEqual(expected_output, actual_output)

    def test_get_sub_board_square63(self):
        actual_output = UBoard._UBoard__get_sub_board_square(63)
        expected_output = 3
        self.assertEqual(expected_output, actual_output)

    def test_get_sub_board_square64(self):
        actual_output = UBoard._UBoard__get_sub_board_square(64)
        expected_output = 4
        self.assertEqual(expected_output, actual_output)

    def test_get_sub_board_square65(self):
        actual_output = UBoard._UBoard__get_sub_board_square(65)
        expected_output = 5
        self.assertEqual(expected_output, actual_output)

    def test_get_sub_board_square66(self):
        actual_output = UBoard._UBoard__get_sub_board_square(66)
        expected_output = 3
        self.assertEqual(expected_output, actual_output)

    def test_get_sub_board_square67(self):
        actual_output = UBoard._UBoard__get_sub_board_square(67)
        expected_output = 4
        self.assertEqual(expected_output, actual_output)

    def test_get_sub_board_square68(self):
        actual_output = UBoard._UBoard__get_sub_board_square(68)
        expected_output = 5
        self.assertEqual(expected_output, actual_output)

    def test_get_sub_board_square69(self):
        actual_output = UBoard._UBoard__get_sub_board_square(69)
        expected_output = 3
        self.assertEqual(expected_output, actual_output)

    def test_get_sub_board_square70(self):
        actual_output = UBoard._UBoard__get_sub_board_square(70)
        expected_output = 4
        self.assertEqual(expected_output, actual_output)

    def test_get_sub_board_square71(self):
        actual_output = UBoard._UBoard__get_sub_board_square(71)
        expected_output = 5
        self.assertEqual(expected_output, actual_output)

    def test_get_sub_board_square72(self):
        actual_output = UBoard._UBoard__get_sub_board_square(72)
        expected_output = 6
        self.assertEqual(expected_output, actual_output)

    def test_get_sub_board_square73(self):
        actual_output = UBoard._UBoard__get_sub_board_square(73)
        expected_output = 7
        self.assertEqual(expected_output, actual_output)

    def test_get_sub_board_square74(self):
        actual_output = UBoard._UBoard__get_sub_board_square(74)
        expected_output = 8
        self.assertEqual(expected_output, actual_output)

    def test_get_sub_board_square75(self):
        actual_output = UBoard._UBoard__get_sub_board_square(75)
        expected_output = 6
        self.assertEqual(expected_output, actual_output)

    def test_get_sub_board_square76(self):
        actual_output = UBoard._UBoard__get_sub_board_square(76)
        expected_output = 7
        self.assertEqual(expected_output, actual_output)

    def test_get_sub_board_square77(self):
        actual_output = UBoard._UBoard__get_sub_board_square(77)
        expected_output = 8
        self.assertEqual(expected_output, actual_output)

    def test_get_sub_board_square78(self):
        actual_output = UBoard._UBoard__get_sub_board_square(78)
        expected_output = 6
        self.assertEqual(expected_output, actual_output)

    def test_get_sub_board_square79(self):
        actual_output = UBoard._UBoard__get_sub_board_square(79)
        expected_output = 7
        self.assertEqual(expected_output, actual_output)

    def test_get_sub_board_square80(self):
        actual_output = UBoard._UBoard__get_sub_board_square(80)
        expected_output = 8
        self.assertEqual(expected_output, actual_output)

    def test_get_super_board_square0(self):
        actual_output = UBoard._UBoard__get_super_board_square(0)
        expected_output = 0
        self.assertEqual(expected_output, actual_output)

    def test_get_super_board_square1(self):
        actual_output = UBoard._UBoard__get_super_board_square(1)
        expected_output = 0
        self.assertEqual(expected_output, actual_output)

    def test_get_super_board_square2(self):
        actual_output = UBoard._UBoard__get_super_board_square(2)
        expected_output = 0
        self.assertEqual(expected_output, actual_output)

    def test_get_super_board_square3(self):
        actual_output = UBoard._UBoard__get_super_board_square(3)
        expected_output = 1
        self.assertEqual(expected_output, actual_output)

    def test_get_super_board_square4(self):
        actual_output = UBoard._UBoard__get_super_board_square(4)
        expected_output = 1
        self.assertEqual(expected_output, actual_output)

    def test_get_super_board_square5(self):
        actual_output = UBoard._UBoard__get_super_board_square(5)
        expected_output = 1
        self.assertEqual(expected_output, actual_output)

    def test_get_super_board_square6(self):
        actual_output = UBoard._UBoard__get_super_board_square(6)
        expected_output = 2
        self.assertEqual(expected_output, actual_output)

    def test_get_super_board_square7(self):
        actual_output = UBoard._UBoard__get_super_board_square(7)
        expected_output = 2
        self.assertEqual(expected_output, actual_output)

    def test_get_super_board_square8(self):
        actual_output = UBoard._UBoard__get_super_board_square(8)
        expected_output = 2
        self.assertEqual(expected_output, actual_output)

    def test_get_super_board_square9(self):
        actual_output = UBoard._UBoard__get_super_board_square(9)
        expected_output = 0
        self.assertEqual(expected_output, actual_output)

    def test_get_super_board_square10(self):
        actual_output = UBoard._UBoard__get_super_board_square(10)
        expected_output = 0
        self.assertEqual(expected_output, actual_output)

    def test_get_super_board_square11(self):
        actual_output = UBoard._UBoard__get_super_board_square(11)
        expected_output = 0
        self.assertEqual(expected_output, actual_output)

    def test_get_super_board_square12(self):
        actual_output = UBoard._UBoard__get_super_board_square(12)
        expected_output = 1
        self.assertEqual(expected_output, actual_output)

    def test_get_super_board_square13(self):
        actual_output = UBoard._UBoard__get_super_board_square(13)
        expected_output = 1
        self.assertEqual(expected_output, actual_output)

    def test_get_super_board_square14(self):
        actual_output = UBoard._UBoard__get_super_board_square(14)
        expected_output = 1
        self.assertEqual(expected_output, actual_output)

    def test_get_super_board_square15(self):
        actual_output = UBoard._UBoard__get_super_board_square(15)
        expected_output = 2
        self.assertEqual(expected_output, actual_output)

    def test_get_super_board_square16(self):
        actual_output = UBoard._UBoard__get_super_board_square(16)
        expected_output = 2
        self.assertEqual(expected_output, actual_output)

    def test_get_super_board_square17(self):
        actual_output = UBoard._UBoard__get_super_board_square(17)
        expected_output = 2
        self.assertEqual(expected_output, actual_output)

    def test_get_super_board_square18(self):
        actual_output = UBoard._UBoard__get_super_board_square(18)
        expected_output = 0
        self.assertEqual(expected_output, actual_output)

    def test_get_super_board_square19(self):
        actual_output = UBoard._UBoard__get_super_board_square(19)
        expected_output = 0
        self.assertEqual(expected_output, actual_output)

    def test_get_super_board_square20(self):
        actual_output = UBoard._UBoard__get_super_board_square(20)
        expected_output = 0
        self.assertEqual(expected_output, actual_output)

    def test_get_super_board_square21(self):
        actual_output = UBoard._UBoard__get_super_board_square(21)
        expected_output = 1
        self.assertEqual(expected_output, actual_output)

    def test_get_super_board_square22(self):
        actual_output = UBoard._UBoard__get_super_board_square(22)
        expected_output = 1
        self.assertEqual(expected_output, actual_output)

    def test_get_super_board_square23(self):
        actual_output = UBoard._UBoard__get_super_board_square(23)
        expected_output = 1
        self.assertEqual(expected_output, actual_output)

    def test_get_super_board_square24(self):
        actual_output = UBoard._UBoard__get_super_board_square(24)
        expected_output = 2
        self.assertEqual(expected_output, actual_output)

    def test_get_super_board_square25(self):
        actual_output = UBoard._UBoard__get_super_board_square(25)
        expected_output = 2
        self.assertEqual(expected_output, actual_output)

    def test_get_super_board_square26(self):
        actual_output = UBoard._UBoard__get_super_board_square(26)
        expected_output = 2
        self.assertEqual(expected_output, actual_output)

    def test_get_super_board_square27(self):
        actual_output = UBoard._UBoard__get_super_board_square(27)
        expected_output = 3
        self.assertEqual(expected_output, actual_output)

    def test_get_super_board_square28(self):
        actual_output = UBoard._UBoard__get_super_board_square(28)
        expected_output = 3
        self.assertEqual(expected_output, actual_output)

    def test_get_super_board_square29(self):
        actual_output = UBoard._UBoard__get_super_board_square(29)
        expected_output = 3
        self.assertEqual(expected_output, actual_output)

    def test_get_super_board_square30(self):
        actual_output = UBoard._UBoard__get_super_board_square(30)
        expected_output = 4
        self.assertEqual(expected_output, actual_output)

    def test_get_super_board_square31(self):
        actual_output = UBoard._UBoard__get_super_board_square(31)
        expected_output = 4
        self.assertEqual(expected_output, actual_output)

    def test_get_super_board_square32(self):
        actual_output = UBoard._UBoard__get_super_board_square(32)
        expected_output =4
        self.assertEqual(expected_output, actual_output)

    def test_get_super_board_square33(self):
        actual_output = UBoard._UBoard__get_super_board_square(33)
        expected_output = 5
        self.assertEqual(expected_output, actual_output)

    def test_get_super_board_square34(self):
        actual_output = UBoard._UBoard__get_super_board_square(34)
        expected_output = 5
        self.assertEqual(expected_output, actual_output)

    def test_get_super_board_square35(self):
        actual_output = UBoard._UBoard__get_super_board_square(35)
        expected_output = 5
        self.assertEqual(expected_output, actual_output)

    def test_get_super_board_square36(self):
        actual_output = UBoard._UBoard__get_super_board_square(36)
        expected_output = 3
        self.assertEqual(expected_output, actual_output)

    def test_get_super_board_square37(self):
        actual_output = UBoard._UBoard__get_super_board_square(37)
        expected_output = 3
        self.assertEqual(expected_output, actual_output)

    def test_get_super_board_square38(self):
        actual_output = UBoard._UBoard__get_super_board_square(38)
        expected_output = 3
        self.assertEqual(expected_output, actual_output)

    def test_get_super_board_square39(self):
        actual_output = UBoard._UBoard__get_super_board_square(39)
        expected_output = 4
        self.assertEqual(expected_output, actual_output)

    def test_get_super_board_square40(self):
        actual_output = UBoard._UBoard__get_super_board_square(40)
        expected_output = 4
        self.assertEqual(expected_output, actual_output)

    def test_get_super_board_square41(self):
        actual_output = UBoard._UBoard__get_super_board_square(41)
        expected_output = 4
        self.assertEqual(expected_output, actual_output)

    def test_get_super_board_square42(self):
        actual_output = UBoard._UBoard__get_super_board_square(42)
        expected_output = 5
        self.assertEqual(expected_output, actual_output)

    def test_get_super_board_square43(self):
        actual_output = UBoard._UBoard__get_super_board_square(43)
        expected_output = 5
        self.assertEqual(expected_output, actual_output)

    def test_get_super_board_square44(self):
        actual_output = UBoard._UBoard__get_super_board_square(44)
        expected_output = 5
        self.assertEqual(expected_output, actual_output)

    def test_get_super_board_square45(self):
        actual_output = UBoard._UBoard__get_super_board_square(45)
        expected_output = 3
        self.assertEqual(expected_output, actual_output)

    def test_get_super_board_square46(self):
        actual_output = UBoard._UBoard__get_super_board_square(46)
        expected_output = 3
        self.assertEqual(expected_output, actual_output)

    def test_get_super_board_square47(self):
        actual_output = UBoard._UBoard__get_super_board_square(47)
        expected_output = 3
        self.assertEqual(expected_output, actual_output)

    def test_get_super_board_square48(self):
        actual_output = UBoard._UBoard__get_super_board_square(48)
        expected_output = 4
        self.assertEqual(expected_output, actual_output)

    def test_get_super_board_square49(self):
        actual_output = UBoard._UBoard__get_super_board_square(49)
        expected_output = 4
        self.assertEqual(expected_output, actual_output)

    def test_get_super_board_square50(self):
        actual_output = UBoard._UBoard__get_super_board_square(50)
        expected_output = 4
        self.assertEqual(expected_output, actual_output)

    def test_get_super_board_square51(self):
        actual_output = UBoard._UBoard__get_super_board_square(51)
        expected_output = 5
        self.assertEqual(expected_output, actual_output)

    def test_get_super_board_square52(self):
        actual_output = UBoard._UBoard__get_super_board_square(52)
        expected_output = 5
        self.assertEqual(expected_output, actual_output)

    def test_get_super_board_square53(self):
        actual_output = UBoard._UBoard__get_super_board_square(53)
        expected_output = 5
        self.assertEqual(expected_output, actual_output)

    def test_get_super_board_square54(self):
        actual_output = UBoard._UBoard__get_super_board_square(54)
        expected_output = 6
        self.assertEqual(expected_output, actual_output)

    def test_get_super_board_square55(self):
        actual_output = UBoard._UBoard__get_super_board_square(55)
        expected_output = 6
        self.assertEqual(expected_output, actual_output)

    def test_get_super_board_square56(self):
        actual_output = UBoard._UBoard__get_super_board_square(56)
        expected_output = 6
        self.assertEqual(expected_output, actual_output)

    def test_get_super_board_square57(self):
        actual_output = UBoard._UBoard__get_super_board_square(57)
        expected_output = 7
        self.assertEqual(expected_output, actual_output)

    def test_get_super_board_square58(self):
        actual_output = UBoard._UBoard__get_super_board_square(58)
        expected_output = 7
        self.assertEqual(expected_output, actual_output)

    def test_get_super_board_square59(self):
        actual_output = UBoard._UBoard__get_super_board_square(59)
        expected_output = 7
        self.assertEqual(expected_output, actual_output)

    def test_get_super_board_square60(self):
        actual_output = UBoard._UBoard__get_super_board_square(60)
        expected_output = 8
        self.assertEqual(expected_output, actual_output)

    def test_get_super_board_square61(self):
        actual_output = UBoard._UBoard__get_super_board_square(61)
        expected_output = 8
        self.assertEqual(expected_output, actual_output)

    def test_get_super_board_square62(self):
        actual_output = UBoard._UBoard__get_super_board_square(62)
        expected_output = 8
        self.assertEqual(expected_output, actual_output)

    def test_get_super_board_square63(self):
        actual_output = UBoard._UBoard__get_super_board_square(63)
        expected_output = 6
        self.assertEqual(expected_output, actual_output)

    def test_get_super_board_square64(self):
        actual_output = UBoard._UBoard__get_super_board_square(64)
        expected_output = 6
        self.assertEqual(expected_output, actual_output)

    def test_get_super_board_square65(self):
        actual_output = UBoard._UBoard__get_super_board_square(65)
        expected_output = 6
        self.assertEqual(expected_output, actual_output)

    def test_get_super_board_square66(self):
        actual_output = UBoard._UBoard__get_super_board_square(66)
        expected_output = 7
        self.assertEqual(expected_output, actual_output)

    def test_get_super_board_square67(self):
        actual_output = UBoard._UBoard__get_super_board_square(67)
        expected_output = 7
        self.assertEqual(expected_output, actual_output)

    def test_get_super_board_square68(self):
        actual_output = UBoard._UBoard__get_super_board_square(68)
        expected_output = 7
        self.assertEqual(expected_output, actual_output)

    def test_get_super_board_square69(self):
        actual_output = UBoard._UBoard__get_super_board_square(69)
        expected_output = 8
        self.assertEqual(expected_output, actual_output)

    def test_get_super_board_square70(self):
        actual_output = UBoard._UBoard__get_super_board_square(70)
        expected_output = 8
        self.assertEqual(expected_output, actual_output)

    def test_get_super_board_square71(self):
        actual_output = UBoard._UBoard__get_super_board_square(71)
        expected_output = 8
        self.assertEqual(expected_output, actual_output)

    def test_get_super_board_square72(self):
        actual_output = UBoard._UBoard__get_super_board_square(72)
        expected_output = 6
        self.assertEqual(expected_output, actual_output)

    def test_get_super_board_square73(self):
        actual_output = UBoard._UBoard__get_super_board_square(73)
        expected_output = 6
        self.assertEqual(expected_output, actual_output)

    def test_get_super_board_square74(self):
        actual_output = UBoard._UBoard__get_super_board_square(74)
        expected_output = 6
        self.assertEqual(expected_output, actual_output)

    def test_get_super_board_square75(self):
        actual_output = UBoard._UBoard__get_super_board_square(75)
        expected_output = 7
        self.assertEqual(expected_output, actual_output)

    def test_get_super_board_square76(self):
        actual_output = UBoard._UBoard__get_super_board_square(76)
        expected_output = 7
        self.assertEqual(expected_output, actual_output)

    def test_get_super_board_square77(self):
        actual_output = UBoard._UBoard__get_super_board_square(77)
        expected_output = 7
        self.assertEqual(expected_output, actual_output)

    def test_get_super_board_square78(self):
        actual_output = UBoard._UBoard__get_super_board_square(78)
        expected_output = 8
        self.assertEqual(expected_output, actual_output)

    def test_get_super_board_square79(self):
        actual_output = UBoard._UBoard__get_super_board_square(79)
        expected_output = 8
        self.assertEqual(expected_output, actual_output)

    def test_get_super_board_square80(self):
        actual_output = UBoard._UBoard__get_super_board_square(80)
        expected_output = 8
        self.assertEqual(expected_output, actual_output)

    def test_get_board0(self):
        actual_board, actual_board_id, actual_move = UBoard._UBoard__get_board(UBoard([]), 0)
        expected_board_id = 0
        expected_move = 0
        self.assertEqual(expected_board_id, actual_board_id)
        self.assertEqual(expected_move, actual_move)

    def test_get_board1(self):
        actual_board, actual_board_id, actual_move = UBoard._UBoard__get_board(UBoard([]), 1)
        expected_board_id = 0
        expected_move = 1
        self.assertEqual(expected_board_id, actual_board_id)
        self.assertEqual(expected_move, actual_move)

    def test_get_board2(self):
        actual_board, actual_board_id, actual_move = UBoard._UBoard__get_board(UBoard([]), 2)
        expected_board_id = 0
        expected_move = 2
        self.assertEqual(expected_board_id, actual_board_id)
        self.assertEqual(expected_move, actual_move)

    def test_get_board3(self):
        actual_board, actual_board_id, actual_move = UBoard._UBoard__get_board(UBoard([]), 3)
        expected_board_id = 1
        expected_move = 0
        self.assertEqual(expected_board_id, actual_board_id)
        self.assertEqual(expected_move, actual_move)

    def test_get_board4(self):
        actual_board, actual_board_id, actual_move = UBoard._UBoard__get_board(UBoard([]), 4)
        expected_board_id = 1
        expected_move = 1
        self.assertEqual(expected_board_id, actual_board_id)
        self.assertEqual(expected_move, actual_move)

    def test_get_board5(self):
        actual_board, actual_board_id, actual_move = UBoard._UBoard__get_board(UBoard([]), 5)
        expected_board_id = 1
        expected_move = 2
        self.assertEqual(expected_board_id, actual_board_id)
        self.assertEqual(expected_move, actual_move)

    def test_get_board6(self):
        actual_board, actual_board_id, actual_move = UBoard._UBoard__get_board(UBoard([]), 6)
        expected_board_id = 2
        expected_move = 0
        self.assertEqual(expected_board_id, actual_board_id)
        self.assertEqual(expected_move, actual_move)

    def test_get_board7(self):
        actual_board, actual_board_id, actual_move = UBoard._UBoard__get_board(UBoard([]), 7)
        expected_board_id = 2
        expected_move = 1
        self.assertEqual(expected_board_id, actual_board_id)
        self.assertEqual(expected_move, actual_move)

    def test_get_board8(self):
        actual_board, actual_board_id, actual_move = UBoard._UBoard__get_board(UBoard([]), 8)
        expected_board_id = 2
        expected_move = 2
        self.assertEqual(expected_board_id, actual_board_id)
        self.assertEqual(expected_move, actual_move)

    def test_get_board9(self):
        actual_board, actual_board_id, actual_move = UBoard._UBoard__get_board(UBoard([]), 9)
        expected_board_id = 0
        expected_move = 3
        self.assertEqual(expected_board_id, actual_board_id)
        self.assertEqual(expected_move, actual_move)

    def test_get_board10(self):
        actual_board, actual_board_id, actual_move = UBoard._UBoard__get_board(UBoard([]), 10)
        expected_board_id = 0
        expected_move = 4
        self.assertEqual(expected_board_id, actual_board_id)
        self.assertEqual(expected_move, actual_move)

    def test_get_board11(self):
        actual_board, actual_board_id, actual_move = UBoard._UBoard__get_board(UBoard([]), 11)
        expected_board_id = 0
        expected_move = 5
        self.assertEqual(expected_board_id, actual_board_id)
        self.assertEqual(expected_move, actual_move)

    def test_get_board12(self):
        actual_board, actual_board_id, actual_move = UBoard._UBoard__get_board(UBoard([]), 12)
        expected_board_id = 1
        expected_move = 3
        self.assertEqual(expected_board_id, actual_board_id)
        self.assertEqual(expected_move, actual_move)

    def test_get_board13(self):
        actual_board, actual_board_id, actual_move = UBoard._UBoard__get_board(UBoard([]), 13)
        expected_board_id = 1
        expected_move = 4
        self.assertEqual(expected_board_id, actual_board_id)
        self.assertEqual(expected_move, actual_move)

    def test_get_board14(self):
        actual_board, actual_board_id, actual_move = UBoard._UBoard__get_board(UBoard([]), 14)
        expected_board_id = 1
        expected_move = 5
        self.assertEqual(expected_board_id, actual_board_id)
        self.assertEqual(expected_move, actual_move)

    def test_get_board15(self):
        actual_board, actual_board_id, actual_move = UBoard._UBoard__get_board(UBoard([]), 15)
        expected_board_id = 2
        expected_move = 3
        self.assertEqual(expected_board_id, actual_board_id)
        self.assertEqual(expected_move, actual_move)

    def test_get_board16(self):
        actual_board, actual_board_id, actual_move = UBoard._UBoard__get_board(UBoard([]), 16)
        expected_board_id = 2
        expected_move = 4
        self.assertEqual(expected_board_id, actual_board_id)
        self.assertEqual(expected_move, actual_move)

    def test_get_board17(self):
        actual_board, actual_board_id, actual_move = UBoard._UBoard__get_board(UBoard([]), 17)
        expected_board_id = 2
        expected_move = 5
        self.assertEqual(expected_board_id, actual_board_id)
        self.assertEqual(expected_move, actual_move)

    def test_get_board18(self):
        actual_board, actual_board_id, actual_move = UBoard._UBoard__get_board(UBoard([]), 18)
        expected_board_id = 0
        expected_move = 6
        self.assertEqual(expected_board_id, actual_board_id)
        self.assertEqual(expected_move, actual_move)

    def test_get_board19(self):
        actual_board, actual_board_id, actual_move = UBoard._UBoard__get_board(UBoard([]), 19)
        expected_board_id = 0
        expected_move = 7
        self.assertEqual(expected_board_id, actual_board_id)
        self.assertEqual(expected_move, actual_move)

    def test_get_board20(self):
        actual_board, actual_board_id, actual_move = UBoard._UBoard__get_board(UBoard([]), 20)
        expected_board_id = 0
        expected_move = 8
        self.assertEqual(expected_board_id, actual_board_id)
        self.assertEqual(expected_move, actual_move)

    def test_get_board21(self):
        actual_board, actual_board_id, actual_move = UBoard._UBoard__get_board(UBoard([]), 21)
        expected_board_id = 1
        expected_move = 6
        self.assertEqual(expected_board_id, actual_board_id)
        self.assertEqual(expected_move, actual_move)

    def test_get_board22(self):
        actual_board, actual_board_id, actual_move = UBoard._UBoard__get_board(UBoard([]), 22)
        expected_board_id = 1
        expected_move = 7
        self.assertEqual(expected_board_id, actual_board_id)
        self.assertEqual(expected_move, actual_move)

    def test_get_board23(self):
        actual_board, actual_board_id, actual_move = UBoard._UBoard__get_board(UBoard([]), 23)
        expected_board_id = 1
        expected_move = 8
        self.assertEqual(expected_board_id, actual_board_id)
        self.assertEqual(expected_move, actual_move)

    def test_get_board24(self):
        actual_board, actual_board_id, actual_move = UBoard._UBoard__get_board(UBoard([]), 24)
        expected_board_id = 2
        expected_move = 6
        self.assertEqual(expected_board_id, actual_board_id)
        self.assertEqual(expected_move, actual_move)

    def test_get_board25(self):
        actual_board, actual_board_id, actual_move = UBoard._UBoard__get_board(UBoard([]), 25)
        expected_board_id = 2
        expected_move = 7
        self.assertEqual(expected_board_id, actual_board_id)
        self.assertEqual(expected_move, actual_move)

    def test_get_board26(self):
        actual_board, actual_board_id, actual_move = UBoard._UBoard__get_board(UBoard([]), 26)
        expected_board_id = 2
        expected_move = 8
        self.assertEqual(expected_board_id, actual_board_id)
        self.assertEqual(expected_move, actual_move)

    def test_get_board27(self):
        actual_board, actual_board_id, actual_move = UBoard._UBoard__get_board(UBoard([]), 27)
        expected_board_id = 3
        expected_move = 0
        self.assertEqual(expected_board_id, actual_board_id)
        self.assertEqual(expected_move, actual_move)

    def test_get_board28(self):
        actual_board, actual_board_id, actual_move = UBoard._UBoard__get_board(UBoard([]), 28)
        expected_board_id = 3
        expected_move = 1
        self.assertEqual(expected_board_id, actual_board_id)
        self.assertEqual(expected_move, actual_move)

    def test_get_board29(self):
        actual_board, actual_board_id, actual_move = UBoard._UBoard__get_board(UBoard([]), 29)
        expected_board_id = 3
        expected_move = 2
        self.assertEqual(expected_board_id, actual_board_id)
        self.assertEqual(expected_move, actual_move)

    def test_get_board30(self):
        actual_board, actual_board_id, actual_move = UBoard._UBoard__get_board(UBoard([]), 30)
        expected_board_id = 4
        expected_move = 0
        self.assertEqual(expected_board_id, actual_board_id)
        self.assertEqual(expected_move, actual_move)

    def test_get_board31(self):
        actual_board, actual_board_id, actual_move = UBoard._UBoard__get_board(UBoard([]), 31)
        expected_board_id = 4
        expected_move = 1
        self.assertEqual(expected_board_id, actual_board_id)
        self.assertEqual(expected_move, actual_move)

    def test_get_board32(self):
        actual_board, actual_board_id, actual_move = UBoard._UBoard__get_board(UBoard([]), 32)
        expected_board_id = 4
        expected_move = 2
        self.assertEqual(expected_board_id, actual_board_id)
        self.assertEqual(expected_move, actual_move)

    def test_get_board33(self):
        actual_board, actual_board_id, actual_move = UBoard._UBoard__get_board(UBoard([]), 33)
        expected_board_id = 5
        expected_move = 0
        self.assertEqual(expected_board_id, actual_board_id)
        self.assertEqual(expected_move, actual_move)

    def test_get_board34(self):
        actual_board, actual_board_id, actual_move = UBoard._UBoard__get_board(UBoard([]), 34)
        expected_board_id = 5
        expected_move = 1
        self.assertEqual(expected_board_id, actual_board_id)
        self.assertEqual(expected_move, actual_move)

    def test_get_board35(self):
        actual_board, actual_board_id, actual_move = UBoard._UBoard__get_board(UBoard([]), 35)
        expected_board_id = 5
        expected_move = 2
        self.assertEqual(expected_board_id, actual_board_id)
        self.assertEqual(expected_move, actual_move)

    def test_get_board36(self):
        actual_board, actual_board_id, actual_move = UBoard._UBoard__get_board(UBoard([]), 36)
        expected_board_id = 3
        expected_move = 3
        self.assertEqual(expected_board_id, actual_board_id)
        self.assertEqual(expected_move, actual_move)

    def test_get_board37(self):
        actual_board, actual_board_id, actual_move = UBoard._UBoard__get_board(UBoard([]), 37)
        expected_board_id = 3
        expected_move = 4
        self.assertEqual(expected_board_id, actual_board_id)
        self.assertEqual(expected_move, actual_move)

    def test_get_board38(self):
        actual_board, actual_board_id, actual_move = UBoard._UBoard__get_board(UBoard([]), 38)
        expected_board_id = 3
        expected_move = 5
        self.assertEqual(expected_board_id, actual_board_id)
        self.assertEqual(expected_move, actual_move)

    def test_get_board39(self):
        actual_board, actual_board_id, actual_move = UBoard._UBoard__get_board(UBoard([]), 39)
        expected_board_id = 4
        expected_move = 3
        self.assertEqual(expected_board_id, actual_board_id)
        self.assertEqual(expected_move, actual_move)

    def test_get_board40(self):
        actual_board, actual_board_id, actual_move = UBoard._UBoard__get_board(UBoard([]), 40)
        expected_board_id = 4
        expected_move = 4
        self.assertEqual(expected_board_id, actual_board_id)
        self.assertEqual(expected_move, actual_move)

    def test_get_board41(self):
        actual_board, actual_board_id, actual_move = UBoard._UBoard__get_board(UBoard([]), 41)
        expected_board_id = 4
        expected_move = 5
        self.assertEqual(expected_board_id, actual_board_id)
        self.assertEqual(expected_move, actual_move)

    def test_get_board42(self):
        actual_board, actual_board_id, actual_move = UBoard._UBoard__get_board(UBoard([]), 42)
        expected_board_id = 5
        expected_move = 3
        self.assertEqual(expected_board_id, actual_board_id)
        self.assertEqual(expected_move, actual_move)

    def test_get_board43(self):
        actual_board, actual_board_id, actual_move = UBoard._UBoard__get_board(UBoard([]), 43)
        expected_board_id = 5
        expected_move = 4
        self.assertEqual(expected_board_id, actual_board_id)
        self.assertEqual(expected_move, actual_move)

    def test_get_board44(self):
        actual_board, actual_board_id, actual_move = UBoard._UBoard__get_board(UBoard([]), 44)
        expected_board_id = 5
        expected_move = 5
        self.assertEqual(expected_board_id, actual_board_id)
        self.assertEqual(expected_move, actual_move)

    def test_get_board45(self):
        actual_board, actual_board_id, actual_move = UBoard._UBoard__get_board(UBoard([]), 45)
        expected_board_id = 3
        expected_move = 6
        self.assertEqual(expected_board_id, actual_board_id)
        self.assertEqual(expected_move, actual_move)

    def test_get_board46(self):
        actual_board, actual_board_id, actual_move = UBoard._UBoard__get_board(UBoard([]), 46)
        expected_board_id = 3
        expected_move = 7
        self.assertEqual(expected_board_id, actual_board_id)
        self.assertEqual(expected_move, actual_move)

    def test_get_board47(self):
        actual_board, actual_board_id, actual_move = UBoard._UBoard__get_board(UBoard([]), 47)
        expected_board_id = 3
        expected_move = 8
        self.assertEqual(expected_board_id, actual_board_id)
        self.assertEqual(expected_move, actual_move)

    def test_get_board48(self):
        actual_board, actual_board_id, actual_move = UBoard._UBoard__get_board(UBoard([]), 48)
        expected_board_id = 4
        expected_move = 6
        self.assertEqual(expected_board_id, actual_board_id)
        self.assertEqual(expected_move, actual_move)

    def test_get_board49(self):
        actual_board, actual_board_id, actual_move = UBoard._UBoard__get_board(UBoard([]), 49)
        expected_board_id = 4
        expected_move = 7
        self.assertEqual(expected_board_id, actual_board_id)
        self.assertEqual(expected_move, actual_move)

    def test_get_board50(self):
        actual_board, actual_board_id, actual_move = UBoard._UBoard__get_board(UBoard([]), 50)
        expected_board_id = 4
        expected_move = 8
        self.assertEqual(expected_board_id, actual_board_id)
        self.assertEqual(expected_move, actual_move)

    def test_get_board51(self):
        actual_board, actual_board_id, actual_move = UBoard._UBoard__get_board(UBoard([]), 51)
        expected_board_id = 5
        expected_move = 6
        self.assertEqual(expected_board_id, actual_board_id)
        self.assertEqual(expected_move, actual_move)

    def test_get_board52(self):
        actual_board, actual_board_id, actual_move = UBoard._UBoard__get_board(UBoard([]), 52)
        expected_board_id = 5
        expected_move = 7
        self.assertEqual(expected_board_id, actual_board_id)
        self.assertEqual(expected_move, actual_move)

    def test_get_board53(self):
        actual_board, actual_board_id, actual_move = UBoard._UBoard__get_board(UBoard([]), 53)
        expected_board_id = 5
        expected_move = 8
        self.assertEqual(expected_board_id, actual_board_id)
        self.assertEqual(expected_move, actual_move)

    def test_get_board54(self):
        actual_board, actual_board_id, actual_move = UBoard._UBoard__get_board(UBoard([]), 54)
        expected_board_id = 6
        expected_move = 0
        self.assertEqual(expected_board_id, actual_board_id)
        self.assertEqual(expected_move, actual_move)

    def test_get_board55(self):
        actual_board, actual_board_id, actual_move = UBoard._UBoard__get_board(UBoard([]), 55)
        expected_board_id = 6
        expected_move = 1
        self.assertEqual(expected_board_id, actual_board_id)
        self.assertEqual(expected_move, actual_move)

    def test_get_board56(self):
        actual_board, actual_board_id, actual_move = UBoard._UBoard__get_board(UBoard([]), 56)
        expected_board_id = 6
        expected_move = 2
        self.assertEqual(expected_board_id, actual_board_id)
        self.assertEqual(expected_move, actual_move)

    def test_get_board57(self):
        actual_board, actual_board_id, actual_move = UBoard._UBoard__get_board(UBoard([]), 57)
        expected_board_id = 7
        expected_move = 0
        self.assertEqual(expected_board_id, actual_board_id)
        self.assertEqual(expected_move, actual_move)

    def test_get_board58(self):
        actual_board, actual_board_id, actual_move = UBoard._UBoard__get_board(UBoard([]), 58)
        expected_board_id = 7
        expected_move = 1
        self.assertEqual(expected_board_id, actual_board_id)
        self.assertEqual(expected_move, actual_move)

    def test_get_board59(self):
        actual_board, actual_board_id, actual_move = UBoard._UBoard__get_board(UBoard([]), 59)
        expected_board_id = 7
        expected_move = 2
        self.assertEqual(expected_board_id, actual_board_id)
        self.assertEqual(expected_move, actual_move)

    def test_get_board60(self):
        actual_board, actual_board_id, actual_move = UBoard._UBoard__get_board(UBoard([]), 60)
        expected_board_id = 8
        expected_move = 0
        self.assertEqual(expected_board_id, actual_board_id)
        self.assertEqual(expected_move, actual_move)

    def test_get_board61(self):
        actual_board, actual_board_id, actual_move = UBoard._UBoard__get_board(UBoard([]), 61)
        expected_board_id = 8
        expected_move = 1
        self.assertEqual(expected_board_id, actual_board_id)
        self.assertEqual(expected_move, actual_move)

    def test_get_board62(self):
        actual_board, actual_board_id, actual_move = UBoard._UBoard__get_board(UBoard([]), 62)
        expected_board_id = 8
        expected_move = 2
        self.assertEqual(expected_board_id, actual_board_id)
        self.assertEqual(expected_move, actual_move)

    def test_get_board63(self):
        actual_board, actual_board_id, actual_move = UBoard._UBoard__get_board(UBoard([]), 63)
        expected_board_id = 6
        expected_move = 3
        self.assertEqual(expected_board_id, actual_board_id)
        self.assertEqual(expected_move, actual_move)

    def test_get_board64(self):
        actual_board, actual_board_id, actual_move = UBoard._UBoard__get_board(UBoard([]), 64)
        expected_board_id = 6
        expected_move = 4
        self.assertEqual(expected_board_id, actual_board_id)
        self.assertEqual(expected_move, actual_move)

    def test_get_board65(self):
        actual_board, actual_board_id, actual_move = UBoard._UBoard__get_board(UBoard([]), 65)
        expected_board_id = 6
        expected_move = 5
        self.assertEqual(expected_board_id, actual_board_id)
        self.assertEqual(expected_move, actual_move)

    def test_get_board66(self):
        actual_board, actual_board_id, actual_move = UBoard._UBoard__get_board(UBoard([]), 66)
        expected_board_id = 7
        expected_move = 3
        self.assertEqual(expected_board_id, actual_board_id)
        self.assertEqual(expected_move, actual_move)

    def test_get_board67(self):
        actual_board, actual_board_id, actual_move = UBoard._UBoard__get_board(UBoard([]), 67)
        expected_board_id = 7
        expected_move = 4
        self.assertEqual(expected_board_id, actual_board_id)
        self.assertEqual(expected_move, actual_move)

    def test_get_board68(self):
        actual_board, actual_board_id, actual_move = UBoard._UBoard__get_board(UBoard([]), 68)
        expected_board_id = 7
        expected_move = 5
        self.assertEqual(expected_board_id, actual_board_id)
        self.assertEqual(expected_move, actual_move)

    def test_get_board69(self):
        actual_board, actual_board_id, actual_move = UBoard._UBoard__get_board(UBoard([]), 69)
        expected_board_id = 8
        expected_move = 3
        self.assertEqual(expected_board_id, actual_board_id)
        self.assertEqual(expected_move, actual_move)

    def test_get_board70(self):
        actual_board, actual_board_id, actual_move = UBoard._UBoard__get_board(UBoard([]), 70)
        expected_board_id = 8
        expected_move = 4
        self.assertEqual(expected_board_id, actual_board_id)
        self.assertEqual(expected_move, actual_move)

    def test_get_board71(self):
        actual_board, actual_board_id, actual_move = UBoard._UBoard__get_board(UBoard([]), 71)
        expected_board_id = 8
        expected_move = 5
        self.assertEqual(expected_board_id, actual_board_id)
        self.assertEqual(expected_move, actual_move)

    def test_get_board72(self):
        actual_board, actual_board_id, actual_move = UBoard._UBoard__get_board(UBoard([]), 72)
        expected_board_id = 6
        expected_move = 6
        self.assertEqual(expected_board_id, actual_board_id)
        self.assertEqual(expected_move, actual_move)

    def test_get_board73(self):
        actual_board, actual_board_id, actual_move = UBoard._UBoard__get_board(UBoard([]), 73)
        expected_board_id = 6
        expected_move = 7
        self.assertEqual(expected_board_id, actual_board_id)
        self.assertEqual(expected_move, actual_move)

    def test_get_board74(self):
        actual_board, actual_board_id, actual_move = UBoard._UBoard__get_board(UBoard([]), 74)
        expected_board_id = 6
        expected_move = 8
        self.assertEqual(expected_board_id, actual_board_id)
        self.assertEqual(expected_move, actual_move)

    def test_get_board75(self):
        actual_board, actual_board_id, actual_move = UBoard._UBoard__get_board(UBoard([]), 75)
        expected_board_id = 7
        expected_move = 6
        self.assertEqual(expected_board_id, actual_board_id)
        self.assertEqual(expected_move, actual_move)

    def test_get_board76(self):
        actual_board, actual_board_id, actual_move = UBoard._UBoard__get_board(UBoard([]), 76)
        expected_board_id = 7
        expected_move = 7
        self.assertEqual(expected_board_id, actual_board_id)
        self.assertEqual(expected_move, actual_move)

    def test_get_board77(self):
        actual_board, actual_board_id, actual_move = UBoard._UBoard__get_board(UBoard([]), 77)
        expected_board_id = 7
        expected_move = 8
        self.assertEqual(expected_board_id, actual_board_id)
        self.assertEqual(expected_move, actual_move)

    def test_get_board78(self):
        actual_board, actual_board_id, actual_move = UBoard._UBoard__get_board(UBoard([]), 78)
        expected_board_id = 8
        expected_move = 6
        self.assertEqual(expected_board_id, actual_board_id)
        self.assertEqual(expected_move, actual_move)

    def test_get_board79(self):
        actual_board, actual_board_id, actual_move = UBoard._UBoard__get_board(UBoard([]), 79)
        expected_board_id = 8
        expected_move = 7
        self.assertEqual(expected_board_id, actual_board_id)
        self.assertEqual(expected_move, actual_move)

    def test_get_board80(self):
        actual_board, actual_board_id, actual_move = UBoard._UBoard__get_board(UBoard([]), 80)
        expected_board_id = 8
        expected_move = 8
        self.assertEqual(expected_board_id, actual_board_id)
        self.assertEqual(expected_move, actual_move)

    def test_get_binary_board0(self):
        self.maxDiff = None
        uboard = UBoard([])

        uboard.insert_x(1)
        actual_b_uboard_x = uboard.get_binary_board('X')
        expected_b_uboard_x = [[[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]],
                               [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]],
                               [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]],
                               [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]],
                               [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]],
                               [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]],
                               [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]],
                               [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]],
                               [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [1, 0]]]
        self.assertEqual(expected_b_uboard_x, actual_b_uboard_x)
        actual_b_uboard_o = uboard.get_binary_board('O')
        expected_b_uboard_o = [[[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]],
                               [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]],
                               [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]],
                               [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]],
                               [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]],
                               [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]],
                               [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]],
                               [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]],
                               [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 1]]]
        self.assertEqual(expected_b_uboard_o, actual_b_uboard_o)

        uboard.insert_o(21)
        actual_b_uboard_x = uboard.get_binary_board('X')
        expected_b_uboard_x = [[[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]],
                               [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]],
                               [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]],
                               [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]],
                               [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]],
                               [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]],
                               [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 1], [0, 0], [0, 0]],
                               [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]],
                               [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [1, 0]]]
        self.assertEqual(expected_b_uboard_x, actual_b_uboard_x)
        actual_b_uboard_o = uboard.get_binary_board('O')
        expected_b_uboard_o = [[[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]],
                               [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]],
                               [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]],
                               [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]],
                               [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]],
                               [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]],
                               [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [1, 0], [0, 0], [0, 0]],
                               [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]],
                               [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 1]]]
        self.assertEqual(expected_b_uboard_o, actual_b_uboard_o)

        uboard.insert_x(80)
        actual_b_uboard_x = uboard.get_binary_board('X')
        expected_b_uboard_x = [[[0, 0], [1, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]],
                               [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]],
                               [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]],
                               [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]],
                               [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]],
                               [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]],
                               [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 1], [0, 0], [0, 0]],
                               [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]],
                               [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [1, 0]]]
        self.assertEqual(expected_b_uboard_x, actual_b_uboard_x)
        actual_b_uboard_o = uboard.get_binary_board('O')
        expected_b_uboard_o = [[[0, 0], [0, 1], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]],
                               [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]],
                               [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]],
                               [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]],
                               [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]],
                               [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]],
                               [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [1, 0], [0, 0], [0, 0]],
                               [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]],
                               [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 1]]]
        self.assertEqual(expected_b_uboard_o, actual_b_uboard_o)

        uboard.insert_o(68)
        actual_b_uboard_x = uboard.get_binary_board('X')
        expected_b_uboard_x = [[[0, 0], [1, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]],
                               [[0, 0], [0, 0], [0, 0], [0, 0], [0, 1], [0, 0], [0, 0], [0, 0], [0, 0]],
                               [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]],
                               [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]],
                               [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]],
                               [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]],
                               [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 1], [0, 0], [0, 0]],
                               [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]],
                               [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [1, 0]]]
        self.assertEqual(expected_b_uboard_x, actual_b_uboard_x)
        actual_b_uboard_o = uboard.get_binary_board('O')
        expected_b_uboard_o = [[[0, 0], [0, 1], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]],
                               [[0, 0], [0, 0], [0, 0], [0, 0], [1, 0], [0, 0], [0, 0], [0, 0], [0, 0]],
                               [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]],
                               [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]],
                               [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]],
                               [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]],
                               [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [1, 0], [0, 0], [0, 0]],
                               [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]],
                               [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 1]]]
        self.assertEqual(expected_b_uboard_o, actual_b_uboard_o)

        uboard.insert_x(49)
        actual_b_uboard_x = uboard.get_binary_board('X')
        expected_b_uboard_x = [[[0, 0], [1, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]],
                               [[0, 0], [0, 0], [0, 0], [0, 0], [0, 1], [0, 0], [0, 0], [0, 0], [0, 0]],
                               [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]],
                               [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [1, 0], [0, 0], [0, 0], [0, 0]],
                               [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]],
                               [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]],
                               [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 1], [0, 0], [0, 0]],
                               [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]],
                               [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [1, 0]]]
        self.assertEqual(expected_b_uboard_x, actual_b_uboard_x)
        actual_b_uboard_o = uboard.get_binary_board('O')
        expected_b_uboard_o = [[[0, 0], [0, 1], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]],
                               [[0, 0], [0, 0], [0, 0], [0, 0], [1, 0], [0, 0], [0, 0], [0, 0], [0, 0]],
                               [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]],
                               [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 1], [0, 0], [0, 0], [0, 0]],
                               [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]],
                               [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]],
                               [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [1, 0], [0, 0], [0, 0]],
                               [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]],
                               [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 1]]]
        self.assertEqual(expected_b_uboard_o, actual_b_uboard_o)

        uboard.insert_o(57)
        actual_b_uboard_x = uboard.get_binary_board('X')
        expected_b_uboard_x = [[[0, 0], [1, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]],
                               [[0, 0], [0, 0], [0, 0], [0, 0], [0, 1], [0, 0], [0, 0], [0, 0], [0, 0]],
                               [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 1], [0, 0], [0, 0]],
                               [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [1, 0], [0, 0], [0, 0], [0, 0]],
                               [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]],
                               [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]],
                               [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 1], [0, 0], [0, 0]],
                               [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]],
                               [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [1, 0]]]
        self.assertEqual(expected_b_uboard_x, actual_b_uboard_x)
        actual_b_uboard_o = uboard.get_binary_board('O')
        expected_b_uboard_o = [[[0, 0], [0, 1], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]],
                               [[0, 0], [0, 0], [0, 0], [0, 0], [1, 0], [0, 0], [0, 0], [0, 0], [0, 0]],
                               [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [1, 0], [0, 0], [0, 0]],
                               [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 1], [0, 0], [0, 0], [0, 0]],
                               [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]],
                               [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]],
                               [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [1, 0], [0, 0], [0, 0]],
                               [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]],
                               [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 1]]]
        self.assertEqual(expected_b_uboard_o, actual_b_uboard_o)

        uboard.insert_x(16)
        actual_b_uboard_x = uboard.get_binary_board('X')
        expected_b_uboard_x = [[[0, 0], [1, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]],
                               [[0, 0], [0, 0], [0, 0], [0, 0], [0, 1], [0, 0], [0, 0], [0, 0], [0, 0]],
                               [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 1], [0, 0], [0, 0]],
                               [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [1, 0], [0, 0], [0, 0], [0, 0]],
                               [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]],
                               [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]],
                               [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 1], [0, 0], [0, 0]],
                               [[0, 0], [0, 0], [1, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]],
                               [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [1, 0]]]
        self.assertEqual(expected_b_uboard_x, actual_b_uboard_x)
        actual_b_uboard_o = uboard.get_binary_board('O')
        expected_b_uboard_o = [[[0, 0], [0, 1], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]],
                               [[0, 0], [0, 0], [0, 0], [0, 0], [1, 0], [0, 0], [0, 0], [0, 0], [0, 0]],
                               [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [1, 0], [0, 0], [0, 0]],
                               [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 1], [0, 0], [0, 0], [0, 0]],
                               [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]],
                               [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]],
                               [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [1, 0], [0, 0], [0, 0]],
                               [[0, 0], [0, 0], [0, 1], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]],
                               [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 1]]]
        self.assertEqual(expected_b_uboard_o, actual_b_uboard_o)

        uboard.insert_o(39)
        actual_b_uboard_x = uboard.get_binary_board('X')
        expected_b_uboard_x = [[[0, 0], [1, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]],
                               [[0, 0], [0, 0], [0, 0], [0, 0], [0, 1], [0, 0], [0, 0], [0, 0], [0, 0]],
                               [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 1], [0, 0], [0, 0]],
                               [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [1, 0], [0, 0], [0, 0], [0, 0]],
                               [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 1], [0, 0], [0, 0]],
                               [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]],
                               [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 1], [0, 0], [0, 0]],
                               [[0, 0], [0, 0], [1, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]],
                               [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [1, 0]]]
        self.assertEqual(expected_b_uboard_x, actual_b_uboard_x)
        actual_b_uboard_o = uboard.get_binary_board('O')
        expected_b_uboard_o = [[[0, 0], [0, 1], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]],
                               [[0, 0], [0, 0], [0, 0], [0, 0], [1, 0], [0, 0], [0, 0], [0, 0], [0, 0]],
                               [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [1, 0], [0, 0], [0, 0]],
                               [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 1], [0, 0], [0, 0], [0, 0]],
                               [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [1, 0], [0, 0], [0, 0]],
                               [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]],
                               [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [1, 0], [0, 0], [0, 0]],
                               [[0, 0], [0, 0], [0, 1], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]],
                               [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 1]]]
        self.assertEqual(expected_b_uboard_o, actual_b_uboard_o)

        uboard.insert_x(35)
        actual_b_uboard_x = uboard.get_binary_board('X')
        expected_b_uboard_x = [[[0, 0], [1, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]],
                               [[0, 0], [0, 0], [0, 0], [0, 0], [0, 1], [0, 0], [0, 0], [0, 0], [0, 0]],
                               [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 1], [0, 0], [0, 0]],
                               [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [1, 0], [0, 0], [0, 0], [0, 0]],
                               [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 1], [0, 0], [0, 0]],
                               [[0, 0], [1, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]],
                               [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 1], [0, 0], [0, 0]],
                               [[0, 0], [0, 0], [1, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]],
                               [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [1, 0]]]
        self.assertEqual(expected_b_uboard_x, actual_b_uboard_x)
        actual_b_uboard_o = uboard.get_binary_board('O')
        expected_b_uboard_o = [[[0, 0], [0, 1], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]],
                               [[0, 0], [0, 0], [0, 0], [0, 0], [1, 0], [0, 0], [0, 0], [0, 0], [0, 0]],
                               [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [1, 0], [0, 0], [0, 0]],
                               [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 1], [0, 0], [0, 0], [0, 0]],
                               [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [1, 0], [0, 0], [0, 0]],
                               [[0, 0], [0, 1], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]],
                               [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [1, 0], [0, 0], [0, 0]],
                               [[0, 0], [0, 0], [0, 1], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]],
                               [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 1]]]
        self.assertEqual(expected_b_uboard_o, actual_b_uboard_o)

        uboard.insert_o(4)
        actual_b_uboard_x = uboard.get_binary_board('X')
        expected_b_uboard_x = [[[0, 0], [1, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]],
                               [[0, 0], [0, 0], [0, 0], [0, 0], [0, 1], [0, 0], [0, 0], [0, 0], [0, 0]],
                               [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 1], [0, 0], [0, 0]],
                               [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [1, 0], [0, 0], [0, 0], [0, 0]],
                               [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 1], [0, 0], [0, 0]],
                               [[0, 0], [1, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]],
                               [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 1], [0, 0], [0, 0]],
                               [[0, 0], [0, 0], [1, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]],
                               [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 1], [0, 0], [0, 0], [1, 0]]]
        self.assertEqual(expected_b_uboard_x, actual_b_uboard_x)
        actual_b_uboard_o = uboard.get_binary_board('O')
        expected_b_uboard_o = [[[0, 0], [0, 1], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]],
                               [[0, 0], [0, 0], [0, 0], [0, 0], [1, 0], [0, 0], [0, 0], [0, 0], [0, 0]],
                               [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [1, 0], [0, 0], [0, 0]],
                               [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 1], [0, 0], [0, 0], [0, 0]],
                               [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [1, 0], [0, 0], [0, 0]],
                               [[0, 0], [0, 1], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]],
                               [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [1, 0], [0, 0], [0, 0]],
                               [[0, 0], [0, 0], [0, 1], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]],
                               [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [1, 0], [0, 0], [0, 0], [0, 1]]]
        self.assertEqual(expected_b_uboard_o, actual_b_uboard_o)

    def test_is_valid_move0(self):
        uboard = UBoard([])
        for i in range(81):
            board, board_id, move = UBoard._UBoard__get_board(uboard, i)
            is_valid_move = UBoard._UBoard__is_valid_move(board, move)
            self.assertTrue(is_valid_move, msg=str(i))

        uboard.insert_x(1)
        for i in range(81):
            board, board_id, move = UBoard._UBoard__get_board(uboard, i)
            is_valid_move = UBoard._UBoard__is_valid_move(board, move)
            if i not in [1, 2, 9, 10, 11, 18, 19, 20]:
                self.assertFalse(is_valid_move, msg=str(i))
            else:
                self.assertTrue(is_valid_move, msg=str(i))



if __name__ == '__main__':
    unittest.main()
