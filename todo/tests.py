from django.test import TestCase, Client
from django.test.utils import setup_test_environment, teardown_test_environment
from django.urls import reverse
from .models import Todo


class TodoTestCase(TestCase):

    def setUp(self):
        Todo.create(title='Kill the cat', text='Use a tool')
        Todo.create(title='Feed dog', text='Give some food')
        Todo.create(title='', text='')
        Todo.create(title='Missing text', text='')
        Todo.create(title='', text='missing title')
        Todo.create(title='6', text='some text with 234=)(&&%')
        Todo.create(title='7', text='some other text')
        Todo.create(title='Last one', text='one. two, three')

    def test_default_order(self):
        kill_cat = Todo.objects.get(title='Kill the cat')
        feed_dog = Todo.objects.get(title='Feed dog')
        assert kill_cat.rank < feed_dog.rank

    def test_highest_rank(self):
        last_item = Todo.objects.get(title='Last one')
        assert last_item.rank == Todo.highest_rank

    def test_rerank_up(self):
        seven = Todo.objects.get(title='7')
        seven.rerank(1)
        seven.refresh_from_db()
        assert seven.rank == 1
        six = Todo.objects.get(title='6')
        assert six.rank == 7

    def test_rerank_down(self):
        six = Todo.objects.get(title='6')
        six.rerank(8)
        six.refresh_from_db()
        assert six.rank == 8
        seven = Todo.objects.get(title='7')
        assert seven.rank == 6

    def test_rerank_by_list(self):
        reranked = [7, 1, 2, 3, 4, 5, 6, 8]
        Todo.rerank_by_list(reranked)
        for pk in reranked:
            # + 1 because rank starts at 1, and indexes at 0
            assert Todo.objects.get(pk=pk).rank == reranked.index(pk) + 1

    def test_empty_fields(self):
        empty_title = Todo.objects.filter(title='').exclude(text='')[0]
        assert empty_title.text == 'missing title'
        empty_text = Todo.objects.filter(text='').exclude(title='')[0]
        assert empty_text.title == 'Missing text'

    def test_load_index(self):
        c = Client()
        response = c.get(reverse('todo:index'))
        self.assertTemplateUsed(response, 'todo/index.html')
        assert response.status_code == 200
        assert response['content-type'] == 'text/html; charset=utf-8'

    def test_load_item(self):
        c = Client()
        response = c.get(reverse('todo:todo_details_partial', args=[1]))
        assert response.status_code == 200
        assert b'Kill the cat' in response.content

    def test_add_item(selg):
        c = Client(HTTP_HX_CURRENT_URL='/')
        response = c.post(
            reverse('todo:create'), {'title': 'Some title', 'text': 'some text'})
        assert response.status_code == 200
        response = c.get(reverse('todo:todo_details_partial', args=[9]))
        assert response.status_code == 200
        assert b'Some title' in response.content
        assert b'some text' in response.content
