"""
 @Time : 2021/3/6 15:35
 @Author : tango
 @FileName: handle_jwt_response.py
 @Software: PyCharm
 @E-mail : 13012830533@163.com
 @Description: 
"""


def jwt_response_payload_handler(token, user=None, request=None):
    """
    定制响应结果
    """
    return {
        'user_id': user.id,
        'username': user.username,
        'token': token
    }
