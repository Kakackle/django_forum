from django.test import SimpleTestCase
from forum.forms import NewTopicForm

class TestForms(SimpleTestCase):

    def test_topic_form_valid_data(self):
        form = NewTopicForm(data={
            'name': 'test topic',
            'description': 'test description'
        })

        self.assertTrue(form.is_valid())
    
    def test_topic_form_invalid_data(self):
        form = NewTopicForm(data={
        })

        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 2)