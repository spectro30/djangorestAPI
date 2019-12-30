from django.shortcuts import render

from rest_framework import generics
from .serializers import InfoSerializer
from .models import Info


class CreateView(generics.ListCreateAPIView):
    queryset = Info.objects.all()
    serializer_class = InfoSerializer

    def perform_create(self, serializer):
        serializer.save()

        
class DetailsView(generics.RetrieveUpdateDestroyAPIView):    
    def test_api_can_get_a_info(self):
        info = Info.objects.get()
        response = self.client.get(
            reverse('details',
            kwargs={'pk': info.id}), format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, info)

    def test_api_can_update_info(self):
        change_info = {'val': 'Something new'}
        res = self.client.put(
            reverse('details', kwargs={'pk': info.id}),
            change_bucketlist, format='json'
        )
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_api_can_delete_info(self):
        info = Info.objects.get()
        response = self.client.delete(
            reverse('details', kwargs={'pk': info.id}),
            format='json',
            follow=True)
        self.assertEquals(response.status_code, status.HTTP_204_NO_CONTENT)

    queryset = Info.objects.all()
    serializer_class = InfoSerializer


