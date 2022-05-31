from rest_framework.pagination import PageNumberPagination as _PageNumberPagination


class PageNumberPagination(_PageNumberPagination):
    # 指定默认每一页的数据条数，优先级最高
    page_size = 10
    # 指定前端获取哪一页的key
    page_query_param = 'page'
    # 指定前端获取每页总数据的key
    page_size_query_param = 'size'
    # 每页最大条数
    max_page_size = 100
    # 无效页面错误提示
    invalid_page_message = '页码无效'
