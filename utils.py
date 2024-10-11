import unittest
from src.core.hybrid_scheduler import HexagScheduler
from src.core.classic_driver import ClassicProcessor

class TestHexagScheduler(unittest.TestCase):
    def test_add_classic_task(self):
        scheduler = HexagScheduler()
        task = "2 + 2"
        scheduler.add_task("classic", task)
        self.assertEqual(scheduler.classic_queue.qsize(), 1)

    def test_execute_classic_task(self):
        processor = ClassicProcessor()
        result = processor.execute_classic_task("2 + 2")
        self.assertEqual(result, 4)

if __name__ == '__main__':
    unittest.main()
