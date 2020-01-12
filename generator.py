sample = """
    def test_get_uboard_square{}(self):
        actual_output = UBoard._UBoard__get_uboard_square({}, {})
        expected_output = 
        self.assertEqual(expected_output, actual_output)
"""

for i in range(0, 9):
    for j in range(0, 9):
        print(sample.format(i*9 + j, i, j))
        print()




# sample_x = [[[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]],
#                                [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]],
#                                [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]],
#                                [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]],
#                                [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]],
#                                [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]],
#                                [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]],
#                                [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]],
#                                [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]]
# sample_o = [[[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]],
#                                [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]],
#                                [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]],
#                                [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]],
#                                [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]],
#                                [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]],
#                                [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]],
#                                [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]],
#                                [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]]
#
#
# def fill_value(sample, index, subindex):
#     sample[8 - index//9][8-index%9][subindex] = 1
#     return sample
#
#
# outstring = "   "
# for i in range(80, -1, -1):
#     if i % 9 == 0:
#         if i > 9:
#             outstring += "  "
#         else:
#             outstring += "  "
#     if i > 9:
#         outstring += " {}     ".format(i)
#     else:
#         outstring += " {}      ".format(i)
#
#
# count = 0
# for i in [0, 20, 79, 67, 48, 56, 15, 38, 34, 3]:
#     if count % 2 == 0:
#         print(i, 'x')
#         sample_x = fill_value(sample_x, i, 0)
#         print(outstring)
#         print(sample_x)
#
#         print(i, 'o')
#         sample_o = fill_value(sample_o, i, 1)
#         print(outstring)
#         print(sample_o)
#     else:
#         print(i, 'x')
#         sample_x = fill_value(sample_x, i, 1)
#         print(outstring)
#         print(sample_x)
#
#         print(i, 'o')
#         sample_o = fill_value(sample_o, i, 0)
#         print(outstring)
#         print(sample_o)
#     count += 1
