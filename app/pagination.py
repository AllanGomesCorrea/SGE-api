from rest_framework.pagination import PageNumberPagination

class CustomPageNumberPagination(PageNumberPagination):
    page_size_query_param = 'page_size'  # Permite definir o número de itens por página via query param
    max_page_size = 50  # Define um limite máximo de itens por página para evitar sobrecarga
