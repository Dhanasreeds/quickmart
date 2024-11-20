#! C:/Users/dhanasree/AppData/Local/Programs/Python/Python312/python.exe
print("Content-type:text/html \r\n\r\n")

import cgi, cgitb, pymysql
form = cgi.FieldStorage()
Sid = form.getvalue("sid")
Uid = form.getvalue("uid")
cgitb.enable()
con = pymysql.connect(host="localhost", user="root", password="", database="quickmart")
cur = con.cursor()
query = """select * from shop_register where id="%s" """ % (Sid)
cur.execute(query)
rec = cur.fetchall()
for i in rec:
     sn=i[1]
query = """select * from user_register where id="%s" """ % (Uid)
cur.execute(query)
rec = cur.fetchall()
for i in rec:
    un=i[2]
query = """select * from product_upload where shop_name="%s" """%(sn)
cur.execute(query)
rec = cur.fetchall()

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
          </nav>""" % (Uid, Uid, Uid, Uid))
print("""
<div class="container mt-5">
    <div class="row">""")
for i in rec:
    NAME = i[2]
    fn = "img/product_upload/" + i[6]
    pd =i[7]
    pp = i[4]
    print("""
        <div class="col-md-3 col-sm-6 mb-4">
            <div class="card h-100">
                <img src="%s" class="card-img-top"width="100px" height="100" alt="Product Image">
                <div class="card-body">
                    
                    <p class="card-text"name="prdes">%s</p>
                    <p class="card-text" name="pprice"><strong>Price:%s</strong></p>
                    <p class="card-text">
                    <form  method="post">
                    <input type="text" class="form-control" name="prname" style="height: 30px; width: 200px; font-size: 15px; font-weight: bold;" value="%s"><br>
                     <input type="number" class="from-inline" name="qty" style="height: 30px; width: 50px; font-size: 15px; font-weight: bold;" value="1">
                     <input type="submit" class="btn btn-success form-inline" name="submit" value="Add to cart">
                    </form>
                 </p>
                </div>
            </div>  
        </div>      
      """ % (fn,pd,pp,NAME))

print("""   
</div>
</div>
</body>
</html>""")
sb = form.getvalue("submit")
if sb!= None:
    prname=form.getvalue("prname")
    qt=form.getvalue("qty")
    query="""select * from cart where username='%s' and shopname='%s' and productname='%s' """%(un,sn,prname)
    cur.execute(query)
    rec=cur.fetchone()
    if rec!=None:
        q1="""update cart set quantity=quantity+'%s' where username='%s' and productname='%s' """%(qt,un,prname)
        cur.execute(q1)
        rec = cur.fetchone()
        con.commit()
        print("""
              <script>
              alert("item added to cart successfully");
              location.href="products.py?sid=%s&uid=%s";
              </script>
              """%(Sid,Uid))
    else:
        q1="""insert into cart values(%s,'%s','%s','%s','%s')"""%(Uid,un,sn,prname,qt)
        cur.execute(q1)
        rec = cur.fetchone()
        con.commit()
        print("""
                     <script>
                     alert("item added to cart successfully");
                     location.href="products.py?sid=%s&uid=%s";
                     </script>
                     """ % (Sid,Uid))
