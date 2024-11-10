import json

from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render
from .models import *
from cryptography.fernet import Fernet
import random
import datetime
import requests
from django import template
from django.views.decorators.clickjacking import xframe_options_exempt
from django.views.decorators.csrf import csrf_exempt
from django.core.mail import send_mail
from django.conf import settings
from django.utils.html import strip_tags
import boto3
from django.forms.models import model_to_dict
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods

# from gdstorage.storage import GoogleDriveStorage

register = template.Library()
client_id = 'AamB-Te52PnmRJKM7rmroLZ_m7j9voNh9aqkqSkvBKx0kWX_64LqTwbBr9k8b8oXzi2S7LCHGu-b6umZ'
client_key = 'EI9D1G-ilWpyvJYesga2b3s13lqk53h3QSjsVY6UMhYqz29ZloMiRouTwFM82obO16fr725FblHHaNrl'

iframe = 'ET-fOTwEB78NHvQF2wGouthaMjg5uYMT-MrpDnKrq8c='

Imgur_Client_ID="d4adccbc743e99a"
Imgur_Client_secret="894ad64b02348ae6402c93a3f8fe9dd6fb8eec1d"

message1 = '''<!DOCTYPE html
    PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">

<head>
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <meta name="x-apple-disable-message-reformatting" />
    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
    <meta name="color-scheme" content="light dark" />
    <meta name="supported-color-schemes" content="light dark" />
    <title></title>
    <style type="text/css" rel="stylesheet" media="all">
        /* Base ------------------------------ */

        @import url("https://fonts.googleapis.com/css?family=Nunito+Sans:400,700&display=swap");

        body {
            width: 100% !important;
            height: 100%;
            margin: 0;
            -webkit-text-size-adjust: none;
        }

        a {
            color: #3869D4;
        }

        a img {
            border: none;
        }

        td {
            word-break: break-word;
        }

        .preheader {
            display: none !important;
            visibility: hidden;
            mso-hide: all;
            font-size: 1px;
            line-height: 1px;
            max-height: 0;
            max-width: 0;
            opacity: 0;
            overflow: hidden;
        }

        /* Type ------------------------------ */

        body,
        td,
        th {
            font-family: "Nunito Sans", Helvetica, Arial, sans-serif;
        }

        h1 {
            margin-top: 0;
            color: #333333;
            font-size: 22px;
            font-weight: bold;
            text-align: left;
        }

        h2 {
            margin-top: 0;
            color: #333333;
            font-size: 16px;
            font-weight: bold;
            text-align: left;
        }

        h3 {
            margin-top: 0;
            color: #333333;
            font-size: 14px;
            font-weight: bold;
            text-align: left;
        }

        td,
        th {
            font-size: 16px;
        }

        p,
        ul,
        ol,
        blockquote {
            margin: .4em 0 1.1875em;
            font-size: 16px;
            line-height: 1.625;
        }

        p.sub {
            font-size: 13px;
        }

        /* Utilities ------------------------------ */

        .align-right {
            text-align: right;
        }

        .align-left {
            text-align: left;
        }

        .align-center {
            text-align: center;
        }

        /* Buttons ------------------------------ */

        .button {
            background-color: #22BC66;
            border-top: 10px solid #22BC66;
            border-right: 18px solid #22BC66;
            border-bottom: 10px solid #22BC66;
            border-left: 18px solid #22BC66;
            display: inline-block;
            color: #FFF;
            text-decoration: none;
            border-radius: 3px;
            box-shadow: 0 2px 3px rgba(0, 0, 0, 0.16);
            -webkit-text-size-adjust: none;
            box-sizing: border-box;
        }

        .button--green {
            background-color: #3869D4;
            border-top: 10px solid #3869D4;
            border-right: 18px solid #3869D4;
            border-bottom: 10px solid #3869D4;
            border-left: 18px solid #3869D4;
        }

        .button--red {
            background-color: #FF6136;
            border-top: 10px solid #FF6136;
            border-right: 18px solid #FF6136;
            border-bottom: 10px solid #FF6136;
            border-left: 18px solid #FF6136;
        }

        @media only screen and (max-width: 500px) {
            .button {
                width: 100% !important;
                text-align: center !important;
            }
        }

        /* Attribute list ------------------------------ */

        .attributes {
            margin: 0 0 21px;
        }

        .attributes_content {
            background-color: #F4F4F7;
            padding: 16px;
        }

        .attributes_item {
            padding: 0;
        }

        /* Related Items ------------------------------ */

        .related {
            width: 100%;
            margin: 0;
            padding: 25px 0 0 0;
            -premailer-width: 100%;
            -premailer-cellpadding: 0;
            -premailer-cellspacing: 0;
        }

        .related_item {
            padding: 10px 0;
            color: #CBCCCF;
            font-size: 15px;
            line-height: 18px;
        }

        .related_item-title {
            display: block;
            margin: .5em 0 0;
        }

        .related_item-thumb {
            display: block;
            padding-bottom: 10px;
        }

        .related_heading {
            border-top: 1px solid #CBCCCF;
            text-align: center;
            padding: 25px 0 10px;
        }

        /* Discount Code ------------------------------ */

        .discount {
            width: 100%;
            margin: 0;
            padding: 24px;
            -premailer-width: 100%;
            -premailer-cellpadding: 0;
            -premailer-cellspacing: 0;
            background-color: #F4F4F7;
            border: 2px dashed #CBCCCF;
        }

        .discount_heading {
            text-align: center;
        }

        .discount_body {
            text-align: center;
            font-size: 15px;
        }

        /* Social Icons ------------------------------ */

        .social {
            width: auto;
        }

        .social td {
            padding: 0;
            width: auto;
        }

        .social_icon {
            height: 20px;
            margin: 0 8px 10px 8px;
            padding: 0;
        }

        /* Data table ------------------------------ */

        .purchase {
            width: 100%;
            margin: 0;
            padding: 35px 0;
            -premailer-width: 100%;
            -premailer-cellpadding: 0;
            -premailer-cellspacing: 0;
        }

        .purchase_content {
            width: 100%;
            margin: 0;
            padding: 25px 0 0 0;
            -premailer-width: 100%;
            -premailer-cellpadding: 0;
            -premailer-cellspacing: 0;
        }

        .purchase_item {
            padding: 10px 0;
            color: #51545E;
            font-size: 15px;
            line-height: 18px;
        }

        .purchase_heading {
            padding-bottom: 8px;
            border-bottom: 1px solid #EAEAEC;
        }

        .purchase_heading p {
            margin: 0;
            color: #85878E;
            font-size: 12px;
        }

        .purchase_footer {
            padding-top: 15px;
            border-top: 1px solid #EAEAEC;
        }

        .purchase_total {
            margin: 0;
            text-align: right;
            font-weight: bold;
            color: #333333;
        }

        .purchase_total--label {
            padding: 0 15px 0 0;
        }

        body {
            background-color: #F4F4F7;
            color: #51545E;
        }

        p {
            color: #51545E;
        }

        p.sub {
            color: #6B6E76;
        }

        .email-wrapper {
            width: 100%;
            margin: 0;
            padding: 0;
            -premailer-width: 100%;
            -premailer-cellpadding: 0;
            -premailer-cellspacing: 0;
            background-color: #F4F4F7;
        }

        .email-content {
            width: 100%;
            margin: 0;
            padding: 0;
            -premailer-width: 100%;
            -premailer-cellpadding: 0;
            -premailer-cellspacing: 0;
        }

        /* Masthead ----------------------- */

        .email-masthead {
            padding: 25px 0;
            text-align: center;
        }

        .email-masthead_logo {
            width: 94px;
        }

        .email-masthead_name {
            font-size: 16px;
            font-weight: bold;
            color: #A8AAAF;
            text-decoration: none;
            text-shadow: 0 1px 0 white;
        }

        /* Body ------------------------------ */

        .email-body {
            width: 100%;
            margin: 0;
            padding: 0;
            -premailer-width: 100%;
            -premailer-cellpadding: 0;
            -premailer-cellspacing: 0;
            background-color: #FFFFFF;
        }

        .email-body_inner {
            width: 570px;
            margin: 0 auto;
            padding: 0;
            -premailer-width: 570px;
            -premailer-cellpadding: 0;
            -premailer-cellspacing: 0;
            background-color: #FFFFFF;
        }

        .email-footer {
            width: 570px;
            margin: 0 auto;
            padding: 0;
            -premailer-width: 570px;
            -premailer-cellpadding: 0;
            -premailer-cellspacing: 0;
            text-align: center;
        }

        .email-footer p {
            color: #6B6E76;
        }

        .body-action {
            width: 100%;
            margin: 30px auto;
            padding: 0;
            -premailer-width: 100%;
            -premailer-cellpadding: 0;
            -premailer-cellspacing: 0;
            text-align: center;
        }

        .body-sub {
            margin-top: 25px;
            padding-top: 25px;
            border-top: 1px solid #EAEAEC;
        }

        .content-cell {
            padding: 35px;
        }

        /*Media Queries ------------------------------ */

        @media only screen and (max-width: 600px) {

            .email-body_inner,
            .email-footer {
                width: 100% !important;
            }
        }

        @media (prefers-color-scheme: dark) {

            body,
            .email-body,
            .email-body_inner,
            .email-content,
            .email-wrapper,
            .email-masthead,
            .email-footer {
                background-color: #333333 !important;
                color: #FFF !important;
            }

            p,
            ul,
            ol,
            blockquote,
            h1,
            h2,
            h3 {
                color: #FFF !important;
            }

            .attributes_content,
            .discount {
                background-color: #222 !important;
            }

            .email-masthead_name {
                text-shadow: none !important;
            }
        }

        :root {
            color-scheme: light dark;
            supported-color-schemes: light dark;
        }
    </style>
    <!--[if mso]>
    <style type="text/css">
      .f-fallback  {
        font-family: Arial, sans-serif;
      }
    </style>
  <![endif]-->
</head>'''

