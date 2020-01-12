sample = """
    def test_get_board{}(self):
        actual_board, actual_board_id, actual_move = UBoard._UBoard__get_board({})
        expected_board_id = 
        expected_move = 
        self.assertEqual(expected_board_id, actual_board_id)
        self.assertEqual(expected_move, actual_move)
"""

# for i in range(1, 81):
#     print(sample.format(i, i))
#     print()
#
#
#

sample_x = [[[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]],
                               [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]],
                               [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]],
                               [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]],
                               [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]],
                               [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]],
                               [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]],
                               [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]],
                               [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]]
sample_o = [[[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]],
                               [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]],
                               [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]],
                               [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]],
                               [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]],
                               [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]],
                               [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]],
                               [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]],
                               [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]]


def fill_value(sample, index, subindex):
    sample[8 - index//9][8-index%9][subindex] = 1
    return sample


outstring = "   "
for i in range(80, -1, -1):
    if i % 9 == 0:
        if i > 9:
            outstring += "  "
        else:
            outstring += "  "
    if i > 9:
        outstring += " {}     ".format(i)
    else:
        outstring += " {}      ".format(i)


count = 0
for i in [0, 20, 79, 67, 48, 56, 15, 38, 34, 3]:
    if count % 2 == 0:
        print(i, 'x')
        sample_x = fill_value(sample_x, i, 0)
        print(outstring)
        print(sample_x)

        print(i, 'o')
        sample_o = fill_value(sample_o, i, 1)
        print(outstring)
        print(sample_o)
    else:
        print(i, 'x')
        sample_x = fill_value(sample_x, i, 1)
        print(outstring)
        print(sample_x)

        print(i, 'o')
        sample_o = fill_value(sample_o, i, 0)
        print(outstring)
        print(sample_o)
    count += 1
