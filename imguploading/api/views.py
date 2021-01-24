from rest_framework import generics,mixins
from imguploading.models import Images
from imguploading.serializers import ImageSerializer
from rest_framework.permissions import IsAuthenticated
class ImageDelete(generics.DestroyAPIView):
    queryset=Images.objects.all()
    serializer_class = ImageSerializer
    permission_classes = [IsAuthenticated]
    # def get_queryset(self):
    #     queryset = Images.objects.filter( id=self.kwargs['pk'])
    #     if queryset[0].baseimage :
    #         queryset[0].baseimage.delete()
    #     if queryset[0].timage :
    #         queryset[0].timage.delete()
    #     return queryset
   
    # def destroy(self, request, *args, **kwargs):
    #     instance = self.get_object()
        # if instance.baseimage.file:
            # delete image file for the folder 
            # instance.baseimage.delete()
            # return Response("Cannot delete default system category", status=status.HTTP_400_BAD_REQUEST)
        # if instance.timage.file:
        #     instance.timage.delete()

        # now delete form bd
        # self.perform_destroy(instance)