from django.test import TestCase
from rest_framework.test import APITestCase
from .models import WhyUs ,Team, Subscribe, Certificate,FeedBack,FAQ,FAQCategory
from .api.serializers import WhyUsSerializer, TeamSerializer, SubscribeSerializer,CertificateSerializer,FeedBackSerializer,FAQCategorySerializer,FAQSerializer


class WhyUsTestCase(APITestCase):
    def setUp(self):

        self.whyus = WhyUs.objects.create(
            title = 'test1',
            description = 'test2',
          
        )

    def test_whyus_content(self):
        serializer = WhyUsSerializer(self.whyus)
        serialized_data = serializer.data

        self.assertEqual(serialized_data['title'],'test1')
        self.assertEqual(serialized_data['description'],'test2')
    
    def test_whyus_invalid_data(self):
        # Test if invalid data raises error
        invalid_data = {'title': '', 'description': ''}
        serializer = WhyUsSerializer(data=invalid_data)
        self.assertFalse(serializer.is_valid())
        self.assertIn('title', serializer.errors)

    
class TeamTestCase(APITestCase):
    def setUp(self):

        self.team = Team.objects.create(
            name = 'Shahzod',
            image= 'test1.png',
            profession = 'data enginer',
            )
        
    def test_team_check(self):
        serializer = TeamSerializer(self.team)
        serializer_data = serializer.data


        self.assertEqual(serializer_data['name'],'Shahzod')
        self.assertEqual(serializer_data['image'],'/media/test1.png')
        self.assertEqual(serializer_data['profession'],'data enginer')

class SubscribeTestCase(APITestCase):
    def setUp(self):
        self.subscribe = Subscribe.objects.create(
            full_name = 'shahzod',
            phone_number = '+99894949494',
            is_checked = False,
        )

    def test_subscribe_check(self):
        serializer = SubscribeSerializer(self.subscribe)
        serializer_data = serializer.data

        self.assertEqual(serializer_data['full_name'],'shahzod')
        self.assertEqual(serializer_data['phone_number'],'+99894949494')
        self.assertEqual(serializer_data['is_checked'],False)


class CertificateTestCase(APITestCase):
    def setUp(self):
        self.certificate = Certificate.objects.create(
            title = 'test1',
            image = 'test1.png',
            description = 'test2'
        )

    def test_certificate(self):
        serializer = CertificateSerializer(self.certificate)
        serializer_data = serializer.data

        self.assertEqual(serializer_data['title'],'test1')
        self.assertEqual(serializer_data['image'],'/media/test1.png')
        self.assertEqual(serializer_data['description'],'test2')


class FeedbackTestCase(APITestCase):
    def setUp(self):
        self.feedback = FeedBack.objects.create(
            name = 'test1',
            image = 'test1',
            comment = 'test2',
            profession = 'test1'
        )

    def test_feedback(self):
        serialize = FeedBackSerializer(self.feedback)
        serialize_data = serialize.data

        self.assertEqual(serialize_data['name'],'test1')
        self.assertEqual(serialize_data['image'],'/media/test1')
        self.assertEqual(serialize_data['comment'],'test2')
        self.assertEqual(serialize_data['profession'],'test1')


class FAQTestCase(APITestCase):
    def setUp(self):

        self.category = FAQCategory.objects.create(
            title = 'test1'
        )

        self.faq = FAQ.objects.create(
            question = 'test1',
            answer = 'test2',
            faq_page =self.category 
        )

    def test_faq_answer_question(self):
        serializer = FAQSerializer(self.faq)
        serializer_data = serializer.data

        self.assertEqual(serializer_data['question'],'test1')
        self.assertEqual(serializer_data['answer'],'test2')
        self.assertEqual(serializer_data['faq_page'],self.category.id)
        