s3_client = boto3.client('s3')

def save_files(request):
    try:
        imgur_api_url = "https://api.imgur.com/3/image"
        headers = {"Authorization": f"Client-ID {Imgur_Client_ID}"}
        file_names=""
        files = request.FILES.getlist('images')
        file_paths = []

        for file in files:
            # print(file.name)
            payload = {"image": file}
            response = requests.post(imgur_api_url, headers=headers, files=payload)
            # print(response.text)
            if response.status_code == 200:
                response = json.loads(response.text)
                print(response["data"]["link"])
                file_paths.append(response["data"]["link"])

        if file_paths:
            file_names += ','.join(file_paths)

        return file_names
    except Exception as e:
        print(e)
        return ""


def check_integration_credentials(url,email,password,api_key):
    payload = json.dumps({
        "email": email,
        "password": password,
        "api_key": api_key
    })
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    if response.status_code==200:
        return response.json()
    return False

def get_access_token():
    data = {
        'grant_type': 'client_credentials',

    }
    response = requests.post('https://api-m.paypal.com/v1/oauth2/token', data=data, auth=(
        client_id, client_key))
    return response.json()["access_token"]


def payment_check(request, id="", email=""):
    try:
        if email == "":
            email = request.session['email']
        user = Profiles.objects.get(email=email)

        #Need to remove - Temp Fix
        if user.subscriber_id =="GROZIITADMIN":
            return True

        headers = {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer ' + get_access_token(),
        }
        try:
            if id == "":
                id = request.POST['subscriptionID']
        except:
            id = user.subscriber_id

        subscriptions_response = requests.get(
            'https://api-m.paypal.com/v1/billing/subscriptions/' + id,
            headers=headers)

        # print("subscriptionID:", id, subscriptions_response.json()["status"])
        if subscriptions_response.json()["status"] == "ACTIVE":
            user.subscriber_id = id
            user.subscriber = True
            user.save()
        else:
            user.subscriber_id = id
            user.subscriber = False
            user.save()
        return True
    except Exception as e:
        print(e)
        return False


def payment(request):
    if not logged_in(request):
        return HttpResponseRedirect('pages-login')
    try:
        if not payment_check(request):
            raise Exception

        request.session[
            'message'] = '<b> <i class="bi bi-check-circle-fill" style="color: green"></i> Payment Successful..!</b>'
        return HttpResponseRedirect("users-profile")

    except Exception as e:
        request.session[
            'message'] = '<b> <i class="bi bi-x-circle-fill" style="color: red"></i> Payment Unsuccessful..!<br>Please contact admin or try again.</b>'
        return HttpResponseRedirect("users-profile")


@register.simple_tag
def split(string):
    return string.split()


def logged_in(request):
    try:
        profile = Profiles.objects.get(email=request.session['email'])
        fernet = Fernet(profile.key.encode('utf-8'))

        try:
            if (profile.subscriber_id == "" or profile.subscriber_id.lower() == "na") and profile.subscriber == False:
                pass
            elif profile.subscriber_id != "" or profile.subscriber_id.lower() != "na":
                payment_check(request)
        except:
            pass

        if (profile.password == fernet.decrypt(request.session['password'].encode()).decode('utf-8')):
            return True
    except Exception as e:
        print(e)
        return False


def message_check(request):
    msg = ""
    if "message" not in request.session.keys():
        request.session["message"] = ""
    msg, request.session["message"] = request.session["message"], ""
    return msg


def register(request):
    try:
        profile = Profiles()
        profile.name = request.POST['name']
        profile.email = request.POST['email'].lower()
        profile.username = request.POST['username']
        profile.password = request.POST['password']
        profile.job = request.POST['job']
        profile.account_type = request.POST['accountType']
        profile.company = request.POST['company']
        profile.key = Fernet.generate_key().decode('utf-8')
        profile.save()
        request.session[
            'message'] = '<b> <i class="bi bi-check-circle-fill" style="color: green"></i> Successfully created your account!</b>'
        return HttpResponseRedirect('pages-login')
    except Exception as e:
        print(e)
        request.session[
            'message'] = '<b> <i class="bi bi-x-circle-fill" style="color: red"></i> There is an error creating your account<br>Please try again or Contact us</b>'
        return HttpResponseRedirect("pages-register")


def login(request):
    try:
        profile = Profiles.objects.get(email__iexact=request.POST['email'])
        if (profile.password == request.POST['password']):
            request.session['email'] = profile.email
            fernet = Fernet(profile.key.encode('utf-8'))
            request.session['password'] = fernet.encrypt(profile.password.encode()).decode('utf-8')
            return HttpResponseRedirect('index')
        else:
            raise Exception
    except Exception as e:
        print(e)
        request.session[
            'message'] = '<b> <i class="bi bi-x-circle-fill" style="color: red"></i> Incorrect Credentials Please try again</b>'
        return HttpResponseRedirect('pages-login')


def logout(request):
    try:
        request.session.flush()
    except:
        pass
    return HttpResponseRedirect('pages-login')


def handler404(request, exception):
    return render(request, 'pages-error-404.html', status=404)


def handler500(request):
    return render(request, 'pages-error-404.html', status=500)


