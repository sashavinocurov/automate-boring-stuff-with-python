import bs4, requests

def getAmazonPrice(productUrl):
    res = requests.get(productUrl)
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    elems =soup.select('font-family: "Amazon Ember",Arial,sans-serif; border-collapse: collapse; box-sizing: border-box; font-size: 18px!important; line-height: 24px!important; text-rendering: optimizeLegibility; color: \#B12704!important;') #CSS Brakedown
    return elems[0].text.strip()
    



price = getAmazonPrice('https://www.amazon.com/Apple-MWP22AM-A-AirPods-Pro/dp/B07ZPC9QD4/ref=lp_509318_1_5?s=aht&ie=UTF8&qid=1602525855&sr=1-5') #Amazon Url
print('The price is ' + price)

