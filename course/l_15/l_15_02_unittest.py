from unittest import main, TestCase

from .l_15_01_polymorphism import Pigeon


class TestPigeon(TestCase):
    def setUp(self) -> None:  # Fixtures потрібні для того щоб ми збудували щось до того як почали користуватись
        self.pigeon = Pigeon()

    def tearDown(self) -> None:
        self.pigeon.die()

    def test_pigeon_voice(self):  # Naming - only 'test_name'
        # self.assertTrue(self.pigeon.voice() == 'cur cur', msg='the voice of pigeon not right' )

        self.assertEqual(self.pigeon.voice(), 'cur cur')

    def test_pigeon_voice_1(self):  # Naming - only 'test_name'
        self.assertTrue(self.pigeon.voice() == 'cur curк', msg='the voice of pigeon not right')

    def test_pigeon_is_live(self):
        self.assertTrue(self.pigeon.is_live(), msg='it is dead')


if __name__ == '__main__':
    main()  # Run all tests