def index(request):
    if not logged_in(request):
        return HttpResponseRedirect('pages-login')

    profile = Profiles.objects.get(email=request.session['email'])

    iframe_data = ""
    if profile.account_type in ["Form","Images"]:
        fernet = Fernet(iframe)
        iframe_data = request.session["email"] + "~" + request.session["password"]
        iframe_data = fernet.encrypt(iframe_data.encode()).decode('utf-8')

    jobs = Jobs.objects.filter(posted_by=request.session['email'])
    datas = FormData.objects.filter(posted_for=request.session['email'])
    contents = Content.objects.filter(posted_by=request.session['email'])
    #Adding 1st form field data as preview
    for form_data in datas:
        #print(form_data.data.split("<br>", 1)[0].split(":")[1])
        form_data.preview = form_data.data.split("<br>", 1)[0].split(":")[1]
    return render(request, "index.html",
                  {'jobs': jobs,'datas':datas, 'username': profile.username, 'role': profile.job,
                   "contents": contents,
                   "pp": profile.img_url, "msg": message_check(request), "actype": profile.account_type,
                   "i_frame": iframe_data})


def add_post(request):
    if not logged_in(request):
        return HttpResponseRedirect('pages-login')

    profile = Profiles.objects.get(email=request.session['email'])

    return render(request, "add-post.html", {'username': profile.username, 'role': profile.job,
                                             "pp": profile.img_url, "actype": profile.account_type,
                                             "msg": message_check(request)})

def add_content(request):
    if not logged_in(request):
        return HttpResponseRedirect('pages-login')

    if request.method == 'POST':
        try:
            content = Content()
            content.title = request.POST['title']
            content.subtitle = request.POST['sub-title']
            content.description = request.POST['description']
            content.posted_by = request.session['email']
            content.key = Fernet.generate_key().decode('utf-8')
            content.save()

            request.session[
                'message'] = f'<b> <i class="bi bi-check-circle-fill" style="color: green"></i> Successfully added the content!</b>'
            return HttpResponseRedirect('add-content')
        except Exception as e:
            print(e)
            request.session[
                'message'] = '<b> <i class="bi bi-x-circle-fill" style="color: red"></i> Error Editing<br>Please try again.</b>'
            return HttpResponseRedirect('add-content')
    else:
        profile = Profiles.objects.get(email=request.session['email'])

        return render(request, "add-content.html", {'username': profile.username, 'role': profile.job,
                                                 "pp": profile.img_url, "actype": profile.account_type,
                                                 "msg": message_check(request)})


def edit_post(request):
    if not logged_in(request):
        return HttpResponseRedirect('pages-login')
    try:
        job = Jobs.objects.get(id=request.GET["id"])
        profile = Profiles.objects.get(email=request.session['email'])
        return render(request, "edit-post.html",
                      {'job': job, 'username': profile.username, 'role': profile.job,
                       "pp": profile.img_url, "actype": profile.account_type, "msg": message_check(request)})
    except Exception as e:
        return HttpResponseRedirect('index')

def edit_content(request):
    if not logged_in(request):
        return HttpResponseRedirect('pages-login')
    if request.method=="POST":
        try:
            content = Content.objects.get(id=request.POST["id"], posted_by=request.session['email'])
            content.title = request.POST['title']
            content.subtitle = request.POST['sub-title']
            content.description = request.POST['description']
            content.save()
            request.session[
                'message'] = f'<b> <i class="bi bi-check-circle-fill" style="color: green"></i> Successfully edited the Content!</b>'
            return HttpResponseRedirect('index')
        except Exception as e:
            print(e)
            request.session[
                'message'] = '<b> <i class="bi bi-x-circle-fill" style="color: red"></i> Error Editing<br>Please try again.</b>'
            return HttpResponseRedirect('index')
    try:
        content = Content.objects.get(id=request.GET["id"])
        profile = Profiles.objects.get(email=request.session['email'])
        return render(request, "edit-content.html",
                      {'content': content, 'username': profile.username, 'role': profile.job,
                       "pp": profile.img_url, "actype": profile.account_type, "msg": message_check(request)})
    except Exception as e:
        return HttpResponseRedirect('index')

def delete_post(request):
    if not logged_in(request):
        return HttpResponseRedirect('pages-login')
    try:
        profile = Profiles.objects.get(email=request.session['email'])
        job = Jobs.objects.get(id=request.GET["id"],posted_by=request.session['email'])
        job.delete()
        request.session[
            'message'] = f'<b> <i class="bi bi-check-circle-fill" style="color: green"></i> Successfully deleted the {profile.account_type}!</b>'
        return HttpResponseRedirect('index')
    except Exception as e:
        print(e)
        request.session[
            'message'] = '<b> <i class="bi bi-x-circle-fill" style="color: red"></i> Error deleting<br>Please try again.</b>'
        return HttpResponseRedirect('index')

def delete_content(request):
    if not logged_in(request):
        return HttpResponseRedirect('pages-login')
    try:
        profile = Profiles.objects.get(email=request.session['email'])
        content = Content.objects.get(id=request.GET["id"],posted_by=request.session['email'])
        content.delete()
        request.session[
            'message'] = f'<b> <i class="bi bi-check-circle-fill" style="color: green"></i> Successfully deleted the {profile.account_type}!</b>'
        return HttpResponseRedirect('index')
    except Exception as e:
        print(e)
        request.session[
            'message'] = '<b> <i class="bi bi-x-circle-fill" style="color: red"></i> Error deleting<br>Please try again.</b>'
        return HttpResponseRedirect('index')


def adding_job(request):
    if not logged_in(request):
        return HttpResponseRedirect('pages-login')
    try:
        profile = Profiles.objects.get(email=request.session['email'])
        job = Jobs()
        job.title = request.POST['title']
        job.posted_by = request.session['email']
        if profile.account_type in ['Job','Form']:
            job.description = request.POST['description']
        elif profile.account_type == "Images":
            job.description = save_files(request)

        if profile.account_type == "Job":
            job.sdescription = request.POST['sdescription']
            job.location = request.POST['location']
            job.eemail = request.POST['eemail']
            job.company = request.POST['company']
            job.logo_img_url = request.POST['logo_img_url']
            job.expire_in_days = request.POST['expire_in_days']
            job.background_img_url = request.POST['background_img_url']
            job.keywords = request.POST['keywords']
        elif profile.account_type == "Form":
            job.need_files = request.POST['needfiles'] == "Yes"

        job.save()
        request.session[
            'message'] = f'<b> <i class="bi bi-check-circle-fill" style="color: green"></i> Successfully added the {profile.account_type}!</b>'
        return HttpResponseRedirect('index')
    except Exception as e:
        print(e)
        request.session[
            'message'] = '<b> <i class="bi bi-x-circle-fill" style="color: red"></i> Error Editing<br>Please try again.</b>'
        return HttpResponseRedirect('add-post')


def editing_job(request):
    if not logged_in(request):
        return HttpResponseRedirect('pages-login')
    try:
        profile = Profiles.objects.get(email=request.session['email'])
        job = Jobs.objects.get(id=request.POST["id"],posted_by=request.session['email'])
        job.title = request.POST['title']
        if profile.account_type in ['Job', 'Form']:
            job.description = request.POST['description']
        elif profile.account_type == "Images":
            new_images = save_files(request)
            if job.description!="" and new_images!="":
                job.description = ",".join([job.description,new_images])
            elif new_images!="":
                job.description = new_images

        if profile.account_type == "Job":
            job.sdescription = request.POST['sdescription']
            job.location = request.POST['location']
            job.eemail = request.POST['eemail']
            job.company = request.POST['company']
            job.logo_img_url = request.POST['logo_img_url']
            job.expire_in_days = request.POST['expire_in_days']
            job.background_img_url = request.POST['background_img_url']
            job.keywords = request.POST['keywords']
        elif profile.account_type == "Form":
            job.need_files = request.POST['needfiles'] == "Yes"
        job.save()
        request.session[
            'message'] = f'<b> <i class="bi bi-check-circle-fill" style="color: green"></i> Successfully edited the {profile.account_type}!</b>'
        return HttpResponseRedirect('index')
    except Exception as e:
        print(e)
        request.session[
            'message'] = '<b> <i class="bi bi-x-circle-fill" style="color: red"></i> Error Editing<br>Please try again.</b>'
        return HttpResponseRedirect('edit-post')

