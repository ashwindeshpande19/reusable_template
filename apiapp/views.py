
import requests
from django.shortcuts import render

def form_view(request):
    response_message = None
    if request.method == 'POST':
        # Hardcoded template ID
        template_id = 'cuddly-weasels-mix-tightly-1717'

        # Collect form data
        data = {
            "template": template_id,  # Use the hardcoded template ID
            "data": {
                "MainTagLineText.text": request.POST.get('MainTagLineText.text'),
                "WebsiteLinkPage1.text": request.POST.get('WebsiteLinkPage1.text'),
                "PhoneNumberPage1.text": request.POST.get('PhoneNumberPage1.text'),
                "CallToAction.text": request.POST.get('CallToAction.text'),
                "qr.value": request.POST.get('qr.value'),
                "Service1.text": request.POST.get('Service1.text'),
                "Service2.text": request.POST.get('Service2.text'),
                "Service3.text": request.POST.get('Service3.text'),
                "Service4.text": request.POST.get('Service4.text'),
                "rating.value": request.POST.get('rating.value'),
                "Coupon1Title.text": request.POST.get('Coupon1Title.text'),
                "Coupon2Title.text": request.POST.get('Coupon2Title.text'),
                "Coupon3Title.text": request.POST.get('Coupon3Title.text'),
                "Coupon1Tag.text": request.POST.get('Coupon1Tag.text'),
                "Coupon2Tag.text": request.POST.get('Coupon2Tag.text'),
                "Coupon3Tag.text": request.POST.get('Coupon3Tag.text'),
                "Coupon1Discount.text": request.POST.get('Coupon1Discount.text'),
                "Coupon2Discount.text": request.POST.get('Coupon2Discount.text'),
                "Coupon3Discount.text": request.POST.get('Coupon3Discount.text'),
                "Coupon1Condition.text": request.POST.get('Coupon1Condition.text'),
                "Coupon2Condition.text": request.POST.get('Coupon2Condition.text'),
                "Coupon3Condition.text": request.POST.get('Coupon3Condition.text'),
                "PhoneNumberPage2.text": request.POST.get('PhoneNumberPage2.text'),
                "FeaturesOfService.text": request.POST.get('FeaturesOfService.text'),
                "Feature1.text": request.POST.get('Feature1.text'),
                "Feature2.text": request.POST.get('Feature2.text'),
                "Feature3.text": request.POST.get('Feature3.text'),
                "HighlightFeature.text": request.POST.get('HighlightFeature.text'),
                "WebsiteLinkPage2.text": request.POST.get('WebsiteLinkPage2.text'),
                "CompanyAddressPage.text": request.POST.get('CompanyAddressPage.text'),
                "CutomerAddress.text": request.POST.get('CutomerAddress.text')
            }
        }

        # Define the API endpoint URL
        api_url = 'https://get.renderform.io/api/v2/render'

        # Retrieve the API key from settings (you should store your API key in Django settings for security)
        api_key = 'API_KEY'
        
        # Set up headers with the API key
        headers = {
            'X-API-KEY': api_key,
            'Content-Type': 'application/json'
        }

        try:
            # Send a POST request to the API
            response = requests.post(api_url, json=data, headers=headers)
            
            # Check if the request was successful
            if response.status_code == 200:
                response_message = f"API call successful! Response: {response.json()}"
            else:
                response_message = f"API call failed with status code {response.status_code}. Response: {response.text}"
        
        except requests.RequestException as e:
            response_message = f"An error occurred: {e}"

    # Render the form and pass response_message to the template
    return render(request, 'form.html', {'response_message': response_message})


