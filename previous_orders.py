#! C:/Users/dhanasree/AppData/Local/Programs/Python/Python312/python.exe
print("Content-type:text/html \r\n\r\n")
import cgi, cgitb, pymysql, os
cgitb.enable()
con = pymysql.connect(host="localhost", user="root", password="", database="quickmart")
cur = con.cursor()
form = cgi.FieldStorage()
Id = form.getvalue("id")

q1 = """select * from shop_register where id=%s """ % (Id)
cur.execute(q1)
rec = cur.fetchall()
for i in rec:
    NAME = i[1]
    fn = "img/shop_register/shop_photo/" + i[2]
    print("""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>orders</title>
    <link rel="stylesheet" href="css/skupload.css">
    <link rel="stylesheet" href="css/approved.css">
     <link rel="stylesheet" href="css/admin_home.css">
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC" crossorigin="anonymous">

</head>
<body>
<div class ="containerfulid ">
      <div class="sidenav">
     <center> <img src="%s" class="rounded-circle"width="100px" height="100" ><br>
      <h2>%s</h2></center>
     """ % (fn, NAME))
    print("""
      <a href="shop_info.py?id=%s">Home</a>
      <a href="uploads.py?id=%s">Update product</a>
      <a href="product_list.py?id=%s">Product list</a>
      <a href="orders.py?id=%s">Placed order</a>
      <a href="previous_orders.py?id=%s">previous order</a>
      <a href="slogin.py">Log out</a>"""%(Id,Id,Id,Id,Id) )
    print("""</div>""")
print("""<div class="con">
 <center>
 <h1>previous Orders</h1></center>
   <table class="table  table-hover table-bordered">
            <thead>
              <tr>
                <th scope="col">ID</th>
                <th scope="col">customer mail</th>
                <th scope="col">shop name</th>
                <th scope="col">product name</th>
                <th scope="col">price</th>
                <th scope="col">quantity</th>
                <th scope="col">net price</th>
                <th scope="col">Status</th>
              </tr>
            </thead>""")
q2 = """select * from orders where shopname="%s" """%(NAME)
cur.execute(q2)
rec = cur.fetchall()
for i in rec:
    print("""
                 <tbody>
                   <tr>
                     <td>%s</td>
                     <td>%s</td>
                     <td>%s</td>
                     <td>%s</td>
                     <td>%s</td>
                     <td>%s</td>
                     <td>%s</td>
                     <td>%s</td>
                  </tr>
                 </tbody>""" % (i[0], i[1], NAME, i[3], i[4], i[5], i[6], i[7]))
print("""</table>
     </div>
     </body>
     </html>""")