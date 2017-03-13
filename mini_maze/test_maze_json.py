from django.test import TestCase

from settings import height, width, maze_json_filename
import json

class MazeJSONTest(TestCase):
    def setUp(self):
        self.maze_json = json.load(maze_json_filename)

    def test_dimensions(self):
        self.assertEqual(len(self.maze_json["maze"]), height)
        for row in self.maze_json["maze"]:
            self.assertEqual(len(row), width)