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
for i in rec:
    NAME = i[1]
    fn = "img/shop_register/shop_photo/" + i[2]
print("""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <link rel="stylesheet" href="css/prdlist.css">
    <link rel="stylesheet" href="css/admin_home.css">
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC" crossorigin="anonymous">

</head>
<body>
<div class ="containerfulid ">
      <div class="sidenav">
     <center> <img src="%s" class="rounded-circle"width="100px" height="100" ><br>
      <h2>%s</h2></center>
     """%(fn, NAME))
print("""
      <a href="shop_info.py?id=%s">home</a>
      <a href="uploads.py?id=%s">update product</a>
      <a href="product_list.py?id=%s">product list</a>
      <a href="uprolist.py?id=%s">placed order</a>"""%(Id,Id,Id,Id))
query = """select * from product_upload where shop_name="%s" """
cur.execute(query)
rec = cur.fetchall()
for i in rec:
    pn=i[2]
    fn= "img/product_upload/" + i[6]
    print("""</div></div>
    <div class="con">
    <fieldset>
        <div class="row">
    <div class="col-lg-3">
        <div class="cart">
     <div class="thumbunail">
      <center>  <img src="%s" width="100px" height="100" ><br>
      <h6>%s</h6>
      """%(fn,pn))
      
print("""       <div class="caption">
            <form action="" method="post">
              <input type="number" class="from-inline" name="qty" style="height: 30px; width: 50px; font-size: 15px; font-weight: bold;" value="1">
              <input type="submit" class="btn btn-success form-inline" name="submit"value="Add to cart">
            </form></center>
        </div>
      </div></div>
     </div>
</div></fieldset></div>
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/js/bootstrap.bundle.min.js" integrity="sha384-MrcW6ZMFYlzcLA8Nl+NtUVF0sA7MsXsP1UyJoMp4YLEuNSfAP+JcXn/tWtIaxVXM" crossorigin="anonymous"></script>

</body>
</html>""")