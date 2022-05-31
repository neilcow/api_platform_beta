from rest_framework.filters import OrderingFilter
from rest_framework.permissions import IsAuthenticated

from utils.constant.serializer_base_constant import SerializerFieldBaseConstant
from utils.pagenation import PageNumberPagination


class BaseViews:
    permission_classes = [IsAuthenticated]
    pagination_class = PageNumberPagination
    # 设置引擎为排序引擎
    filter_backends = [OrderingFilter]
    # 设置排序的字段
    ordering_fields = [SerializerFieldBaseConstant.ID_FIELD]
    lookup_field = SerializerFieldBaseConstant.ID_FIELD
    RESULTS_KEY = "results"

    def names(self, request, key, *args, **kwargs):
        response = self.retrieve(request, *args, **kwargs)
        response.data = response.data.get(key)
        return response