def GroziitRemoveImage(request):
    if not logged_in(request):
        return HttpResponseRedirect('pages-login')

    try:
        profile = Profiles.objects.get(email=request.session['email'])
        if request.method=="POST" and profile.account_type == "Images":
            job_id, image_id = request.POST['key'].split("_")
            job = Jobs.objects.get(id=job_id, posted_by=request.session['email'])
            images = job.description.split(",")
            del images[int(image_id)]
            job.description = ",".join(images)
            job.save()

            return HttpResponse('<b> <i class="bi bi-check-circle-fill" style="color: green"></i> Successfully deleted the image!</b>')

    except Exception as e:
        print(e)
        return HttpResponse('<b> <i class="bi bi-x-circle-fill" style="color: red"></i> Error Editing<br>Please try again.</b>')


@xframe_options_exempt
def GroziitDynamicSpace(request):
    if not logged_in(request):
        try:
            data = request.GET["data"]
            fernet = Fernet(iframe)
            data = fernet.decrypt(data.encode()).decode()

            email, password = data.split("~")

            profile = Profiles.objects.get(email=email)

            if not payment_check(request, id=profile.subscriber_id, email=email):
                raise Exception

            if profile.subscriber == False:
                raise Exception

            fernet = Fernet(profile.key.encode('utf-8'))

            if (profile.password != fernet.decrypt(password.encode()).decode('utf-8')):
                raise Exception

        except Exception as e:
            return HttpResponseRedirect('404')
    else:
        email = request.session['email']
        # return HttpResponseRedirect('pages-login')
    jobs = Jobs.objects.filter(posted_by=email)
    integrated_jobs = []
    try:
        account_integrations = AccountIntegrations.objects.filter(account=email)

        for integration in account_integrations:
            authentication_link, jobs_list_link = integration.integration.links.split(",")[:2]

            access_token = check_integration_credentials(authentication_link,
                                                         integration.email,
                                                         integration.password,
                                                         integration.api_key)['access_token']

            while True:

                headers = {
                    'Content-Type': 'application/json',
                    'accept': 'application/json',
                    'Authorization': f'Bearer {access_token}'
                }

                response = requests.request("GET", jobs_list_link, headers=headers).json()

                for job in response['results']: job['integration_id'] = integration.integration.id

                integrated_jobs.extend(response['results'])
                jobs_list_link = response['next']
                if not jobs_list_link:
                    break

    except Exception as e:
        print(e)
        pass

    return render(request, "GroziitJobs.html", {'jobs': jobs,'integrated_jobs':integrated_jobs,"jobs_count":len(jobs)+len(integrated_jobs)})


@xframe_options_exempt
def integration_detail(request,id,integration_id):
    if not logged_in(request):
        try:
            data = request.GET["data"]
            fernet = Fernet(iframe)
            data = fernet.decrypt(data.encode()).decode()

            email, password = data.split("~")

            profile = Profiles.objects.get(email=email)

            company = profile.company

            if not payment_check(request, id=profile.subscriber_id, email=email):
                raise Exception

            if profile.subscriber == False:
                raise Exception

            fernet = Fernet(profile.key.encode('utf-8'))

            if (profile.password != fernet.decrypt(password.encode()).decode('utf-8')):
                raise Exception

        except Exception as e:
            return HttpResponseRedirect('404')

    else:
        email = request.session['email']
        profile = Profiles.objects.get(email=email)
        company = profile.company
    try:
        integration = AccountIntegrations.objects.get(account=email,integration_id=integration_id)

        authentication_link, jobs_list_link,job_details_link,posted_by_link = integration.integration.links.split(",")[:4]

        access_token = check_integration_credentials(authentication_link,
                                                     integration.email,
                                                     integration.password,
                                                     integration.api_key)['access_token']

        headers = {
            'Content-Type': 'application/json',
            'accept': 'application/json',
            'Authorization': f'Bearer {access_token}'
        }

        response = requests.request("GET", job_details_link+id, headers=headers).json()

        posted_by = requests.request("GET", posted_by_link+response.get('posted_by'), headers=headers).json().get('email_id')

        job={
            'title': response.get('position_title'),
            'company': company,
            'description': response.get('requisition_description'),
            'location': f'{response.get("state")},{response.get("country")}'.strip(),
            'eemail': posted_by,
            'expire_in_days': response.get('closing_date').strip(),
            'time': response.get('posted'),
            'need_files': True,
            'integration_id': integration_id,
            'id': id
        }

    except Exception as e:
        print(e)
        return HttpResponseRedirect('404')

    return render(request, "detail.html", {"job": job, "msg": message_check(request), 'integration': True})


@xframe_options_exempt
def postdetail(request):
    if not logged_in(request):
        try:
            data = request.GET["data"]
            fernet = Fernet(iframe)
            data = fernet.decrypt(data.encode()).decode()

            email, password = data.split("~")

            profile = Profiles.objects.get(email=email)

            if not payment_check(request, id=profile.subscriber_id, email=email):
                raise Exception

            if profile.subscriber == False:
                raise Exception

            fernet = Fernet(profile.key.encode('utf-8'))

            if (profile.password != fernet.decrypt(password.encode()).decode('utf-8')):
                raise Exception

            job = Jobs.objects.get(id=request.GET['job'], posted_by=email)
            return render(request, "detail.html", {"job": job, "msg": message_check(request)})

        except Exception as e:
            return HttpResponseRedirect('404')
    job = Jobs.objects.get(id=request.GET['job'], posted_by=request.session['email'])
    # job.time = tim
    return render(request, "detail.html", {"job": job, "msg": message_check(request)})


@xframe_options_exempt
def GroziitFromview(request):
    if not logged_in(request):
        try:
            data = request.GET["data"]
            fernet = Fernet(iframe)
            data = fernet.decrypt(data.encode()).decode()

            email, password = data.split("~")

            profile = Profiles.objects.get(email=email)

            if not payment_check(request, id=profile.subscriber_id, email=email):
                raise Exception

            if profile.subscriber == False:
                raise Exception

            fernet = Fernet(profile.key.encode('utf-8'))

            if (profile.password != fernet.decrypt(password.encode()).decode('utf-8')):
                raise Exception

            if profile.account_type != "Form":
                raise Exception

            form = Jobs.objects.get(id=request.GET['id'], posted_by=email)
            return render(request, "GroziitFromView.html", {"form": form, "msg": message_check(request)})

        except Exception as e:
            return HttpResponseRedirect('404')
    form = Jobs.objects.get(id=request.GET['id'], posted_by=request.session['email'])
    # job.time = tim
    return render(request, "GroziitFromView.html", {"form": form, "msg": message_check(request)})

