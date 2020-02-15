from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseRedirect, JsonResponse
from django.urls import reverse
from django.conf import settings

from django.db.models import Q

from itertools import chain

def index(request):
    return render(request, 'ff/index.html')

# def watch(request, video_id):
#     video = Video.objects.filter(pk=video_id)
#     context = {
#         "video" : video,
#         "form": q()
#     }
#     return render(request, 'vidboard/watch.html', context)


# # def search(request):
# #     form = q(request.GET)
# #     if form.is_valid():
# #         query = form.cleaned_data['q']
# #     video = Video.objects.filter(pk=query)
# #     print(query)
# #     context = {
# #         "video" : video,
# #     }
# #     return render(request, 'vidboard/watch.html', context)
# class VideoListCreate(generics.ListCreateAPIView):
#     queryset = Video.objects.all()
#     serializer_class = VideoSerializer