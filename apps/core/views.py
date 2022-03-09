from django.shortcuts import render


def custom_404(request, exception, template_name="404.html"):
    response = render(request, template_name)
    response.status_code = 404
    return response

def custom_403(request, exception, template_name="403.html"):
    response = render(request, template_name)
    response.status_code = 403
    return response

def custom_400(request, exception, template_name="400.html"):
    response = render(request, template_name)
    response.status_code = 400
    return response

def custom_500(request, *args, **argv):
    return render(request, '500.html', status=500)