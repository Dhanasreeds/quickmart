#! C:/Users/dhanasree/AppData/Local/Programs/Python/Python312/python.exe
print("Content-type:text/html \r\n\r\n")
import cgi,cgitb,pymysql
form =cgi.FieldStorage()
Id=form.getvalue("id")
cid=form.getvalue("Mail_id")
cgitb.enable()
con = pymysql.connect(host="localhost", user="root", password="", database="quickmart")
cur = con.cursor()
query = """select * from user_register where id="%s" """% (Id)
cur.execute(query)
rec = cur.fetchall()
for i in rec:
    cid=i[2]
q1 = """select * from orders where cst_mail="%s" """%(cid)
cur.execute(q1)
rec = cur.fetchall()

print("""<!DOCTYPE html>
<html lang="en">
 <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>home</title>
         <link rel="stylesheet" href="css/skupload.css">
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
 <div class="con">
 <center>
 <h3>Orders placed</h3></center>
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
                 </tbody>""" % (i[0], i[1], i[2], i[3], i[4], i[5], i[6],i[7]))
print(""" </table>
     </div>
     </body>
     </html>""")