from unittest import TestCase

from finding_a_shared_motif import find_possible_motifs


class TestScan(TestCase):

    def test_find_possible_values(self):
        example_sequence = 'ATCG'
        expected_motifs = set(['A', 'AT', 'ATC', 'ATCG', 'T', 'TC', 'TCG', 'C', 'CG', 'G'])
        possible_motifs = find_possible_motifs(example_sequence)
        print(possible_motifs)
        self.assertSetEqual(possible_motifs, expected_motifs)