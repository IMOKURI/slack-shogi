import unittest
from app.modules.shogi import Shogi, Koma

class ShogiTest(unittest.TestCase):
    def setUp(self):
        pass

    def test_move_76fu(self):
        shogi = Shogi()
        shogi.move(2, 6, 2, 5, False)
        self.assertEqual(shogi.board[5][2], Koma.fu)
        self.assertEqual(shogi.board[6][2], Koma.empty)

    def test_movable_for_empty(self):
        shogi = Shogi()
        movable = shogi.movable(5, 5, 5, 6, False)
        self.assertFalse(movable)

    def test_movable_for_enemy(self):
        shogi = Shogi()
        movable = shogi.movable(0, 0, 0, 1, False)
        self.assertFalse(movable)
        movable = shogi.movable(0, 1, 0, 2, False)
        self.assertFalse(movable)
        shogi.move(2, 6, 2, 5, False)
        movable = shogi.movable(0, 0, 0, 1, False)
        self.assertTrue(movable)

    def test_movable_for_kyo(self):
        shogi = Shogi()
        shogi.move(8, 6, 0, 0, False)
        shogi.first = True
        movable = shogi.movable(8, 8, 8, 4, False)
        self.assertTrue(movable)
        movable = shogi.movable(8, 8, 8, 3, False)
        self.assertTrue(movable)
        movable = shogi.movable(8, 8, 8, 2, False)
        self.assertTrue(movable)
        movable = shogi.movable(8, 8, 8, 1, False)
        self.assertFalse(movable)

    def test_movable_for_fu(self):
        shogi = Shogi()
        movable = shogi.movable(0, 6, 0, 4, False)
        self.assertFalse(movable)
        movable = shogi.movable(0, 6, 0, 7, False)
        self.assertFalse(movable)
        movable = shogi.movable(0, 6, 1, 5, False)
        self.assertFalse(movable)
        movable = shogi.movable(0, 2, 0, 3, False)
        self.assertFalse(movable)

        # 96fu
        movable = shogi.movable(0, 6, 0, 5, False)
        self.assertTrue(movable)
        shogi.move(0, 6, 0, 5, False)

        # 94fu
        movable = shogi.movable(0, 2, 0, 3, False)
        self.assertTrue(movable)
        shogi.move(0, 2, 0, 3, False)

        # 95fu
        movable = shogi.movable(0, 5, 0, 4, False)
        self.assertTrue(movable)
        shogi.move(0, 5, 0, 4, False)

        # 95 do fu
        movable = shogi.movable(0, 3, 0, 4, False)
        self.assertTrue(movable)
        shogi.move(0, 3, 0, 4, False)

        # moving opponent koma
        movable = shogi.movable(0, 4, 0, 5, False)
        self.assertFalse(movable)

    def test_movable_for_kaku(self):
        shogi = Shogi()
        movable = shogi.movable(1, 7, 3, 5, False)
        self.assertFalse(movable)

        # 66 fu
        movable = shogi.movable(2, 6, 2, 5, False)
        self.assertTrue(movable)
        shogi.move(2, 6, 2, 5, False)

        # 34 fu
        movable = shogi.movable(6, 2, 6, 3, False)
        self.assertTrue(movable)
        shogi.move(6, 2, 6, 3, False)

        movable = shogi.movable(1, 7, 8, 0, False)
        self.assertFalse(movable)

        # 22 kaku
        movable = shogi.movable(1, 7, 7, 1, False)
        self.assertTrue(movable)
        shogi.move(6, 2, 6, 3, False)

    def test_move_for_promote(self):
        shogi = Shogi()
        shogi.board = [
                [Koma.empty, Koma.empty, Koma.empty, Koma.empty, Koma.empty, Koma.promoted_fu, Koma.hisha, Koma.empty, Koma.kin],
                [Koma.fu, Koma.kyosha, Koma.empty, Koma.empty, Koma.empty, Koma.empty, Koma.empty, Koma.empty, Koma.gyoku],
                [Koma.opponent_fu, Koma.empty, Koma.empty, Koma.empty, Koma.empty, Koma.empty, Koma.empty, Koma.empty, Koma.empty],
                [Koma.empty, Koma.empty, Koma.gin, Koma.empty, Koma.empty, Koma.empty, Koma.empty, Koma.empty, Koma.empty],
                [Koma.empty, Koma.kyosha, Koma.opponent_kyosha, Koma.empty, Koma.empty, Koma.empty, Koma.empty, Koma.empty, Koma.empty],
                [Koma.empty, Koma.empty, Koma.opponent_gin, Koma.empty, Koma.empty, Koma.empty, Koma.empty, Koma.empty, Koma.empty],
                [Koma.fu, Koma.empty, Koma.empty, Koma.empty, Koma.empty, Koma.empty, Koma.empty, Koma.empty, Koma.empty],
                [Koma.opponent_fu, Koma.opponent_kyosha, Koma.empty, Koma.empty, Koma.empty, Koma.empty, Koma.empty, Koma.empty, Koma.opponent_gyoku],
                [Koma.empty, Koma.empty, Koma.empty, Koma.empty, Koma.empty, Koma.opponent_promoted_fu, Koma.opponent_hisha, Koma.empty, Koma.opponent_kin],
        ]

        shogi.first = True
        # 91 fu narazu
        movable = shogi.movable(0, 1, 0, 0, False)
        self.assertFalse(movable)

        # 91 fu naru
        movable = shogi.movable(0, 1, 0, 0, True)
        self.assertTrue(movable)

        shogi.first = False
        # 99 fu narazu
        movable = shogi.movable(0, 7, 0, 8, False)
        self.assertFalse(movable)

        # 99 fu naru
        movable = shogi.movable(0, 7, 0, 8, True)
        self.assertTrue(movable)

        shogi.first = True
        # 81 kyo narazu
        movable = shogi.movable(1, 1, 1, 0, False)
        self.assertFalse(movable)

        # 81 kyo naru
        movable = shogi.movable(1, 1, 1, 0, True)
        self.assertTrue(movable)

        shogi.first = False
        # 89 kyo narazu
        movable = shogi.movable(1, 7, 1, 8, False)
        self.assertFalse(movable)

        # 89 kyo naru
        movable = shogi.movable(1, 7, 1, 8, True)
        self.assertTrue(movable)

        shogi.first = True
        # 96 fu naru
        movable = shogi.movable(0, 6, 0, 5, True)
        self.assertFalse(movable)

        # 96 fu narazu
        movable = shogi.movable(0, 6, 0, 5, False)
        self.assertTrue(movable)

        shogi.first = False
        # 94 fu naru
        movable = shogi.movable(0, 2, 0, 3, True)
        self.assertFalse(movable)

        # 94 fu narazu
        movable = shogi.movable(0, 2, 0, 3, False)
        self.assertTrue(movable)

        shogi.first = True
        # 73 gin naru and narazu
        movable = shogi.movable(2, 3, 2, 2, True)
        self.assertTrue(movable)

        movable = shogi.movable(2, 3, 2, 2, False)
        self.assertTrue(movable)

        shogi.first = False
        # 77 gin naru and narazu
        movable = shogi.movable(2, 5, 2, 6, True)
        self.assertTrue(movable)

        movable = shogi.movable(2, 5, 2, 6, False)
        self.assertTrue(movable)

        # kin and gyoku can't promote
        shogi.first = False
        movable = shogi.movable(8, 0, 8, 1, True)
        self.assertFalse(movable)
        movable = shogi.movable(7, 0, 7, 1, True)
        self.assertFalse(movable)
        shogi.first = True
        movable = shogi.movable(1, 0, 1, 1, True)
        self.assertFalse(movable)
        movable = shogi.movable(0, 0, 0, 1, True)
        self.assertFalse(movable)

        # back promoteTrue
        shogi.first = True
        movable = shogi.movable(6, 0, 6, 5, True)
        self.assertTrue(movable)
        movable = shogi.movable(6, 0, 6, 7, True)
        self.assertTrue(movable)

        shogi.first = False
        movable = shogi.movable(6, 8, 6, 5, True)
        self.assertTrue(movable)
        movable = shogi.movable(6, 8, 6, 1, True)
        self.assertTrue(movable)

        # promoted' koma try to promote
        shogi.first = True
        movable = shogi.movable(5, 0, 5, 1, True)
        self.assertFalse(movable)
        shogi.first = False
        movable = shogi.movable(5, 8, 5, 7, True)
        self.assertFalse(movable)


    def test_find_koma(self):
        shogi = Shogi()
        koma_positions = shogi.find_koma(Koma.kin)
        self.assertIn([3, 8], koma_positions)
        self.assertIn([5, 8], koma_positions)

        koma_positions = shogi.find_koma(Koma.opponent_kin)
        self.assertIn([3, 0], koma_positions)
        self.assertIn([5, 0], koma_positions)

        koma_positions = shogi.find_koma(Koma.hisha)
        self.assertIn([7, 7], koma_positions)

