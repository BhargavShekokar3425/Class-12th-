from collections import Counter
ph1= ["Robocalls are on the rise. Be wary of any pre-recorded messages you might receive"]
ph2=["our access to your library account is expiring soon due to inactivity. To continue to have access to the library services account, you must reactivate your account. For this purpose, click the web address below or copy and paste it into your web browser. A successful login will activate your account and you will be redirected to your library profile"]
ph3=["We detected unknown IP access on our date base computer system our security requires you to verify your account for secure security kindly Click Here and verify your account"]
ph4=["Password will expire in 2 days  Click Here To Validate E-mail account"]
ph5=["As we prepare to start the 2016 Tax filling season, we have undergone slight changes in the filling process to make filling for your refund easier and to prevent unnecessary delays."]
ph6=["Hello, You have an important email from the Human Resources Department with regards to your December 2015 Paycheck"]
ph7=["Your parcel (shipping document) arrived at the post office. Here is your Shipping Document/Invoice and copy of DHL receipt for your tracking which includes the bill of lading and DHL tracking number, the new Import/Export policy supplied by DHL Express. Please kindly check the attached to confirm accordingly if your address is correct, before we submit to our outlet office for dispatch to your destination"]
ph8=["Your Itunes-ID has been disabled .You've place your account under the risk of termination by not keeping the correct informations .Please verify your account as soon as possible.Ready to check ?Click here to get back your account."]
ph9=["Hello,  Please refer to the vital info I've shared with you using Google Drive.  Click https://www.google.com/drive/docs/file0116 and sign in to view details.."]
ph10=["I recently read your last article and it was very useful in my field of research. I wonder, if possible, to send me these articles to use in my current research:This email is enclosed in the Marquette University secure network, hence access it below.Access the documents here <http://gabrielramon.be/<link removed>,***Ensure your login credentials are correct to avoid cancellations** Part of the changes include updating our database with your information."]
words1=ph1[0].split()+ph2[0].split()+ph3[0].split()+ph4[0].split()+ph5[0].split()+ph6[0].split()+ph7[0].split()+ph8[0].split()+ph9[0].split()+ph10[0].split()
stopwords=['to','the','and','or','you','your','with','have','had','has','of','in','our','is','for','it','will'] 
words=[]
for i in words1:
    if i not in stopwords:
        words.append(i)

word_counts = Counter(words)
top_five = word_counts.most_common(5)
print(top_five)