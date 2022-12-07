from datetime import date

from checkin_system.api.filter import CheckindataFilter, HrdataFilter
from checkin_system.models import Checkindata, Hrdata
from django.utils import timezone
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView

from .pagination import LargeResultsSetPagination
from .serializers import CheckindataSerializer, HrdataSerializer


# Create your views here.
class HrdataViewSet(viewsets.ModelViewSet):
    queryset = Hrdata.objects.all()
    serializer_class = HrdataSerializer
    pagination_class = LargeResultsSetPagination
    filter_backends = [DjangoFilterBackend]
    filter_class = HrdataFilter


class CheckindataViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Checkindata.objects.all()
    serializer_class = CheckindataSerializer
    pagination_class = LargeResultsSetPagination
    filter_backends = [DjangoFilterBackend]
    filter_class = CheckindataFilter


class ChekinView(APIView):

    def post(self, request):
        resp = {
            'api_success': False,
            'msg': None
        }

        try:
            employee_id = request.data['employee_id']
            today_date = date.today()
            checkin_time = timezone.now()

            temp_obj = Checkindata.objects.filter(
                employee_id=employee_id,
                checkin_date=today_date
            ).first()

            if not temp_obj:
                temp_obj = Checkindata.objects.create(
                    employee_id=employee_id
                )

            if not temp_obj.timein:
                temp_obj.timein = checkin_time
                temp_obj.save()

                resp['api_success'] = True
                return Response(resp)

            temp_obj.timeout = checkin_time
            temp_obj.save()

            resp['api_success'] = True
            return Response(resp)

        except Exception as err:
            resp['api_success'] = False
            resp['msg'] =\
                f'api unavailable. Please contact the developer. err:{err}'
            return Response(resp)


class SupervisorCheckView(APIView):

    def get(self, request):
        resp = {
            'api_success': False,
            'msg': None,
            'data': None
        }

        try:
            supervisor_id = request.GET.get('supervisor_id', None)
            search_date = request.GET.get('search_date', None)

            if (not supervisor_id) or (not search_date):
                resp['msg'] = 'lost supervisor_id or search_date parameters'
                return Response(resp)

            member_list = list(Hrdata.objects.filter(
                supervisor_id=supervisor_id).values_list(
                    'employee_id', flat=True).distinct())

            temp_obj_qs = Checkindata.objects.filter(
                employee_id__in=member_list,
                checkin_date=search_date
            ).values()

            resp['data'] = temp_obj_qs
            resp['api_success'] = True
            return Response(resp)

        except Exception as err:
            resp['api_success'] = False
            resp['msg'] =\
                f'api unavailable. Please contact the developer. err:{err}'
            return Response(resp)
