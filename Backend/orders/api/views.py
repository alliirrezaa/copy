from .serializers import OrderDetailSerializer
from rest_framework.response import Response
from rest_framework import status,viewsets,mixins,generics
from rest_framework.decorators import api_view
from ..models import OrderDetail
from rest_framework.generics import get_object_or_404
from django.utils.crypto import get_random_string
from django.core.mail import EmailMessage
from accounts.models import User

@api_view(['POST',])
def order_Detail(request):
    if request.method == 'POST':
        # remember old state
        _mutable = request.data._mutable
        # set to mutable
        request.data._mutable = True
        #change value
        code=get_random_string(length=8)
        request.data['tracking_code']=code
        # set mutable flag back
        request.data._mutable = _mutable

        serializer=OrderDetailSerializer(data=request.data)
        data={}
        if serializer.is_valid():
            form=serializer.save()
            data['response']='Successfully create a form.'
            subject='Order status'
            user=User.objects.get(id=request.data['userId'])
            email=str(user)
            msg='Your order has been successfully registered. Click the following link to see the factor.'
            body=subject+'\n'+email+'\n'+msg
            form=EmailMessage('Order',body,'software.proj.test@gmail.com',(email,))
            form.send(fail_silently=False)
            return Response(data)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class orderHitory(generics.ListAPIView):
    serializer_class = OrderDetailSerializer

    def get_queryset(self):
        return OrderDetail.objects.filter(userId=self.request.user)