@xframe_options_exempt
def GroziitImageview(request):
    if not logged_in(request):
        try:
            data = request.GET["data"]
            fernet = Fernet(iframe)
            data = fernet.decrypt(data.encode()).decode()

            email, password = data.split("~")

            profile = Profiles.objects.get(email=email)

            if not payment_check(request, id=profile.subscriber_id, email=email):
                raise Exception

            if profile.subscriber == False:
                raise Exception

            fernet = Fernet(profile.key.encode('utf-8'))

            if (profile.password != fernet.decrypt(password.encode()).decode('utf-8')):
                raise Exception

            if profile.account_type != "Form":
                raise Exception

            images = Jobs.objects.get(id=request.GET['id'], posted_by=email)
            return render(request, "GroziitImageview.html", {"images": images.description.split(','), "msg": message_check(request)})

        except Exception as e:
            return HttpResponseRedirect('404')
    images = Jobs.objects.get(id=request.GET['id'], posted_by=request.session['email'])
    return render(request, "GroziitImageview.html", {"images": images.description.split(','), "msg": message_check(request)})


def pages_login(request):
    return render(request, "pages-login.html", {"msg": message_check(request)})


def pages_register(request):
    return render(request, "pages-register.html", {"msg": message_check(request)})


def users_profile(request):
    if not logged_in(request):
        return HttpResponseRedirect('pages-login')

    fernet = Fernet(iframe)
    iframe_data = request.session["email"] + "~" + request.session["password"]
    iframe_data = fernet.encrypt(iframe_data.encode()).decode('utf-8')
    profile = Profiles.objects.get(email=request.session['email'])

    quantities = {
        "Job" : 2,
        "Form" : 2,
        "E-Commerce" : 3,
        "Images": 2
    }

    return render(request, "users-profile.html",
                  {"msg": message_check(request), "profile": profile,
                   'username': profile.username, 'role': profile.job,
                   "pp": profile.img_url, "iframe": iframe_data, "actype": profile.account_type,"quantity":quantities[profile.account_type]})


def cancelsub(request):
    if not logged_in(request):
        return HttpResponseRedirect('pages-login')
    try:
        user = Profiles.objects.get(email=request.session['email'])

        headers = {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer ' + get_access_token(),
        }

        json_data = {
            'reason': 'NA',
        }

        response = requests.post(
            'https://api-m.paypal.com/v1/billing/subscriptions/' + user.subscriber_id + '/cancel',
            headers=headers,
            json=json_data,
        )

        # print(user.subscriber_id)
        # print(response.status_code)

        if response.status_code != 204:
            raise Exception

        user.subscriber = False
        user.subscriber_id = ""
        user.save()

        request.session[
            'message'] = '<b> <i class="bi bi-check-circle-fill" style="color: green"></i> Successfully cancelled Subscription</b>'
        return HttpResponseRedirect("users-profile")

    except Exception as e:
        print(e)
        request.session[
            'message'] = '<b> <i class="bi bi-x-circle-fill" style="color: red"></i> There is an error cancelling the Subscription<br>Please try again or Contact us</b>'
        return HttpResponseRedirect("users-profile")


def edit_profile(request):
    if not logged_in(request):
        return HttpResponseRedirect('pages-login')
    try:
        profile = Profiles.objects.get(email=request.session["email"])
        profile.username = request.POST['username']
        profile.job = request.POST['job']
        profile.company = request.POST['company']
        profile.save()
        request.session[
            'message'] = '<b> <i class="bi bi-check-circle-fill" style="color: green"></i> Changes made Successfully !</b>'
        return HttpResponseRedirect('users-profile')
    except Exception as e:
        print(e)
        request.session[
            'message'] = '<b> <i class="bi bi-x-circle-fill" style="color: red"></i> There is an error changing your details<br>Please try again or Contact us</b>'
        return HttpResponseRedirect(request, "users-profile")


def change_password(request):
    if not logged_in(request):
        return HttpResponseRedirect('pages-login')
    try:
        profile = Profiles.objects.get(email=request.session["email"])
        profile.password = request.POST['newpassword']
        profile.save()
        request.session[
            'message'] = '<b> <i class="bi bi-check-circle-fill" style="color: green"></i> Successfully change account password!</b>'
        return HttpResponseRedirect('users-profile')
    except Exception as e:
        print(e)
        request.session[
            'message'] = '<b> <i class="bi bi-x-circle-fill" style="color: red"></i> There is an error changing password<br>Please try again or Contact us</b>'
        return HttpResponseRedirect(request, "users-profile")

