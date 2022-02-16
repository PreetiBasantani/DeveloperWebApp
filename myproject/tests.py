from django.test import TestCase
from .forms import ProjectForm
from .models import Project
# Create your tests here.


class UnitTestCase(TestCase):
    
    def test_home_page(self):
        response = self.client.get('/')
        self.assertTemplateUsed('myprojecct/projects.html')

    def test_project_form(self):
        form =ProjectForm(data={'name':'Django Web Application','img':'photos/website.jpg',
        'description':'Nice Application','vote_total':200,'vote-ratio':50})
        self.assertTrue(form.is_valid())
#,'tags':('Ruby on Rails','Django'),

    def test_project_model(self):
        proj = Project()
        proj.name='Django Application'
        proj.img='photos/website.jpg'
        proj.save()
        proj_obj = Project.objects.get(name='Django Application')
        self.assertEqual('photos/website.jpg',proj_obj.img)

    def test_view_project(self):
        proj = Project()
        proj.name='Django Application'
        proj.img='photos/website.jpg'
        proj.save()
        proj_obj = Project.objects.get(name='Django Application')
        response = self.client.get('/')
        self.assertContains(response,'Django')