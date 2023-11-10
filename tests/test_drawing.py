import unittest
from unittest.mock import patch
from src.drawing import draw_sphere, draw_tetrahedron

class TestDrawSphere(unittest.TestCase):
    @patch('src.drawing.glColor3f')
    @patch('src.drawing.gluSphere')
    @patch('src.drawing.gluNewQuadric')
    def test_draw_sphere(self, mock_gluNewQuadric, mock_gluSphere, mock_glColor3f):
        radius = 0.85
        draw_sphere(radius)
        mock_glColor3f.assert_called_once_with(0.0, 0.0, 0.0)
        mock_gluNewQuadric.assert_called_once()
        mock_gluSphere.assert_called_once_with(mock_gluNewQuadric.return_value, radius, 100, 100)

class TestDrawTetrahedron(unittest.TestCase):
    @patch('src.drawing.glBegin')
    @patch('src.drawing.glEnd')
    @patch('src.drawing.glVertex3f')
    @patch('src.drawing.glColor3f')
    def test_draw_tetrahedron(self, mock_glColor3f, mock_glVertex3f, mock_glEnd, mock_glBegin):
        draw_tetrahedron()
        expected_calls = [
            unittest.mock.call(0.0, 1.5, 0.0),
            unittest.mock.call(1.0, -1.0, -1.0),
            unittest.mock.call(-1.0, -1.0, -1.0),
            unittest.mock.call(0.0, 1.5, 0.0),
            unittest.mock.call(-1.0, -1.0, -1.0),
            unittest.mock.call(-1.0, -1.0, 1.0),
            unittest.mock.call(-1.0, -1.0, 1.0),
            unittest.mock.call(1.0, -1.0, 1.0),
            unittest.mock.call(1.0, -1.0, -1.0),
            unittest.mock.call(-1.0, -1.0, 1.0),
            unittest.mock.call(1.0, -1.0, -1.0),
            unittest.mock.call(-1.0, -1.0, -1.0)
        ]
        mock_glColor3f.assert_called_once_with(1.0, 0.75, 0.8)
        mock_glVertex3f.assert_has_calls(expected_calls)
        mock_glBegin.assert_called_once_with(4)  # 4 соответствует GL_TRIANGLES
        mock_glEnd.assert_called_once()