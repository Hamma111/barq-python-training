# Projects

---

#### Project #1

YouTube Channel's Videos Data Scraper [2023-03-05]

1. You should write a python program which should be able to scroll a youtube channel webpage all the way to then end.
   For example, you have this channel of my teacher https://www.youtube.com/@zusmani78/videos. Your code should be able
   to go to this page and automatically scroll down until you reach the end of the page.
2. Once you have reached the end of the page, you should scrape the information of all the videos present on that page
   and nicely store that in a CSV file using pandas. The output CSV file should have record of these four fields of
   video: name, views, duration, time, thumbnail image URL
3. Once you have done the above two tasks, write a general program which should take the input of a youtube channel
   link, which then outputs a record of all the videos uploaded by that channel.

---

#### Project #2

YouTube Channel's Videos Comments Data Scraper [2023-03-12]

1. Write a Python program which should visit a YouTube video, and scrape its comments. You should store all the comments
   in a CSV file. For example, if you visit this video of my mentor and
   employer https://www.youtube.com/watch?v=zghBofrKv7s, scrape all the comments of this video and store in a CSV file.
   The CSV file should have these columns: username, user's thumbnail URL (profile image basically), commented at time,
   comment text and number of likes. The name of CSV file should be the video's name.
2. Write a Python program which takes input a YouTube channel link, and create a CSV file in a folder, named against the
   YouTube username, for each and every video on that channel. For example, if you give it the input
   of https://www.youtube.com/@ehmadzubair/videos, it should create a folder named ehmadzubair which should have 67
   separate CSV files in it (because the channel has 67 videos as of now).

---

#### Project #3

Email sender [2023-04-19]

Write a python program which takes in email content and comma separated emails ids as input, and send all those emails
the typed out email. Here is how it should operate:

```
Please enter the mail content : Hi everyone, I am sending this very important email to your from sendgrid but it is just a test to be honest. Ok bye.
Please enter the recepient email ids: person1@gmail.com, person2@gmail.com, person3@gmail.com
```

The above program should the email to all the recipient emails.

**Note** that you have to use sendgrid service to send emails. https://sendgrid.com/. Sign up for it to get started.
This video should be helpful as well: https://www.youtube.com/watch?v=xCCYmOeubRE&t=55s&ab_channel=Twilio

---

