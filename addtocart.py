#! C:/Users/dhanasree/AppData/Local/Programs/Python/Python312/python.exe
print("Content-type:text/html \r\n\r\n")

import cgi,cgitb,pymysql
form =cgi.FieldStorage()
cgitb.enable()
con = pymysql.connect(host="localhost", user="root", password="", database="quickmart")
cur = con.cursor()
Id=form.getvalue("id")
# query = """select * from user_register where id="%s" """% (Id)
# cur.execute(query)
# rec = cur.fetchall()
query = """select * from cart where cst_id="%s"  """%(Id)
cur.execute(query)
rec = cur.fetchall()
for i in rec:
    cst_mail=i[1]
    sn=i[2]
print("""<!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>home</title>
        <link rel="stylesheet" href="css/style.css">
         <link rel="stylesheet" href="css/prdlist.css">
         <script src='https://kit.fontawesome.com/a076d05399.js' crossorigin='anonymous'></script>
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC" crossorigin="anonymous">
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css">
        <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/js/bootstrap.bundle.min.js" integrity="sha384-MrcW6ZMFYlzcLA8Nl+NtUVF0sA7MsXsP1UyJoMp4YLEuNSfAP+JcXn/tWtIaxVXM" crossorigin="anonymous"></script>
    </head>
    <body>
            <nav class="navbar navbar-expand-md navbar-dark bg-dark px-4 mb-4">
                <div class="container-fluid ">
                    <img src="img/src/QM logo.png" class="img-fluid" alt="..." width="230px" height="200px">
                  <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
                    <span class="navbar-toggler-icon"></span>
                  </button>
                  <div class="collapse navbar-collapse" id="navbarSupportedContent">
                    <ul class="navbar-nav me-auto mb-2 mb-lg-0">
                      <li class="nav-item">
                            <a class="nav-link active" aria-current="page" href="">Spices</a>
                     </li>
                      <li class="nav-item">
                        <a class="nav-link active" aria-current="page" href="">Vegetables</a>
                      </li>
                      <li class="nav-item">
                        <a class="nav-link active" aria-current="page" href="">Rice & Cereal</a>
                      </li>

                      <li class="nav-item">
                        <a class="nav-link active"aria-current="page" href="">Snacks</a>
                      </li>
                      <li class="nav-item">
                        <a class="nav-link active" aria-current="page" href="">Personal Care</a>
                      </li>
                    </ul>
                        <div class="dropdown">
                        <a  dropdown-toggle me-2" href="#" role="button" id="dropdownMenuLink" data-bs-toggle="dropdown" aria-expanded="false">
                        <i class='fas fa-user-circle' style='font-size:40px;color:white; margin:5px;'> </i>
                        </a>
                        <ul class="dropdown-menu" aria-labelledby="dropdownMenuLink">
                            <li><a class="dropdown-item" href="user_info.py?id=%s"><i class='fas fa-user-circle' ></i> User info</a></li>
                            <li><a class="dropdown-item" href="user_dashboard.py?id=%s"><i class='fa fa-home' ></i> Home</a></li>
                            <li><a class="dropdown-item" href="login.py"><i class='fas fa-power-off' ></i> Logout</a></li>
                        </ul>
                      </div>
                        <a class="btn btn-outline-light  me-2" href="addtocart.py?id=%s" role="button">
                        cart
                        </a>
                        <a class="btn btn-outline-light  me-2" href="user_orders.py?id=%s" role="button">
                        view orders
                        </a>
                  </div>
                </div>
            </nav>""" % (Id, Id, Id, Id))
print("""
<table class="table">
<tr><th>product</th>
<th>quantity</th></tr>
<form method="post">""")
for i in rec:
    print("""<tr>
    <td><input type='checkbox' name="vege" value="%s">%s</td>
    <td><input type='number' class='form-inline' name='qty' min=1 max=50 style='heigth:30px; width:50px; font-size:15px; fontweigth:bold;' value="%s"></td></tr>"""%(i[3],i[3],i[4]))
print(""" <tr><td colspan=2 align="center"><input type="submit" name="submit" class="btn btn-warning" value="BUY NOW"></td></tr>
</form>
</table>""")
sb = form.getvalue("submit")
if sb!=None:
    pn= form.getvalue("vege")
    ta=0
    np=0
    price=0
    qty=0
    print("""<table class="table">""")
    print("<tr><th>Shop name</th><th>Product</th><th>Quantity</th><th>Price</th><th>Net Price</th></tr>")
    for i in pn:
        query="select product_price from product_upload where product_name='%s'"%(i)
        cur.execute(query)
        rec=cur.fetchone()
        if rec!=None:
            price=rec[0]
        print(price,i)
        qry="""select * from cart where cst_id=%s and productname='%s'"""%(Id,i)
        cur.execute(qry)
        rec = cur.fetchall()
        for j in rec:
            sn=j[2]
            qty=j[4]
        np=qty*price
        ta=ta+np
        print("""<tr><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td>"""%(sn,i,qty,price,np))
        q="""insert into orders(cst_mail,shopname,productname,quantity,price,net_price)values('%s','%s','%s','%s',%s,%s)"""%(cst_mail,sn,i,qty,price,np)
        cur.execute(q)
        con.commit()
        q1="""delete from cart where username='%s' and productname='%s' """%(cst_mail,i)
        cur.execute(q1)
        con.commit()
    print("""<tr><td colspan=4 aling='rigth'>total price</td><td>%s</td></tr>"""%(ta))
    print("""</table>
    <center><a href="user_dashboard.py" class='btn btn-info'><i class='glyphicon glyphicon-home'</i>go to home</a></center>
""")
print("""</body>
</html>""")