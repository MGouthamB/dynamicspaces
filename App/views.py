import json

from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render
from .models import *
from cryptography.fernet import Fernet
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
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
        form_data.preview = form_data.data.split("<br><b>")[0].split("<br>")[1]


    return render(request, "index.html",
                  {'jobs': jobs,'datas': datas, 'username': profile.username, 'role': profile.job,
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
    print("helooooo")
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
        user_email = ""
        for i in request.POST.items():
            if i[0] in ["csrfmiddlewaretoken","formname"]: continue
            if i[0] == "email":
                user_email = i[1]
            POSTdata += (
               "<b>" + i[0].capitalize() + "</b>: " + i[1] + "<br>"
            )

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
            send_email('drd_registration.html', "Thank you for your registration!", POSTdata, user_email)
            print(user_email, "sending email to user...")
            data.save()
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
            POSTdata += "<b>" + i[0].capitalize() + "</b>: <br/>" + i[1] + "<br>"

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

# Blog rendering function
@require_http_methods(["GET", "OPTIONS"])
def getBlog(request, slug, id):
    print(slug, id)
    if request.method == "OPTIONS":
        response = JsonResponse({"status": "OK"})
        response["Access-Control-Allow-Origin"] = "*"
        response["Access-Control-Allow-Methods"] = "GET, OPTIONS"
        response["Access-Control-Allow-Headers"] = "Authorization, Content-Type"
        return response

    blog = '''
        <!DOCTYPE html>
        <html lang="en">
        
        <head>
            <meta charset="UTF-8" />
            <meta name="viewport" content="width=device-width, initial-scale=1.0" />
            <title>Vexon || Blog Details Standard</title>
        
            <!--=====FAB ICON=======-->
        
            <!--=====CSS=======-->
        
        
            <!--=====JQUERY=======-->
        </head>
        
        <body>
            <!--===== BLOG DETAILS AREA START=======-->
            <div class="blog-details1-all sp">
                <div class="container">
                    <div class="row">
                        <div class="col-lg-12">
                            <div class="blog-page3-single-box">
                                <div class="heading1">
                                    <div class="social-area mb-16">
                                        <div class="author-area">
                                            <div class="author">
                                                <div class="author-tumb">
                                                    <img src="https://i.imgur.com/wg61NBf.png" alt="vexon" />
                                                </div>
                                                <a href="author.html" class="author-text">Kimberly Mastrangelo</a>
                                            </div>
                                            <div class="date">
                                                <a href="#"><svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-calendar3" viewBox="0 0 16 16">
          <path d="M14 0H2a2 2 0 0 0-2 2v12a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V2a2 2 0 0 0-2-2M1 3.857C1 3.384 1.448 3 2 3h12c.552 0 1 .384 1 .857v10.286c0 .473-.448.857-1 .857H2c-.552 0-1-.384-1-.857z"/>
          <path d="M6.5 7a1 1 0 1 0 0-2 1 1 0 0 0 0 2m3 0a1 1 0 1 0 0-2 1 1 0 0 0 0 2m3 0a1 1 0 1 0 0-2 1 1 0 0 0 0 2m-9 3a1 1 0 1 0 0-2 1 1 0 0 0 0 2m3 0a1 1 0 1 0 0-2 1 1 0 0 0 0 2m3 0a1 1 0 1 0 0-2 1 1 0 0 0 0 2m3 0a1 1 0 1 0 0-2 1 1 0 0 0 0 2m-9 3a1 1 0 1 0 0-2 1 1 0 0 0 0 2m3 0a1 1 0 1 0 0-2 1 1 0 0 0 0 2m3 0a1 1 0 1 0 0-2 1 1 0 0 0 0 2"/>
        </svg> Oct 26, 2024 </a>
                                            </div>
                                        </div>
                                        <a href="categories.html" class="time"><svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-clock" viewBox="0 0 16 16">
          <path d="M8 3.5a.5.5 0 0 0-1 0V9a.5.5 0 0 0 .252.434l3.5 2a.5.5 0 0 0 .496-.868L8 8.71z"/>
          <path d="M8 16A8 8 0 1 0 8 0a8 8 0 0 0 0 16m7-8A7 7 0 1 1 1 8a7 7 0 0 1 14 0"/>
        </svg> 3 min read</a>
                                    </div>
                                    <h2>The Art of Building a Strong Personal Brand on Social Media</h2>
                                    <p class="mt-16">In today’s digital age, building a strong personal brand on social media is more crucial than ever. A compelling personal brand not only establishes your credibility and trustworthiness but also opens doors to new opportunities, connects you with like-minded individuals,</p>
                                </div>
        
                                <div class="thumbnail image-anime _relative mt-20">
                                    <img src="https://vexon-html-demo.vercel.app/assets/img/blog/blog-details-image1.png" alt="vexon" />
                                </div>
                            </div>
                        </div>
                    </div>
        
                    <div class="row">
                        <div class="col-lg-8">
                            <div class="details content-area mt-40">
                                <article>
                                    <div class="heading1">
                                        <p>In today’s digital age, building a strong personal brand on social media is more crucial than ever. A compelling personal brand not only establishes your credibility and trustworthiness but also opens doors to new opportunities, connects you with like-minded individuals, and can even generate income. With billions of users on social media platforms, carving out a unique space for yourself may seem daunting, but with the right strategies, you can create a brand that resonates.</p>
                                        <h3 class="mt-40">Understanding Your Personal Brand</h3>
                                        <p class="mt-16">Your personal brand is a reflection of who you are, what you stand for, and how you want others to perceive you. Before diving into the social media world, take some time to reflect on your values, interests, and goals. Ask yourself: What do I want to be known for? What are my unique strengths and passions? Who is my target audience?</p>
                                        <p class="mt-16">Once you have clarity on these questions, you can begin crafting a brand that authentically represents you. Remember, authenticity is key—people connect with genuine voices, so stay true to who you are and avoid the temptation to imitate others.</p>
                                    </div>
                                </article>
        
                                <article>
                                    <div class="heading1 mt-40">
                                        <h3>Choosing the Right Platforms</h3>
                                        <p class="mt-16">Different social media platforms serve different purposes, and each has its own user demographics. Selecting the right platforms for your brand is essential. For instance:</p>
                                        <p class="mt-16 p-with-sapn"><span>LinkedIn:</span> is ideal for professionals seeking to build a network within their industry.</p>
                                        <p class="mt-10 p-with-sapn"><span>Instagram:</span> is highly visual and works well for brands related to lifestyle, fashion, travel, and more.</p>
                                        <p class="mt-10 p-with-sapn"><span>Twitter:</span> is great for sharing quick thoughts, opinions, and joining conversations on trending topics.</p>
                                        <p class="mt-10 p-with-sapn"><span>TikTok:</span> has a young, highly engaged audience and is excellent for creating entertaining, relatable short videos.</p>
                                        <p class="mt-20">Choose platforms that align with your goals and where your target audience is most active. Instead of spreading yourself too thin across all platforms, focus on two or three and consistently deliver quality content.</p>
                                    </div>
                                </article>
        
                                <article>
                                    <div class="heading1 mt-50">
                                        <h3>Crafting a Consistent Brand Image</h3>
                                        <p class="mt-16">Your brand image is a combination of your visuals, tone, and messaging. Consistency across your profile photos, color scheme, and typography helps establish a memorable and professional look. Choose profile and cover photos that reflect your personality and niche.</p>
                                        <p class="mt-16">Beyond visuals, consider the tone and style of your posts. Are you aiming for a formal, professional voice or a casual, friendly vibe? Having a consistent tone helps your audience feel connected and fosters trust. Remember, consistency is not only about posting frequently but also about aligning your visuals, voice, and message.</p>
                                        <div class="row">
                                            <div class="col-md-6">
                                                <div class="image _relative image-anime mt-40">
                                                    <img class="w-full" src="assets/img/blog/blog-details-image2.png" alt="vexon" />
                                                </div>
                                            </div>
                                            <div class="col-md-6">
                                                <div class="image _relative image-anime mt-40">
                                                    <img class="w-full" src="assets/img/blog/blog-details-image3.png" alt="vexon" />
                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                </article>
        
                                <article>
                                    <div class="heading1 mt-40">
                                        <h3>Creating Valuable Content</h3>
                                        <p class="mt-16">Content is the heart of personal branding on social media. To build a loyal audience, your content should educate, inspire, or entertain. Start by creating a content calendar and brainstorming ideas that align with your brand’s message. Here are some types of content to consider:</p>
                                        <p class="mt-16 p-with-sapn"><span>Educational Content:</span> Share insights, tips, or tutorials related to your expertise. Position yourself as a thought leader by delivering value.</p>
                                        <p class="mt-10 p-with-sapn"><span>Behind-the-Scenes:</span> Give a glimpse into your life or work process. This humanizes your brand and makes you more relatable.</p>
                                        <p class="mt-10 p-with-sapn"><span>Storytelling:</span> Use stories to connect emotionally with your audience. Share experiences, challenges, or milestones that have shaped your journey.</p>
                                        <p class="mt-10 p-with-sapn"><span>User Engagement:</span> Ask questions, create polls, or invite followers to share their experiences. This not only increases engagement but also strengthens your community.</p>
                                        <p class="mt-20">Plan a mix of these content types to keep your feed dynamic and engaging, and always remember to provide value.</p>
                                    </div>
                                </article>
        
                                <article>
                                    <div class="heading1 mt-50">
                                        <h3>Leveraging Hashtags and Keywords</h3>
                                        <p class="mt-16">Hashtags and keywords can dramatically improve the visibility of your content. Research popular and relevant hashtags in your niche and incorporate them into your posts. On platforms like Instagram and LinkedIn, hashtags help your content reach users who don’t follow you yet. However, avoid overloading your posts with too many hashtags—5-10 carefully selected ones are usually enough.</p>
                                        <p class="mt-20">Using keywords effectively in your profile and posts can also enhance discoverability, especially on platforms with search functions like LinkedIn and Twitter. Think of words and phrases your audience might use to find information in your niche, and strategically incorporate them into your bio, captions, and content.</p>
        
                                        <h3 class="mt-40">Staying Authentic and True to Your Brand</h3>
                                        <p class="mt-16">Finally, one of the most important aspects of personal branding is authenticity. Your audience can tell when you’re genuine and when you’re not, and they’re more likely to engage with a brand that feels real. Be transparent about your journey, share your wins and losses, and let your true personality shine through. Authenticity fosters trust, which is the foundation of any strong brand.</p>
                                        <p class="mt-16">As you grow, you may face pressure to conform to trends or present a certain image. Resist the urge to compromise on your values or misrepresent yourself. A strong personal brand is built on honesty, consistency, and the courage to be yourself.</p>
                                    </div>
                                </article>
        
                            </div>
                        </div>
        
                        <div class="col-lg-4">
                            <div class="blog1-sidebar-area mt-40 ml-30 sm:ml-0 md:ml-0 md:mt-30 sm:mt-30">
                                
                                <div class="sidebar-details-widget_1 _author-intro mt-40">
                                    <div class="sidebar-author-thumb text-center">
                                        <img src="assets/img/blog/sidebar-author1.png" alt="vexon" />
                                        <h4>Jerry Helfer</h4>
                                        <div class="heading1">
                                            <p>Whether you’re a tech enthusiast or a business leader, these emerging trends are reshaping the future and offering endless opportunities for growth and creativity.</p>
                                        </div>
                                        <div class="footer-social1">
                                            <ul>
                                                <li>
                                                    <a href="#"><i class="fa-brands fa-facebook-f"></i></a>
                                                </li>
                                                <li>
                                                    <a href="#"><i class="fa-brands fa-linkedin-in"></i></a>
                                                </li>
                                                <li>
                                                    <a href="#"><i class="fa-brands fa-instagram"></i></a>
                                                </li>
                                                <li>
                                                    <a href="#"><i class="fa-regular fa-basketball"></i></a>
                                                </li>
                                                <li>
                                                    <a href="#"><i class="fa-brands fa-behance"></i></a>
                                                </li>
                                            </ul>
                                        </div>
                                    </div>
                                </div>
                                <div class="sidebar-details-widget_1 _recent-posts mt-40">
                                    <h3>Recent Post</h3>
        
                                    <div class="blog1-recent-box">
                                        <div class="">
                                            <div class="recent-thumb">
                                                <img src="assets/img/blog/blog1-recent1.png" alt="vexon" />
                                            </div>
                                        </div>
                                        <div class="heading">
                                            <a href="#" class="date"><img src="assets/img/icons/date1.svg" alt="vexon" /> Oct 13, 2024</a>
                                            <h5><a href="blog-single.html">The Power of Storytelling: How Make Your Brand’s Voice...</a></h5>
                                        </div>
                                    </div>
        
                                    <div class="blog1-recent-box mt-16">
                                        <div class="">
                                            <div class="recent-thumb">
                                                <img src="assets/img/blog/blog1-recent2.png" alt="vexon" />
                                            </div>
                                        </div>
                                        <div class="heading">
                                            <a href="#" class="date"><img src="assets/img/icons/date1.svg" alt="vexon" /> Oct 12, 2024</a>
                                            <h5><a href="blog-single.html">Mastering Content Calendars: A Guide to Consistent Strat...</a></h5>
                                        </div>
                                    </div>
        
                                    <div class="blog1-recent-box mt-16">
                                        <div class="">
                                            <div class="recent-thumb">
                                                <img src="assets/img/blog/blog1-recent3.png" alt="vexon" />
                                            </div>
                                        </div>
                                        <div class="heading">
                                            <a href="#" class="date"><img src="assets/img/icons/date1.svg" alt="vexon" /> Oct 21, 2024</a>
                                            <h5><a href="blog-single.html">Social Media Trends for 2024: What to Watch and How to...</a></h5>
                                        </div>
                                    </div>
        
                                    <div class="blog1-recent-box mt-16">
                                        <div class="">
                                            <div class="recent-thumb">
                                                <img src="assets/img/blog/blog1-recent4.png" alt="vexon" />
                                            </div>
                                        </div>
                                        <div class="heading">
                                            <a href="#" class="date"><img src="assets/img/icons/date1.svg" alt="vexon" /> Oct 19, 2024 </a>
                                            <h5><a href="blog-single.html">Creating a Visual Identity: Tips for Aesthetic & Brand Consi...</a></h5>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        
            <!--===== BLOG DETAILS AREA START=======-->
        
            <!--===== BLOG AREA START=======-->
        
            <div class="details-page-boxs sp bg1">
                <div class="container">
                    <div class="row">
                        <div class="col-lg-6 m-auto text-center">
                            <div class="heading1">
                                <h2>More Blogs</h2>
                            </div>
                        </div>
                    </div>
        
                    <div class="space30"></div>
                    <div class="row">
                        <div class="col-md-6 col-lg-4">
                            <div class="blog1-single-box mt-30">
                                <div class="thumbnail image-anime">
                                    <img src="assets/img/blog/blog1-image6.png" alt="vexon" />
                                </div>
                                <div class="heading1">
                                    <div class="social-area">
                                        <a href="social-media.html" class="social">Brand Consistency</a>
                                        <a href="categories.html" class="time"><img src="assets/img/icons/time1.svg" alt="vexon" /> 3 min read</a>
                                    </div>
                                    <h4><a href="blog-single.html">Creating a Visual Identity: Tips for Aesthetic and Brand Consistency </a></h4>
                                    <p class="mt-16">This post covers tips on color schemes, fonts, and visuals to keep your profile visually appealing and cohesive.</p>
                                    <div class="author-area">
                                        <div class="author">
                                            <div class="author-tumb">
                                                <img src="assets/img/blog/blog1-author5.png" alt="vexon" />
                                            </div>
                                            <a href="author.html" class="author-text">Katie Sims</a>
                                        </div>
                                        <div class="date">
                                            <a href="#"><img src="assets/img/icons/date1.svg" alt="vexon" /> Nov 6, 2024 </a>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
        
                        <div class="col-md-6 col-lg-4">
                            <div class="blog1-single-box mt-30">
                                <div class="thumbnail image-anime">
                                    <img src="assets/img/blog/blog1-image7.png" alt="vexon" />
                                </div>
                                <div class="heading1">
                                    <div class="social-area">
                                        <a href="social-media.html" class="social">Gen - Z</a>
                                        <a href="categories.html" class="time"><img src="assets/img/icons/time1.svg" alt="vexon" /> 3 min read</a>
                                    </div>
                                    <h4><a href="blog-single.html">How to Build Authentic Connections with the New Generation</a></h4>
                                    <p class="mt-16">Gen Z is reshaping digital interaction. Learn what matters to this generation and how to create authentic, meaningful content.</p>
                                    <div class="author-area">
                                        <div class="author">
                                            <div class="author-tumb">
                                                <img src="assets/img/blog/blog1-author5.png" alt="vexon" />
                                            </div>
                                            <a href="author.html" class="author-text">David Elson</a>
                                        </div>
                                        <div class="date">
                                            <a href="#"><img src="assets/img/icons/date1.svg" alt="vexon" /> Oct 26, 2024 </a>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
        
                        <div class="col-md-6 col-lg-4">
                            <div class="blog1-single-box mt-30">
                                <div class="thumbnail image-anime">
                                    <img src="assets/img/blog/blog1-image8.png" alt="vexon" />
                                </div>
                                <div class="heading1">
                                    <div class="social-area">
                                        <a href="social-media.html" class="social">Social Media</a>
                                        <a href="categories.html" class="time"><img src="assets/img/icons/time1.svg" alt="vexon" /> 3 min read</a>
                                    </div>
                                    <h4><a href="blog-single.html">Harnessing Analytics: Using Data to Refine Your Social Media Strategy</a></h4>
                                    <p class="mt-16">Gen Z is reshaping digital interaction. Learn what matters to this generation and how to create authentic, meaningful content.</p>
                                    <div class="author-area">
                                        <div class="author">
                                            <div class="author-tumb">
                                                <img src="assets/img/blog/blog1-author5.png" alt="vexon" />
                                            </div>
                                            <a href="author.html" class="author-text">Kenneth Allen</a>
                                        </div>
                                        <div class="date">
                                            <a href="#"><img src="assets/img/icons/date1.svg" alt="vexon" /> Oct 26, 2024 </a>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        
            <!--===== BLOG AREA START=======-->
        
            <!--===== FOOTER AREA START=======-->
        
            <!--===== FOOTER AREA END=======-->
        
            <!--=== js === -->
        
        </body>
        
        </html>
    '''

    response = JsonResponse({"data": blog})
    response["Access-Control-Allow-Origin"] = "*"
    return response

def send_email(template, subject, data, email):
    html_message = render_to_string(template,
                                    {'user_data': data, 'email': email})

    from_email = settings.DEFAULT_FROM_EMAIL

    email = EmailMessage(subject, html_message, from_email, [email])
    email.extra_headers = {
        'X-Priority': '1',
        'Importance': 'high',
        'List-Unsubscribe': f'<mailto:{settings.DEFAULT_FROM_EMAIL}>',
    }
    email.content_subtype = 'html'
    email.send()

def test(request):
    return render(request,"test.html")
