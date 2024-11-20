#! C:/Users/dhanasree/AppData/Local/Programs/Python/Python312/python.exe
print("Content-type:text/html \r\n\r\n")
import cgi,cgitb,pymysql
form =cgi.FieldStorage()
Id=form.getvalue("id")
cgitb.enable()
con = pymysql.connect(host="localhost", user="root", password="", database="quickmart")
cur = con.cursor()
query = """select * from shop_register where id="%s" """% (Id)
cur.execute(query)
rec = cur.fetchall()
print("""<!DOCTYPE html>

<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <link rel="stylesheet" href="css/shopkhome.css" />
       <link rel="stylesheet" href="css/admin_home.css">
    <link rel="stylesheet" href="css/approved.css">
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC" crossorigin="anonymous">
</head>""")


for i in rec:
    NAME= i[1]
    fn= "img/shop_register/shop_photo/" + i[2]
print("""<body>
    <div class="sidenav">
     <center> <img src="%s" class="rounded-circle"width="100px" height="100" ><br>
      <h2>%s</h2></center>
     """%(fn, NAME))
print("""
      <a href="shop_info.py?id=%s">Home</a>
      <a href="uploads.py?id=%s ">update product</a>
      <a href="product_list.py?id=%s ">Product list</a>
      <a href="orders.py?id=%s ">Placed order</a>
      <a href="previous_orders.py?id=%s">previous order</a>
      <a href="slogin.py">Log out</a>"""%(Id,Id,Id,Id,Id))
print("""</div>
    </div>
      <div class="con">
      <center style="margin-top:130px;">
       <h1>Welcome %s!!!</h1>"""%(NAME))
print("""<br><img src="img/src/QM logo.png" class="logo" width="80%" height="70%">
      </center>
  </div>""")
print("""<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/js/bootstrap.bundle.min.js" integrity="sha384-MrcW6ZMFYlzcLA8Nl+NtUVF0sA7MsXsP1UyJoMp4YLEuNSfAP+JcXn/tWtIaxVXM" crossorigin="anonymous"></script>
</body>
</html>""")
