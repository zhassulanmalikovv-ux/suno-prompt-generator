import unittest
from datetime import date, timedelta
from daily_prompts import daily_collection


class DailyPromptsTest(unittest.TestCase):
    def test_same_day_is_stable_and_next_day_changes(self):
        day = date(2026, 10, 5)
        self.assertEqual(daily_collection(day), daily_collection(day))
        self.assertNotEqual(daily_collection(day)[1], daily_collection(day + timedelta(days=1))[1])

    def test_collections_have_unique_copy_ready_prompts_within_suno_limit(self):
        for offset in range(366):
            _, rows = daily_collection(date(2026, 1, 1) + timedelta(days=offset))
            self.assertEqual(len(rows), 8)
            self.assertEqual(len({row['title'] for row in rows}), 8)
            for row in rows:
                self.assertTrue(0 < len(row['style_prompt']) <= 900)


if __name__ == '__main__':
    unittest.main()
