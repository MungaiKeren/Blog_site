import unittest
from app.models import Comment,Pitch
from app import db


class TestBlog(unittest.TestCase):
    def setUp(self):
        self.new_blog = Blog(content="blogger")
        self.new_comment = Comment(comment="comment",blog=self.new_blog)

    def tearDown(self):
        db.session.delete(self)
        User.query.commit()

    def test_instance(self):
        self.assertTrue(isinstance(self.new_comment.comment,"comment"))
    
    def test_check_instance_variables(self):
        self.assertEquals(self.new_comment.comment,"comment")
        self.assertEquals(self.new_comment.pitch,self.new_pitch,"pitch")

if __name__=="__main__":
    unittest.main()