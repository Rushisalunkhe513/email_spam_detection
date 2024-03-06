#!/usr/bin/env python
# coding: utf-8

# # Python project For Email Spam Detection.

# In[1]:


# lets load the dataset mbox.txt


# In[2]:


import re


# In[15]:


# we have opened file in file, we could have opened file by pandas read_csv but its not csv file.
"""
read() actually reads all file in single string where,
readlines() actually seperates line from text file into list, and then we can count no of lines.
"""
def count_no_lines(filename):
    count = 0
    with open(f"{filename}","r") as file:
        no_lines = file.readlines()
        count = len(no_lines)
    return count

# lets call function
file_name = "mbox-short.txt"
count_no_lines(file_name)
# here are no of lines in text file.


# In[4]:


# now we have to explore content of the email file.


# In[16]:


# we need to find line in text file starting with Subject
# we need to see entire lines strting with Subject, so rather than taking lines in list lets take entire paragraph.
def count_lines(filename):
    with open(filename) as file:
        starts_with_Subject = []
        for line in file:
            if line.startswith("Subject"):
                starts_with_Subject.append(line)
        return len(starts_with_Subject)
   


# In[17]:


# lets call this function to see no of lines start with Subject
file_text_name = "mbox-short.txt"
count_lines(file_text_name)


# In[7]:


# "rb" is used to open non-string data file where "r" used to open string data file like this.
def list_lines(file_name):
    with open(file_name,"r") as file:
        strt = file.readlines()
        str_subject = []
        for line in strt:
            if line.startswith("Subject"):
                str_subject.append(line)
    print(len(str_subject))
                
list_lines("mbox-short.txt")


# In[18]:


# now lets find avg of span confidencwe in line
# lets find a line taht starts with X-DSPAM-Confidence
# and then split that line at : and take its float value and avg it.
def avg_spam_confidence(file_name):
    starts_with_spam = []
    spam_value = []
    with open(file_name,"r") as file:
        file_data = file.readlines()
        
        for line in file_data:
            if line.startswith("X-DSPAM-Confidence:"):
                starts_with_spam.append(line)
        for spam_line in starts_with_spam:
            line_split = spam_line.split(":")
            spam_value.append(float(line_split[1]))
        return sum(spam_value)/len(spam_value)
            
        
# lets call that function and calculate its avg spam value.
avg_spam_confidence("mbox-short.txt")


# In[19]:


# Find Which Day of the Week the Email was sent

def count_day_email_sent(file_name):
    day_email_sent = []
    line_date = []
    dict_day = {}
    with open(file_name,"r") as file:
        file_data = file.readlines()
        
        for line in file_data:
            if line.startswith("From"):
                day_email_sent.append(line)
        #print(file_data)
        for line in day_email_sent:
            from_line = line.split()
            if len(from_line)>3:
                line_date.append(from_line)
            else:
                pass
        for day in line_date:
            for week_day in day:
                if week_day in ["Mon","Tue","Wed","Thu","Fri","Sat"]:
                    dict_day[week_day] = dict_day.get(week_day,0)+1
    return dict_day
# lets call that function
# now we can see no of day email was sent.
count_day_email_sent("mbox-short.txt")


# In[10]:


# now lets explore the header of emails.


# In[11]:


# now lets see how many email address ahve sent us messages.
def count_message_from_email(file_name):
    email_list = []
    email_message = []
    count_email =  {}
    with open(file_name,"r") as file:
        file_data = file.readlines()
        for line in file_data:
            if line.startswith("From"):
                email_list.append(line)
                split_line = line.split()
                count_email[split_line[1]] = count_email.get(split_line[1],0)+1
        return count_email

# lets see how many email have sent us messages.
count_message_from_email("mbox-short.txt")


# In[12]:


# so this many people with there email has sent us emails.


# In[20]:


# now we should write function to see from which domain we have received the emails.

def no_msg_from_domain(filename):
    domain = count_message_from_email(filename)
    domain_dict = {}
    domains_list = []
    for key in domain.keys():
        domain_data = key.split("@")
        domains_list.append(domain_data[1])
    for domain in domains_list:
        domain_dict[domain] = domain_dict.get(domain,0)+1
    return domain_dict

# lets call function to get list domain sent us messages
no_msg_from_domain("mbox-short.txt")


# In[14]:


# Done


# #  let create class and object type file.

# In[21]:


# let create class and object type file.

class SpamEmail:
    # function to count no of lines from text file.
    def count_no_lines(self,filename):
        self.filename = filename
        count = 0
        with open(f"{self.filename}","r") as file:
            no_lines = file.readlines()
            count = len(no_lines)
        return count
    
    # function to calcukte no of line starts from Subject
    def count_lines(self,filename):
        self.filename = filename
        with open(self.filename) as file:
            starts_with_Subject = []
            for line in file:
                if line.startswith("Subject"):
                    starts_with_Subject.append(line)
            return len(starts_with_Subject)
     
    # lets calculte avg spam in email.
    def avg_spam_confidence(self,file_name):
        self.file_name = file_name
        starts_with_spam = []
        spam_value = []
        with open(self.file_name,"r") as file:
            file_data = file.readlines()

            for line in file_data:
                if line.startswith("X-DSPAM-Confidence:"):
                    starts_with_spam.append(line)
            for spam_line in starts_with_spam:
                line_split = spam_line.split(":")
                spam_value.append(float(line_split[1]))
            return sum(spam_value)/len(spam_value)
        
    
    
    # lets see email sent by day in week
    def count_day_email_sent(self,file_name):
        self.file_name = file_name
        day_email_sent = []
        line_date = []
        dict_day = {}
        with open(self.file_name,"r") as file:
            file_data = file.readlines()

            for line in file_data:
                if line.startswith("From"):
                    day_email_sent.append(line)
            #print(file_data)
            for line in day_email_sent:
                from_line = line.split()
                if len(from_line)>3:
                    line_date.append(from_line)
                else:
                    pass
            for day in line_date:
                for week_day in day:
                    if week_day in ["Mon","Tue","Wed","Thu","Fri","Sat"]:
                        dict_day[week_day] = dict_day.get(week_day,0)+1
        return dict_day
    
    # lets see how many emails have sent us message
    def count_message_from_email(self,file_name):
        self.file_name = file_name
        email_list = []
        email_message = []
        count_email =  {}
        with open(self.file_name,"r") as file:
            file_data = file.readlines()
            for line in file_data:
                if line.startswith("From"):
                    email_list.append(line)
                    split_line = line.split()
                    count_email[split_line[1]] = count_email.get(split_line[1],0)+1
            return count_email
    
    # lets see emails from diffrent domains
    def no_msg_from_domain(self,filename):
        self.filename = filename
        domain = count_message_from_email(self.filename)
        domain_dict = {}
        domains_list = []
        for key in domain.keys():
            domain_data = key.split("@")
            domains_list.append(domain_data[1])
        for domain in domains_list:
            domain_dict[domain] = domain_dict.get(domain,0)+1
        return domain_dict
    


# In[28]:


# lets take object of class
email_spam = SpamEmail()

# lets see no of lines in file
email_spam.count_no_lines("mbox-short.txt")

# lets see no of line starts from Subject
email_spam.count_lines("mbox-short.txt")

# lets see avg spam confidence
email_spam.avg_spam_confidence("mbox-short.txt")

# lets see on which day of week email was sent.
email_spam.count_day_email_sent("mbox-short.txt")

# lets see email was sent by whom and which email id by how many times.
email_spam.count_message_from_email("mbox-short.txt")

# see where this ,essage came from
email_spam.no_msg_from_domain("mbox-short.txt")


# In[ ]:




