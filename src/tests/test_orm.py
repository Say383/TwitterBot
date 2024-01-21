
import unittest
from orm import session_scope, User, Tweet

class ORMTestCase(unittest.TestCase):
    def test_add_user(self):
        # Test adding a user to the database
        with session_scope() as session:
            user_count_before = session.query(User).count()
            session.add(User(username="testuser"))
            user_count_after = session.query(User).count()
            self.assertEqual(user_count_before + 1, user_count_after)

if __name__ == '__main__':
    unittest.main()
