#! C:/Users/dhanasree/AppData/Local/Programs/Python/Python312/python.exe
print("Content-type:text/html \r\n\r\n")

import cgi, cgitb, pymysql
form = cgi.FieldStorage()
cgitb.enable()
con = pymysql.connect(host="localhost", user="root", password="", database="quickmart")
cur = con.cursor()
Id = form.getvalue("id")
NAME =form.getvalue("shop_name")
query = """select * from shop_register where id="%s" """ % (Id)
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
    <title>Product Upload</title>
    <link rel="stylesheet" href="css/approved.css">
    <link rel="stylesheet" href="css/admin_home.css">
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.3/dist/js/bootstrap.bundle.min.js"></script>
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
print("""</div></div>
   
  <div class="con">
  <h1>Product upload details</h1>
    <table class="table table-secondary table-hover table-bordered mx-3">
            <thead>
              <tr>
                <th scope="col">ID</th>
                <th scope="col">Shop Name</th>
                <th scope="col">Product Name</th>
                <th scope="col">Quantity</th>
                <th scope="col">Price</th>
                <th scope="col">unit</th>
                <th scope="col">image</th>
                <th scope="col">description</th>
                <th scope="col">Update</th>
                <th scope="col">delete</th>
              </tr>
            </thead>""")

qry = """select * from product_upload where shop_name="%s"  """%(NAME)
cur.execute(qry)
rec = cur.fetchall()
for i in rec:
    fn = "img/product_upload/"+i[6]
    print("""
        <tbody>
          <tr><form method="post" enctype="multipart/form-data">
            <td><input type="text" name="id" value=%s readonly></td>
            <td><input type="text" name="sname" value="%s" readonly></td>
            <td><input type="text" name="name" value="%s"></td>
            <td><input type="text" name="Quantity" value=%s></td>
            <td><input type="text" name="Price" value=%s></td>
            <td><input type="text" name="unit" value=%s></td>
            <td><img src="%s" height="100" width="100" name="image" ></td>
            <td><input type="text" name="description" value="%s"></td>
            <td><input type="submit" name="Update" value="Update" class="btn btn-info"></td>
            <td><input type="submit" name="delete" value="Delete" class="btn btn-danger"></td>
         </form> </tr>
        </tbody>
    """%(i[0],i[1],i[2],i[3],i[4],i[5],fn,i[7]))

print("""</table>
</body>
</html>""")
form = cgi.FieldStorage()
up = form.getvalue("Update")

if up!= None:
    id = form.getvalue("id")
    sn = form.getvalue("sname")
    pn = form.getvalue("Name")
    pq = form.getvalue("Quantity")
    pp = form.getvalue("Price")
    pu = form.getvalue("unit")
    pd = form.getvalue("description")
    query1 = """update product_upload set product_name='%s',  product_quantity='%s', product_price='%s', units='%s', product_description='%s' where id=%s """ %(pn, pq, pp, pu, pd,id)
    cur.execute(query1)
    con.commit()
    print(f"""<script>
                alert("Update successful!");
                window.location.href = "product_list.py?id=%s";
             </script>"""%(Id))
dl = form.getvalue("delete")
if dl!= None:
    id = form.getvalue("id")
    query2 = """delete from product_upload where id=%s""" % (id)
    cur.execute(query2)
    con.commit()
    print(""" <script>
                 alert("delete successfully!!!");
                 </script>
              """)