@xframe_options_exempt
@csrf_exempt
def dynamicspace_form(request):
    try:
        email = ""
        if not logged_in(request):
            data = request.GET["data"]
            fernet = Fernet(iframe)
            data = fernet.decrypt(data.encode()).decode()

            email, password = data.split("~")

            profile = Profiles.objects.get(email=email)

            if not payment_check(request, id=profile.subscriber_id, email=email):
                raise Exception

            if profile.subscriber == False:
                raise Exception

            fernet = Fernet(profile.key.encode('utf-8'))

            if (profile.password != fernet.decrypt(password.encode()).decode('utf-8')):
                raise Exception
        else:
            email = request.session['email']

        profile = Profiles.objects.get(email=email)
        POSTdata = ""
        for i in request.POST.items():
            if i[0] in ["csrfmiddlewaretoken","formname"]: continue
            POSTdata += "<b>" + i[0].capitalize() + "</b>:" + i[1] + "<br>"

        if profile.account_type == "Job":
            job = Jobs.objects.get(id=request.POST['jobid'])
            application = JobApplication()
            application.job = job
            application.name = request.POST['name']
            application.email = request.POST['email']
            application.address = request.POST['address']
            timestamp = str(int(time.time() * 1000))
            file = request.FILES['resume']

            if (file.size / (1024 * 1024) > 2) or (not file.name.endswith((".pdf", ".doc", ".docx"))):
                request.session[
                    'message'] = f'<b> <i class="bi bi-x-circle-fill" style="color: red"></i>Please Upload a valid file.</b>'
                return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

            file_name = timestamp + "_" + file.name
            s3_client.upload_fileobj(file, 'dynamic-spaces-resumes',f'{profile.company.lower()}/{file_name}')
            application.resume_link = f"https://dynamic-spaces-resumes.s3.amazonaws.com/{profile.company.lower()}/{file_name}"
            application.save()
            employee = f'''

                        <body>
                            <table class="email-wrapper" width="100%" cellpadding="0" cellspacing="0" role="presentation">
                                <tr>
                                    <td align="center">
                                        <table class="email-content" width="100%" cellpadding="0" cellspacing="0" role="presentation">
                                            <tr>
                                                <td class="email-masthead">
                                                    <a href="" class="f-fallback email-masthead_name">
                                                        <img src="{job.logo_img_url}" width="auto" style="max-width:300px" />
                                                    </a>
                                                </td>
                                            </tr>
                                            <!-- Email Body -->
                                            <tr>
                                                <td class="email-body" width="100%" cellpadding="0" cellspacing="0">
                                                    <table class="email-body_inner" align="center" width="570" cellpadding="0" cellspacing="0"
                                                        role="presentation">
                                                        <!-- Body content -->
                                                        <tr>
                                                            <td class="content-cell">
                                                                <div class="f-fallback">
                                                                    <h1>Hello {request.POST['name']},</h1>
                                                                    <p>Application acknowledgment for {job.title} at {job.company}</p>
                                                                    <!-- Action -->
                                                                    <table class="attributes" width="100%" cellpadding="0" cellspacing="0"
                                                                        role="presentation">
                                                                        <tr>
                                                                            <td class="attributes_content">
                                                                                <table width="100%" cellpadding="0" cellspacing="0"
                                                                                    role="presentation">
                                                                                    <tr>
                                                                                        <td class="attributes_item">
                                                                                            Thank you for providing the information. This mail is an acknowledgement that we have received your data.
                                                                                        </td>
                                                                                    </tr>

                                                                                </table>
                                                                            </td>
                                                                        </tr>
                                                                    </table>

                                                                    <p>If you have any questions, feel free to <a
                                                                            href="mailto:{job.eemail}">Contact the mail address of the
                                                                            sender</a>. (Click on the link to contact)</p>
                                                                    <p>Thanks,
                                                                        <br>Team {job.company}
                                                                    </p>

                                                                    <!-- Sub copy -->
                                                                    <table class="body-sub" role="presentation" align="center">
                                                                        <tr>
                                                                            <td align="center">
                                                                                <p class="f-fallback sub"><strong>Mail generated by </strong><a
                                                                                        href="https://groziit.com"><img
                                                                                            src="https://i.imgur.com/OUzZa5Z.png"
                                                                                            style="width: 60px;" /></a></p>

                                                                            </td>
                                                                        </tr>
                                                                    </table>
                                                                </div>
                                                            </td>
                                                        </tr>
                                                    </table>
                                                </td>
                                            </tr>
                                            <tr>
                                                <td>
                                                    <table class="email-footer" align="center" width="570" cellpadding="0" cellspacing="0"
                                                        role="presentation">
                                                        <tr>
                                                            <td class="content-cell" align="center">
                                                                <p class="f-fallback sub align-center">&copy; Copyright {job.company}. All Rights
                                                                    Reserved</p>

                                                            </td>
                                                        </tr>
                                                    </table>
                                                </td>
                                            </tr>
                                        </table>
                                    </td>
                                </tr>
                            </table>
                        </body>

                        </html>'''
            employer = f'''<body>
                        <table class="email-wrapper" width="100%" cellpadding="0" cellspacing="0" role="presentation">
                            <tr>
                                <td align="center">
                                    <table class="email-content" width="100%" cellpadding="0" cellspacing="0" role="presentation">
                                        <tr>
                                            <td class="email-masthead">
                                                <a href="{request.META.get('HTTP_REFERER')}" class="f-fallback email-masthead_name">
                                                    <img src="{job.logo_img_url}" width="auto" style="max-width:300px"/>
                                                </a>
                                            </td>
                                        </tr>
                                        <!-- Email Body -->
                                        <tr>
                                            <td class="email-body" width="100%" cellpadding="0" cellspacing="0">
                                                <table class="email-body_inner" align="center" width="570" cellpadding="0" cellspacing="0"
                                                    role="presentation">
                                                    <!-- Body content -->
                                                    <tr>
                                                        <td class="content-cell">
                                                            <div class="f-fallback">
                                                                <h1>Welcome, {job.company}</h1>
                                                                <p>New Job Application submitted for for {job.title} at {job.company}</p>
                                                                <!-- Action -->
                                                                <table class="attributes" width="100%" cellpadding="0" cellspacing="0"
                                                                    role="presentation">
                                                                    <tr>
                                                                        <td class="attributes_content">
                                                                            <table width="100%" cellpadding="0" cellspacing="0"
                                                                                role="presentation">
                                                                                <tr>
                                                                                    <td class="attributes_item">
                                                                                        <span class="f-fallback">
                                                                                        {POSTdata} <br/>
                                                                                        <strong>Resume Link:</strong> {application.resume_link}
                                                                                        </span>
                                                                                    </td>
                                                                                </tr>

                                                                            </table>
                                                                        </td>
                                                                    </tr>
                                                                </table>

                                                                <table class="body-action" align="center" width="100%" cellpadding="0"
                                                                    cellspacing="0" role="presentation">
                                                                    <tr>
                                                                        <td align="center">
                                                                            <!-- Border based button
                               https://litmus.com/blog/a-guide-to-bulletproof-buttons-in-email-design -->
                                                                            <table width="100%" border="0" cellspacing="0" cellpadding="0"
                                                                                role="presentation">
                                                                                <tr>
                                                                                    <td align="center">
                                                                                        <a href="{request.META.get('HTTP_REFERER')}"
                                                                                            class="f-fallback button" target="_blank">Visit
                                                                                            Website</a>
                                                                                    </td>
                                                                                </tr>
                                                                            </table>
                                                                        </td>
                                                                    </tr>
                                                                </table>

                                                                <p>If you have any questions, feel free to <a
                                                                        href="mailto:contact@groziit.com">Contact the mail address of the
                                                                        sender</a>. (Click on the link to contact)</p>
                                                                <p>Thanks,
                                                                    <br>Team GROZiiT
                                                                </p>

                                                                <!-- Sub copy -->
                                                                <table class="body-sub" role="presentation" align="center">
                                                                    <tr>
                                                                        <td align="center">
                                                                            <p class="f-fallback sub"><strong>Mail generated by </strong><a
                                                                                    href="https://groziit.com"><img
                                                                                        src="https://i.imgur.com/OUzZa5Z.png"
                                                                                        style="width: 60px;" /></a></p>

                                                                        </td>
                                                                    </tr>
                                                                </table>
                                                            </div>
                                                        </td>
                                                    </tr>
                                                </table>
                                            </td>
                                        </tr>
                                        <tr>
                                            <td>
                                                <table class="email-footer" align="center" width="570" cellpadding="0" cellspacing="0"
                                                    role="presentation">
                                                    <tr>
                                                        <td class="content-cell" align="center">
                                                            <p class="f-fallback sub align-center">&copy; Copyright GROZiiT. All Rights
                                                                Reserved</p>

                                                        </td>
                                                    </tr>
                                                </table>
                                            </td>
                                        </tr>
                                    </table>
                                </td>
                            </tr>
                        </table>
                    </body>

                    </html>'''

            send_mail(
                subject='Thanks for Applying',
                html_message=message1 + employee,
                message=strip_tags(message1 + employee),
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[request.POST['email'].lower()])
            send_mail(
                subject='New job Application submitted',
                html_message=message1 + employer,
                message=strip_tags(message1 + employer),
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[job.eemail.lower()])

        if profile.account_type == "Form":
            print(request.POST['formname'])
            data = FormData()
            data.data = POSTdata
            data.posted_for = email
            data.form_name = request.POST['formname']
            # print(request.POST['formname'], request.POST['phone_number'])
            #TODO: make the below message generic
            headers = {
                'Content-Type': 'application/json',
                'Authorization': 'Hk3IqZ3crESzStZOh3wfdlKLrta4K3R',
            }
            json_data = {
                 'message': "🎉 Thank you for enrolling to Sitara Grand's opening deals. Get a chance to win any one of the deal listed in our website.",
                 'name': "Sitara Grand",
                 'branch': "25691 Smotherman Rd, Suit No:220, Frisco, Texas -75034",
                 'number': request.POST['Phone Number'],
            }
            response = requests.post(
                'https://revuesmart.herokuapp.com/users/message',
                headers=headers,
                json=json_data,
            )
            print(response.text, "response")
            if(response.text == "sent"):
                data.save()
            else:
                raise Exception
        #     # Get the file from the request
        #     file = request.FILES['files']
        #
        #     # Upload the file to Google Drive
        #     storage = GoogleDriveStorage()
        #     file_path = storage.save(file.name, file)
        #
        #     # Get the link to the file in Google Drive
        #     file_url = storage.url(file_path)

        # print(file_url)
        request.session[
            'message'] = f'<b> <i class="bi bi-check-circle-fill" style="color: green"></i> Successfully submitted the {profile.account_type} Application!</b>'
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


    except Exception as e:
        print(e)
        request.session[
            'message'] = f'<b> <i class="bi bi-x-circle-fill" style="color: red"></i>There is an error submitting the {profile.account_type}<br>Please try again!!</b>'
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

