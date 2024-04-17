from django.utils.deprecation import MiddlewareMixin
from django.conf import settings
from django.shortcuts import redirect, HttpResponse, render
from django.http import JsonResponse


class UserInfo(object):
    def __init__(self, role, name, id):
        self.id = id
        self.name = name
        self.role = role
        self.menu_name = None
        self.text_list = []


class AuthMiddleware(MiddlewareMixin):

    def is_white_url(self, request):
        if request.path_info in settings.NB_WHITE_URL:
            return True

    def process_request(self, request):
        """ 校验用户是否已登录 """
        # 1.不需要登录就能访问的URL
        if self.is_white_url(request):
            return

        # 2.session中获取用户信息，能获取到登录成功；未登录
        #  {'role': mapping[role], 'name': user_object.username, 'id': user_object.id}
        user_dict = request.session.get(settings.NB_SESSION_KEY)

        # 3.未登录，跳转回登录页面
        if not user_dict:
            return redirect(settings.NB_LOGIN_URL)

        # 4.已登录，封装用户信息
        request.nb_user = UserInfo(**user_dict)
        # request.nb_user.id
        # request.nb_user.name
        # request.nb_user.role
        # print(request.nb_user.name)

    def process_view(self, request, callback, callback_args, callback_kwargs):
        if self.is_white_url(request):
            return

        current_name = request.resolver_match.url_name

        # 0.是否是公共权限
        if current_name in settings.NB_PERMISSION_PUBLIC:
            return

        # 1.根据用户角色获取自己具备所有的权限
        user_permission_dict = settings.NB_PERMISSION[request.nb_user.role]

        # 2.获取当前用户访问的URL
        current_name = request.resolver_match.url_name

        # 3.判断是否在自己具备的权限
        if current_name not in user_permission_dict:
            # return HttpResponse("无权访问")

            # print(request.Meta)
            from django.core.handlers.wsgi import WSGIRequest
            # print(request,type(request))
            if request.is_ajax():
                return JsonResponse({'status': False, 'detail': "无权访问"})
            else:
                return render(request, 'permission.html')

        # 4.有权限
        text_list = []  # ["创建订单","订单列表"]
        text_list.append(user_permission_dict[current_name]['text'])

        menu_name = current_name
        while user_permission_dict[menu_name]['parent']:
            menu_name = user_permission_dict[menu_name]['parent']
            text = user_permission_dict[menu_name]['text']
            text_list.append(text)

        text_list.append("首页")

        text_list.reverse()

        # 4.1 当前菜单的值
        request.nb_user.menu_name = menu_name

        # 4.2 路径导航
        request.nb_user.text_list = text_list

        # print(text_list)
