#! C:/Users/dhanasree/AppData/Local/Programs/Python/Python312/python.exe
print("Content-type:text/html \r\n\r\n")
import cgi, cgitb, pymysql,smtplib
cgitb.enable()
con = pymysql.connect(host="localhost", user="root", password="", database="quickmart")
cur = con.cursor()
query = """select * from shop_register where status="" """
cur.execute(query)
rec = cur.fetchall()
print("""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Registered shop</title>
    <link rel="stylesheet" href="css/approved.css">
    <link rel="stylesheet" href="css/admin_home.css">
    
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.3/dist/css/bootstrap.min.css" rel="stylesheet">
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.3/dist/js/bootstrap.bundle.min.js"></script>
</head>
<body>
 <div class ="containerfulid ">

   <div class ="sidenav">
    <center> <img src="img/src/man.jpg" class="rounded-circle" width="100px" height="100" style="border-radius:50%;" ><br>
    <h2>Admin</h2></center>
    <a href = "admin_home.py" > Home </a>
    <a href = "Approved_shop.py" >Approved shop </a>
    <a href = "Registered_shop.py" >Registered shop </a>
    <a href = "users.py" > Customer Details </a>
   </div>
 </div>""")
print("""
  <h1>Registered shop details</h1>
   <div class="con">
    <table class="table table-secondary table-hover table-bordered">
            <thead>
              <tr>
                <th scope="col">ID</th>
                <th scope="col">Shop name</th>
                <th scope="col">Shop photo</th>
                <th scope="col">Address</th>
                <th scope="col">City</th>
                <th scope="col">Pincode</th>
                <th scope="col">State</th>
                <th scope="col">Nationality</th>
                <th scope="col">owner_name</th>
                <th scope="col">Gender</th>
                <th scope="col">owner_photo</th>
                <th scope="col">Mail_id</th>
                <th scope="col">Mobile</th>
                <th scope="col">Approve</th>
                <th scope="col">Reject</th>
              </tr>
            </thead>""")
for i in rec:
    fn1 = "img/shop_register/shop_photo/" + i[2]
    fn2 = "img/shop_register/owner_photo/" + i[10]
    print("""
            <tbody>
              <tr><form method="post">
                <td><input type="text" value="%s" name="id" readonly></td>
                <td><input type="text" value="%s" name="shop_name" ></td>
                <td><img src="%s" height=100 width=100> </td>
                <td>%s</td>
                <td>%s</td>
                <td>%s</td>
                <td>%s</td>
                <td>%s</td>
                <td><input type="text" value="%s" name="owner_name" ></td>
                <td>%s</td>
                <td><img src="%s" height=100 width=100> </td>
                <td><input type="text" value="%s" name="mail_id" ></td>
                <td>%s</td>
            <td><input type="submit" name="Approved" value="Approve" class="btn btn-info"></td>
            <td><input type="submit" name="Reject" value="Reject" class="btn btn-danger"></td>
            
             </form> </tr>
               </tbody>""" % (i[0], i[1], fn1, i[3], i[4], i[5], i[6], i[7], i[8], i[9], fn2, i[11], i[13]))
print(""" </table>
</div>
</body>
</html>""")
form = cgi.FieldStorage()
up = form.getvalue("Approved")
if up != None:
    id = form.getvalue("id")
    sn = form.getvalue("shop_name")
    on = form.getvalue("owner_name")
    mid = form.getvalue("mail_id")
    query = """update shop_register set status="Approved", password="12345" where id=%s""" % (id)
    cur.execute(query)
    con.commit()
    from_email = "mail id "
    password = "mail passcode"
    to_mail = mid
    subject = "Welcome to QuickMart!"
    body = """
Dear {},

Welcome to QuickMart! Your shop {} account has been created successfully.
    
    Password: 12345

Please change your password after logging in.

Best regards,
The QuickMart Team
    """.format(on,sn)
    msg = "subject:{} \n\n {}".format(subject, body)
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    server.login(from_email, password)
    server.sendmail(from_email, to_mail, msg)
    server.quit()
    print("""<script>
     alert("Approved Successfully!");
        </script>
      """)
dl = form.getvalue("Reject")
if dl != None:
    id = form.getvalue("id")
    sn = form.getvalue("shop_name")
    on = form.getvalue("owner_name")
    mid = form.getvalue("mail_id")
    query = """update  shop_register set status="Rejected" where id=%s""" % (id)
    cur.execute(query)
    con.commit()
    from_email = "quickmart29qm@gmail.com"
    password = "bhxx lqqb mjyq thrh"
    to_mail = mid
    subject = "Rejected to QuickMart!"
    body = """
    Dear {},

      Your shop {} account has been Rejected.
      Please provied a valid details.

    Best regards,
    The QuickMart Team
        """.format(on, sn)
    msg = "subject:{} \n\n {}".format(subject, body)
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    server.login(from_email, password)
    server.sendmail(from_email, to_mail, msg)
    server.quit()
    print("""
                 <script>
                 alert("Rejected successfully!!!");
                 </script>
              """)