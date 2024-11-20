#! C:/Users/dhanasree/AppData/Local/Programs/Python/Python312/python.exe
print("Content-type:text/html \r\n\r\n")

import cgi, cgitb, pymysql
form = cgi.FieldStorage()
cgitb.enable()
con = pymysql.connect(host="localhost", user="root", password="", database="quickmart")
cur = con.cursor()
Id = form.getvalue("id")
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
  <div class="con">""")
print("""<center> <img src="%s" class="rounded-circle"width="100px" height="100" ><br>
      <h2>%s</h2></center>
     """ % (fn, NAME))
print("""
 <table class="table  table-secondary table-hover table-bordered mx-3 ">
 <tbody>
          <tr><form method="post" >
               <td>Shop Name</td> 
               <td><input type="text" class="form-control" id="sName" name="sName" value="%s" readonly ></td>
             </form> 
          </tr>
          <tr><form method="post" >
               <td>Address</td> 
               <td><input type="text" class="form-control" id="sName" name="Address" value="%s" ></td>
             </form> 
          </tr> 
          <tr><form method="post">
               <td>City</td> 
               <td><input type="text" class="form-control" id="sName"  name="City"value="%s" ></td>
             </form> 
          </tr>  
          <tr><form method="post" >
               <td>Pincode</td> 
               <td><input type="text" class="form-control" id="sName" name="pincode" value="%s" ></td>
             </form> 
          </tr>  
          <tr><form method="post" >
               <td>State</td> 
               <td><input type="text" class="form-control" id="sName" name="State" value="%s"></td>
             </form> 
          </tr>  
          <tr><form method="post">
               <td>Nationality</td> 
               <td><input type="text" class="form-control" id="sName" name="Nationality"value="%s" ></td>
             </form> 
          </tr>  
          <tr><form method="post">
               <td>shop owner Name</td> 
               <td><input type="text" class="form-control" id="sName" name="oName"value="%s" ></td>
             </form> 
          </tr>  
          <tr><form method="post" >
               <td>Gender</td> 
               <td><input type="text" class="form-control" id="sName" name="Gender" value="%s"></td>
             </form> 
          </tr>  
          <tr><form method="post">
               <td>Mail id</td> 
               <td><input type="text" class="form-control" id="sName" name="Mail id"value="%s" readonly></td>
             </form> 
          </tr>
          <tr><form method="post" >
               <td>Password</td> 
               <td><input type="text" class="form-control" id="sName" name="password" value="%s" ></td>  
          </tr>  
          <tr><form method="post">
               <td>Mobile Number</td> 
               <td><input type="text" class="form-control" id="sName" name="Mobile" value="%s" ></td>
             </form> 
          </tr>   
         <center><tr><form method="post" >
         <td colspan=2><input type="submit" name="Update" value="Update" class="btn btn-info"></td>
          </form> 
         <tr></center>
          
        </tbody>
"""%(NAME,i[3],i[4],i[5],i[6],i[7],i[8],i[9],i[11],i[12],i[13]))
   
print(""" 
</table>  
</div>
</body>
</html>""")
sm = form.getvalue("Update")
if sm != None:
    sn = form.getvalue("sName")
    ad = form.getvalue("Address")
    cn = form.getvalue("City")
    pc = form.getvalue("pincode")
    stn = form.getvalue("State")
    nt = form.getvalue("Nationality")
    on = form.getvalue("oName")
    gn = form.getvalue("Gender")
    mid = form.getvalue("Mail_id")
    ps = form.getvalue("password")
    mn = form.getvalue("Mobile")
    qry="""update shop_register set shop_name='%s',shop_address='%s',City='%s',pincode=%s,state='%s',Nationality='%s',owner_name='%s',Gender='%s',Mail_id='%s',password='%s',	Mobile=%s where id=%s """ % (sn, ad, cn, pc, stn, nt, on, gn, mid, ps, mn,Id)
    cur.execute(qry)
    con.commit()
    print(qry)
    print("""
       <script>
              alert("Update successfully!!!");
       </script>
      """)