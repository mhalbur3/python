import unittest
from television import Television

class TestTelevision(unittest.TestCase):

    def test_initial_state(self):
        tv = Television()
        self.assertEqual(str(tv), "Power = False, Channel = 0, Volume = 0")

    def test_power_toggle(self):
        tv = Television()
        tv.power()
        self.assertTrue(tv._status)
        tv.power()
        self.assertFalse(tv._status)

    def test_channel_up_wrap(self):
        tv = Television()
        tv.power()
        for _ in range(5):  # 0 → 1 → 2 → 3 → 0 → 1
            tv.channel_up()
        self.assertEqual(tv._channel, 1)

    def test_channel_down_wrap(self):
        tv = Television()
        tv.power()
        tv.channel_down()  # from 0 to 3
        self.assertEqual(tv._channel, 3)

    def test_volume_up_down_bounds(self):
        tv = Television()
        tv.power()
        for _ in range(5):
            tv.volume_up()
        self.assertEqual(tv._volume, 2)

        for _ in range(5):
            tv.volume_down()
        self.assertEqual(tv._volume, 0)

    def test_volume_unmutes_on_change(self):
        tv = Television()
        tv.power()
        tv.volume_up()
        tv.mute()
        self.assertTrue(tv._muted)
        tv.volume_up()
        self.assertFalse(tv._muted)
        self.assertEqual(tv._volume, 2)

    def test_mute_toggle(self):
        tv = Television()
        tv.power()
        tv.volume_up()
        tv.volume_up()
        tv.mute()
        self.assertTrue(tv._muted)
        self.assertEqual(str(tv), "Power = True, Channel = 0, Volume = 0")
        tv.mute()
        self.assertFalse(tv._muted)
        self.assertEqual(str(tv), "Power = True, Channel = 0, Volume = 2")

    def test_controls_do_nothing_when_off(self):
        tv = Television()
        tv.channel_up()
        tv.channel_down()
        tv.volume_up()
        tv.volume_down()
        tv.mute()
        self.assertEqual(str(tv), "Power = False, Channel = 0, Volume = 0")

if __name__ == '__main__':
    unittest.main()