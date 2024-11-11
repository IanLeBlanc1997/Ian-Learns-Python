import requests
from bs4 import BeautifulSoup
import smtplib
import os
email = os.getenv("EMAIL")
headers = {'User-Agent':"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.1 Safari/605.1.15","Accept-Language":"en-US"}

response = requests.get('https://www.amazon.com/Raw-Grass-Fed-Whey-5LB/dp/B06XX65GS1?pd_rd_w=m0MCN&content-id=amzn1.sym.2301d529-61cf-4c52-a694-4383fe0e2fbe&pf_rd_p=2301d529-61cf-4c52-a694-4383fe0e2fbe&pf_rd_r=ANCS310A4QRG5MXFYARE&pd_rd_wg=YHAaW&pd_rd_r=ab872654-63eb-4d01-b881-96dcf5737962&pd_rd_i=B06XX65GS1&psc=1&ref_=pd_bap_d_grid_rp_0_1_ec_cp_pd_hp_d_atf_rp_1_i',headers=headers)
data= response.text
soup = BeautifulSoup(data,"html.parser")
whole_number= int(soup.find(class_="a-price-whole").getText().strip("."))
decimal = int(soup.find(class_='a-price-fraction').getText())
full_price = float(whole_number + decimal/100)


if full_price <= 71:
    with smtplib.SMTP("smtp.gmail.com",587) as connection:
        app_password = os.getenv("GMAIL_CODE")
        connection.starttls() #security setup 
        connection.login(user = email, password= app_password) #login and send mail
        connection.sendmail(
            from_addr = email,
            to_addrs = "ianleblanc7667@yahoo.com",
            msg = f"Subject: Pricepoint reached!\n\n Pressure cooker at {full_price}!")