@xframe_options_exempt
@csrf_exempt
def integrations_form(request,id,integration_id):
    try:
        email = ""
        if not logged_in(request):
            data = request.GET["data"]
            fernet = Fernet(iframe)
            data = fernet.decrypt(data.encode()).decode()

            email, password = data.split("~")

            profile = Profiles.objects.get(email=email)

            if not payment_check(request, id=profile.subscriber_id, email=email):
                raise Exception

            if profile.subscriber == False:
                raise Exception

            fernet = Fernet(profile.key.encode('utf-8'))

            if (profile.password != fernet.decrypt(password.encode()).decode('utf-8')):
                raise Exception
        else:
            email = request.session['email']

        profile = Profiles.objects.get(email=email)
        POSTdata = ""
        for i in request.POST.items():
            if i[0] in ["csrfmiddlewaretoken","formname"]: continue
            POSTdata += "<b>" + i[0].capitalize() + "</b>:" + i[1] + "<br>"

        if profile.account_type == "Job":
            integration = AccountIntegrations.objects.get(account=email, integration_id=integration_id)

            authentication_link, jobs_list_link, job_details_link, posted_by_link = integration.integration.links.split(
                ",")[:4]

            access_token = check_integration_credentials(authentication_link,
                                                         integration.email,
                                                         integration.password,
                                                         integration.api_key)['access_token']

            headers = {
                'Content-Type': 'application/json',
                'accept': 'application/json',
                'Authorization': f'Bearer {access_token}'
            }

            job_details = requests.request("GET", job_details_link + id, headers=headers).json()

            posted_by = requests.request("GET", posted_by_link + job_details.get('posted_by'), headers=headers).json().get(
                'email_id')

            application = IntegrationJobApplication()
            application.title = job_details.get('position_title')
            application.eemail = posted_by
            application.name = request.POST['name']
            application.email = request.POST['email']
            application.posted_by = email
            timestamp = str(int(time.time() * 1000))
            file = request.FILES['resume']

            if (file.size / (1024 * 1024) > 2) or (not file.name.endswith((".pdf", ".doc", ".docx"))):
                request.session[
                    'message'] = f'<b> <i class="bi bi-x-circle-fill" style="color: red"></i>Please Upload a valid file.</b>'
                return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

            file_name = timestamp + "_" + file.name
            s3_client.upload_fileobj(file, 'dynamic-spaces-resumes',f'{profile.company.lower()}/{file_name}')
            application.resume_link = f"https://dynamic-spaces-resumes.s3.amazonaws.com/{profile.company.lower()}/{file_name}"
            application.save()
            employee = f'''

                        <body>
                            <table class="email-wrapper" width="100%" cellpadding="0" cellspacing="0" role="presentation">
                                <tr>
                                    <td align="center">
                                        <table class="email-content" width="100%" cellpadding="0" cellspacing="0" role="presentation">
                                            <!-- Email Body -->
                                            <tr>
                                                <td class="email-body" width="100%" cellpadding="0" cellspacing="0">
                                                    <table class="email-body_inner" align="center" width="570" cellpadding="0" cellspacing="0"
                                                        role="presentation">
                                                        <!-- Body content -->
                                                        <tr>
                                                            <td class="content-cell">
                                                                <div class="f-fallback">
                                                                    <h1>Hello {request.POST['name']},</h1>
                                                                    <p>Application acknowledgment for {job_details.get('position_title')} at {profile.company}</p>
                                                                    <!-- Action -->
                                                                    <table class="attributes" width="100%" cellpadding="0" cellspacing="0"
                                                                        role="presentation">
                                                                        <tr>
                                                                            <td class="attributes_content">
                                                                                <table width="100%" cellpadding="0" cellspacing="0"
                                                                                    role="presentation">
                                                                                    <tr>
                                                                                        <td class="attributes_item">
                                                                                            Thank you for providing the information. This mail is an acknowledgement that we have received your data.
                                                                                        </td>
                                                                                    </tr>

                                                                                </table>
                                                                            </td>
                                                                        </tr>
                                                                    </table>

                                                                    <p>If you have any questions, feel free to <a
                                                                            href="mailto:{posted_by}">Contact the mail address of the
                                                                            sender</a>. (Click on the link to contact)</p>
                                                                    <p>Thanks,
                                                                        <br>Team {profile.company}
                                                                    </p>

                                                                    <!-- Sub copy -->
                                                                    <table class="body-sub" role="presentation" align="center">
                                                                        <tr>
                                                                            <td align="center">
                                                                                <p class="f-fallback sub"><strong>Mail generated by </strong><a
                                                                                        href="https://groziit.com"><img
                                                                                            src="https://i.imgur.com/OUzZa5Z.png"
                                                                                            style="width: 60px;" /></a></p>

                                                                            </td>
                                                                        </tr>
                                                                    </table>
                                                                </div>
                                                            </td>
                                                        </tr>
                                                    </table>
                                                </td>
                                            </tr>
                                            <tr>
                                                <td>
                                                    <table class="email-footer" align="center" width="570" cellpadding="0" cellspacing="0"
                                                        role="presentation">
                                                        <tr>
                                                            <td class="content-cell" align="center">
                                                                <p class="f-fallback sub align-center">&copy; Copyright {profile.company}. All Rights
                                                                    Reserved</p>

                                                            </td>
                                                        </tr>
                                                    </table>
                                                </td>
                                            </tr>
                                        </table>
                                    </td>
                                </tr>
                            </table>
                        </body>

                        </html>'''
            employer = f'''<body>
                        <table class="email-wrapper" width="100%" cellpadding="0" cellspacing="0" role="presentation">
                            <tr>
                                <td align="center">
                                    <table class="email-content" width="100%" cellpadding="0" cellspacing="0" role="presentation">
                    
                                        <!-- Email Body -->
                                        <tr>
                                            <td class="email-body" width="100%" cellpadding="0" cellspacing="0">
                                                <table class="email-body_inner" align="center" width="570" cellpadding="0" cellspacing="0"
                                                    role="presentation">
                                                    <!-- Body content -->
                                                    <tr>
                                                        <td class="content-cell">
                                                            <div class="f-fallback">
                                                                <h1>Welcome, {profile.company}</h1>
                                                                <p>New Job Application submitted for for {job_details.get('position_title')} at {profile.company}</p>
                                                                <!-- Action -->
                                                                <table class="attributes" width="100%" cellpadding="0" cellspacing="0"
                                                                    role="presentation">
                                                                    <tr>
                                                                        <td class="attributes_content">
                                                                            <table width="100%" cellpadding="0" cellspacing="0"
                                                                                role="presentation">
                                                                                <tr>
                                                                                    <td class="attributes_item">
                                                                                        <span class="f-fallback">
                                                                                        {POSTdata} <br/>
                                                                                        <strong>Resume Link:</strong> {application.resume_link}
                                                                                        </span>
                                                                                    </td>
                                                                                </tr>

                                                                            </table>
                                                                        </td>
                                                                    </tr>
                                                                </table>

                                                                <table class="body-action" align="center" width="100%" cellpadding="0"
                                                                    cellspacing="0" role="presentation">
                                                                    <tr>
                                                                        <td align="center">
                                                                            <!-- Border based button
                               https://litmus.com/blog/a-guide-to-bulletproof-buttons-in-email-design -->
                                                                            <table width="100%" border="0" cellspacing="0" cellpadding="0"
                                                                                role="presentation">
                                                                                <tr>
                                                                                    <td align="center">
                                                                                        <a href="{request.META.get('HTTP_REFERER')}"
                                                                                            class="f-fallback button" target="_blank">Visit
                                                                                            Website</a>
                                                                                    </td>
                                                                                </tr>
                                                                            </table>
                                                                        </td>
                                                                    </tr>
                                                                </table>

                                                                <p>If you have any questions, feel free to <a
                                                                        href="mailto:contact@groziit.com">Contact the mail address of the
                                                                        sender</a>. (Click on the link to contact)</p>
                                                                <p>Thanks,
                                                                    <br>Team GROZiiT
                                                                </p>

                                                                <!-- Sub copy -->
                                                                <table class="body-sub" role="presentation" align="center">
                                                                    <tr>
                                                                        <td align="center">
                                                                            <p class="f-fallback sub"><strong>Mail generated by </strong><a
                                                                                    href="https://groziit.com"><img
                                                                                        src="https://i.imgur.com/OUzZa5Z.png"
                                                                                        style="width: 60px;" /></a></p>

                                                                        </td>
                                                                    </tr>
                                                                </table>
                                                            </div>
                                                        </td>
                                                    </tr>
                                                </table>
                                            </td>
                                        </tr>
                                        <tr>
                                            <td>
                                                <table class="email-footer" align="center" width="570" cellpadding="0" cellspacing="0"
                                                    role="presentation">
                                                    <tr>
                                                        <td class="content-cell" align="center">
                                                            <p class="f-fallback sub align-center">&copy; Copyright GROZiiT. All Rights
                                                                Reserved</p>

                                                        </td>
                                                    </tr>
                                                </table>
                                            </td>
                                        </tr>
                                    </table>
                                </td>
                            </tr>
                        </table>
                    </body>

                    </html>'''

            send_mail(
                subject='Thanks for Applying',
                html_message=message1 + employee,
                message=strip_tags(message1 + employee),
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[request.POST['email'].lower()])
            send_mail(
                subject='New job Application submitted',
                html_message=message1 + employer,
                message=strip_tags(message1 + employer),
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[request.POST['email'].lower()])

            request.session[
                'message'] = f'<b> <i class="bi bi-check-circle-fill" style="color: green"></i> Successfully submitted the {profile.account_type} Application!</b>'
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

    except Exception as e:
        print(e)
        request.session[
            'message'] = f'<b> <i class="bi bi-x-circle-fill" style="color: red"></i>There is an error submitting the {profile.account_type}<br>Please try again!!</b>'
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def pages_contact(request):
    if not logged_in(request):
        return HttpResponseRedirect('pages-login')
    profile = Profiles.objects.get(email=request.session['email'])
    return render(request, "pages-contact.html", {"msg": message_check(request), "profile": profile,
                                                  'username': profile.username, 'role': profile.job,
                                                  "pp": profile.img_url, "actype": profile.account_type})


