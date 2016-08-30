import django.http
from django.shortcuts import render, get_object_or_404, redirect, render_to_response
from django.template import RequestContext
from logging_setup import init_logging
from .models import DemoConfig, JIFTemplate
from .forms import DemoConfigForm, JIFTemplateForm

control = None

logger = init_logging()


def demo_controls(request):
    if request.method == "GET":
        context = RequestContext(request)
        context_dict = {'demo_status': control.demo_status}
        return render_to_response('APTDemo/demo_controller.html', context_dict, context)
    elif request.method == "POST":
        return render(request, 'APTDemo/demo_controller.html', {'controller': control})


def start_demo(request):
    reply = control.start_demo()
    return django.http.HttpResponse(reply)


def stop_demo(request):
    logger.debug('Stop demo request.')
    reply = control.stop_demo()
    return django.http.HttpResponse(reply)


def pause_demo(request):
    logger.debug('Stop demo request.')
    reply = control.stop_demo()
    return django.http.HttpResponse(reply)


def demo_config(request):
    demo = get_object_or_404(DemoConfig, pk=1)
    if request.method == "POST":
        form = DemoConfigForm(request.POST, instance=demo)
        if form.is_valid():
            logger.debug(form.data)
            demo = form.save(commit=False)
            demo.save()
    else:
        form = DemoConfigForm(instance=demo)
    return render(request, 'APTDemo/demo_config.html', {'form': form})


def jif_config(request):
    jif = get_object_or_404(JIFTemplate, pk=1)
    if request.method == "POST":
        form = JIFTemplateForm(request.POST, instance=jif)
        if form.is_valid():
            jif = form.save(commit=False)
            jif.save()
    else:
        form = JIFTemplateForm(instance=jif)
    return render(request, 'APTDemo/jif_config.html', {'form': form, 'jif': jif})
