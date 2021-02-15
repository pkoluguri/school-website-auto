try:
 from selenium import webdriver
except ModuleNotFoundError:
 print("installing selenium because you don't have it")
 from os import system
 system("pip3 install selenium")
import time
import re

class combined:
  def __init__(self,title,link,subject=""):
      self.title = title
      self.link = link
      self.subject = subject

op = webdriver.ChromeOptions()
driver = webdriver.Chrome(executable_path="chromedriver.exe",options=op)
driver.get("https://parent.neverskip.com")

time.sleep(2)

print("logging in...")
number_field = driver.find_element_by_xpath("/html/body/kt-auth/div/div/div[2]/kt-login/div[2]/div/form/div[1]/mat-form-field/div/div[1]/div/input")
number_field.send_keys("8309457526")
submit = driver.find_element_by_xpath(' //*[@id="kt_login_signin_submit"]')
submit.click()

time.sleep(1)

password_element = driver.find_element_by_xpath('//*[@id="mat-input-1"]')
pasword = input("enter the password:")
password_element.send_keys(password)
submit = driver.find_element_by_xpath(' //*[@id="kt_login_signin_submit"]')
submit.click()
print("logged in..")

time.sleep(1)

print("getting information...")
driver.get("https://parent.neverskip.com/#/default/content-library")

time.sleep(10)
try:
 while True:
  content = driver.page_source
  links = []
  formatted = []
  links = re.findall(r'href="(.*?)"', content)
  downloaded_once = False 
  titles = driver.find_elements_by_class_name("assignment-title")
  subjects = []
  for i in range(9):
   subject = driver.find_element_by_xpath(f'//*[@id="kt_content"]/kt-studentlibrary-v2/div/div/div[2]/div/kt-portlet-body/div[{i+1}]/div[3]/div[2]/span[1]')
   subjects.append(subject.text)

  with open("k.txt","r") as linkss:
      for link in linkss:
        i = links.index(link.strip("\n"))
        links.pop(i)

  for index in range(len(links)):
    if ".pdf" in links[index] or ".docx" in links[index] or ".pttx" in links[index]:
      ob = combined(titles[index].text,links[index],subjects[index])
      formatted.append(ob)
  print("got inormation...")

  for formatt in formatted:
      typeoffile = re.findall(r"\.pdf|\.docx|\.pptx",formatt.link) 
      filename_downloaded = re.findall(r'/lms_upload/(.*?\.pdf|\.docx|\.pptx)',formatt.link)
      import os
      filename = ""
      download = False
      completed = False
      files = []
      subject = formatt.subject
      filename = formatt.title+typeoffile[0]
      path = "C:\\Manas Disc D\\Manas 8C PDF Subject"
      if os.path.exists(path+"\\"+subject):
        files = os.listdir(path+"\\"+subject)
      else:
          os.mkdir(path+"\\"+subject)
      if files != []:
          for file in files:
              if file == filename:
                  completed = True
          if not completed:          
            download = True
      else:
          download = True

      if download:
          downloaded_once = True
          print(f"downloading {filename}")
          driver.get(formatt.link)
          path1 = f"C:\\Users\\MANAS POTTLAPELLI\\Downloads\\{filename_downloaded[0]}"
          time.sleep(20)
          binary = ""
          with open(path1,"rb") as file:
            binary = file.read()
          os.remove(path1)  
          with open(path+"\\"+subject+"\\"+filename,"wb") as file:
            file.write(binary)
          print(f"downloaded {filename}")
      if not downloaded_once:
        print("nothing to download")
      print("waiting for 2 min")
      time.sleep(60*2)
      print("checking again")
  driver.quit()
except KeyboardInterrupt:
  print("keyboard has interrupted the code")

except Exception as error:
  print(f"uknown exception as occured:{error}") 