def GroziitApplicationsView(request):
    if not logged_in(request):
        return HttpResponseRedirect('pages-login')

    profile = Profiles.objects.get(email=request.session['email'])

    job_applications = JobApplication.objects.filter(job__posted_by=profile.email)
    integrated_applications = IntegrationJobApplication.objects.filter(posted_by=profile.email)

    return render(request, "GroziitApplicationsView.html",
                  {'job_applications': job_applications, "integrated_applications":integrated_applications,
                   'username': profile.username, 'role': profile.job,
                   "pp": profile.img_url, "msg": message_check(request), "actype": profile.account_type})

@require_http_methods(["GET", "OPTIONS"])
def GroziitContentAPI(request):
    if request.method == "OPTIONS":
        response = JsonResponse({"status": "OK"})
        response["Access-Control-Allow-Origin"] = "*"
        response["Access-Control-Allow-Methods"] = "GET, OPTIONS"
        response["Access-Control-Allow-Headers"] = "Authorization, Content-Type"
        return response

    content_id = request.GET.get('id')
    if not content_id:
        return JsonResponse({'error': 'ID parameter is missing'}, status=400)

    try:
        content = Content.objects.get(id=content_id)
        if not logged_in(request):
            token = request.headers.get('Authorization')
            if token != f'Token {content.key}':
                return JsonResponse({'error': 'Invalid or missing token'}, status=401)
    except Content.DoesNotExist:
        return JsonResponse({'error': 'Content not found'}, status=404)


    content_data = model_to_dict(content)
    del content_data['posted_by']
    del content_data['id']
    del content_data['key']
    response = JsonResponse(content_data)
    response["Access-Control-Allow-Origin"] = "*"
    return response


def GroziitIntegrations(request):
    if not logged_in(request):
        return HttpResponseRedirect('pages-login')

    try:
        profile = Profiles.objects.get(email=request.session['email'])

        if profile.account_type == "Job":
            integrations = Integration.objects.all()

            account_integrations = AccountIntegrations.objects.filter(account=request.session['email'])

            integrated_status = {}

            for integration in integrations:
                integrated_status[integration] = account_integrations.filter(integration=integration).exists()

        return render(request, "GroziitIntegrationsView.html",
                      {'username': profile.username, 'role': profile.job,"integrations":integrations,
                       "pp": profile.img_url, "msg": message_check(request), "actype": profile.account_type,
                       "integrated_status": integrated_status})
    except Exception as e:
        print(e)
        return HttpResponse("Unauthorized or issue, Please contact admin")

def GroziitIntegrationsDetails(request,id):
    if not logged_in(request):
        return HttpResponseRedirect('pages-login')

    if request.method=="POST":
        try:
            profile = Profiles.objects.get(email=request.session['email'])
            if profile.account_type == "Job":
                integration = Integration.objects.get(id=id)

                try:
                    account_integrations = AccountIntegrations.objects.get(account=request.session['email'],
                                                                           integration=integration)
                except AccountIntegrations.DoesNotExist:
                    account_integrations = AccountIntegrations()
                    account_integrations.integration = integration
                    account_integrations.account = request.session['email']

                if check_integration_credentials(
                        integration.links.split()[0],
                        request.POST["email"],
                        request.POST["password"],
                        request.POST["key"]):
                    account_integrations.email = request.POST["email"]
                    account_integrations.password = request.POST["password"]
                    account_integrations.api_key = request.POST["key"]
                    account_integrations.save()
                    request.session[
                        'message'] = f'<b> <i class="bi bi-check-circle-fill" style="color: green"></i> Successfully submitted Integration Details!</b>'
                    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
                else:
                    request.session[
                        'message'] = f'<b> <i class="bi bi-x-circle-fill" style="color: red"></i>Entered Invalid Credentials<br>Please try again!!</b>'
                    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        except Exception as e:
            print(e)
            request.session[
                'message'] = f'<b> <i class="bi bi-x-circle-fill" style="color: red"></i>There is an error with integration<br>Please try again!!</b>'
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


    try:
        profile = Profiles.objects.get(email=request.session['email'])

        if profile.account_type == "Job":
            integration = Integration.objects.get(id=id)

            try:
                account_integrations = AccountIntegrations.objects.get(account=request.session['email'],integration=integration)
            except AccountIntegrations.DoesNotExist:
                account_integrations = None

        return render(request, "GroziitIntegrationsViewDetails.html",
                      {'username': profile.username, 'role': profile.job, "integration":integration,
                       "pp": profile.img_url, "msg": message_check(request), "actype": profile.account_type,
                       "account_integrations": account_integrations})
    except Exception as e:
        print(e)
        return HttpResponse("Unauthorized or issue, Please contact admin")


def test(request):
    return render(request,"test.html")
