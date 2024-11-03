import yfinance as yf
from django.shortcuts import render

def company_details(request):
    company_data = {}
    if 'ticker' in request.GET:  # Change 'company_name' to 'ticker'
        ticker = request.GET.get('ticker').strip().upper()  # Convert ticker to uppercase for consistency
        
        try:
            # Attempt to fetch the stock information using yfinance
            stock = yf.Ticker(ticker)
            info = stock.info
            
            # Check if the info contains valid data
            if 'longName' in info:
                company_data = {
                    'Name': info.get('longName', 'N/A'),
                    'Market Cap': info.get('marketCap', 'N/A'),
                    'PE Ratio': info.get('trailingPE', 'N/A'),
                    'Enterprise Value': info.get('enterpriseValue', 'N/A'),
                    'Number of Shares': info.get('sharesOutstanding', 'N/A'),
                    'Face Value': info.get('bookValue', 'N/A'),
                    'Debt': info.get('totalDebt', 'N/A'),
                    'Cash': info.get('totalCash', 'N/A'),
                    'ROCE': info.get('returnOnCapitalEmployed', 'N/A'),
                    'ROE': info.get('returnOnEquity', 'N/A'),
                    'PAT': info.get('netIncomeToCommon', 'N/A')
                }
            else:
                company_data = {'Error': 'Company ticker not found. Please check the ticker and try again.'}
        
        except Exception as e:
            company_data = {'Error': str(e)}

    return render(request, 'stockapp/company_details.html', {'company_data': company_data})
