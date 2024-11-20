#! C:/Users/dhanasree/AppData/Local/Programs/Python/Python312/python.exe
print("Content-type:text/html \r\n\r\n")
import  cgitb, pymysql
cgitb.enable()
con = pymysql.connect(host="localhost", user="root", password="", database="quickmart")
cur = con.cursor()
query = """select * from shop_register where status="Approved" """
cur.execute(query)
rec = cur.fetchall()
print("""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Approved shop</title>
    <link rel="stylesheet" href="css/admin_home.css">
    <link rel="stylesheet" href="css/approved.css">
    <link rel="stylesheet" href="css/admin_home.css">
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.3/dist/css/bootstrap.min.css" rel="stylesheet">
</head>
<body>
 <div class ="containerfulid ">
   <div class ="sidenav">
    <center> <img src="img/src/man.jpg" class="rounded-circle" width="100px" height="100px" style="border-radius:50%;" ><br>
    <h2>Admin</h2></center>
    <a href = "admin_home.py" > Home </a>
    <a href = "Approved_shop.py" >Approved shop </a>
    <a href = "Registered_shop.py" >Registered shop </a>
    <a href = "users.py" > Customer Details </a>
   </div>
 </div>""")
print("""
  <h1>Approved shop details</h1>
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
                <th scope="col">password</th>
                <th scope="col">Mobile</th>
                </tr>
            </thead>""")
for i in rec:
    fn1 = "img/shop_register/shop_photo/" + i[2]
    fn2 = "img/shop_register/owner_photo/" + i[10]
    print("""
            <tbody>
              <tr><form method="post">
                <td>%s</td>
                <td>%s</td>
                <td><img src="%s" height=100 width=100> </td>
                <td>%s</td>
                <td>%s</td>
                <td>%s</td>
                <td>%s</td>
                <td>%s</td>
                <td>%s</td>
                <td>%s</td>
                <td><img src="%s" height=100 width=100> </td>
                <td>%s</td>
                <td>%s</td>
                <td>%s</td>
             </form> </tr>
               </tbody>""" % (i[0], i[1], fn1, i[3], i[4], i[5], i[6], i[7], i[8], i[9], fn2, i[11], i[12],i[13]))
print(""" </table>
</div>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.3/dist/js/bootstrap.bundle.min.js"></script>
</body>
</html>""")
