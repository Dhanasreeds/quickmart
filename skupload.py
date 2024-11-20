#! C:/Users/dhanasree/AppData/Local/Programs/Python/Python312/python.exe
print("Content-type:text/html \r\n\r\n")
import cgi,cgitb,pymysql,os
form =cgi.FieldStorage()
Id=form.getvalue("id")
cgitb.enable()
con = pymysql.connect(host="localhost", user="root", password="", database="quickmart")
cur = con.cursor()
query = """select * from shop_register where id="%s" """% (Id)
cur.execute(query)
rec = cur.fetchall()
for i in rec:
    NAME= i[1]
    fn= "img/shop_register/shop_photo/" + i[2]
print("""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Product Upload</title>
    <link rel="stylesheet" href="css/skupload.css" />
     <link rel="stylesheet" href="css/admin_home.css">
       <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/js/bootstrap.bundle.min.js" integrity="sha384-MrcW6ZMFYlzcLA8Nl+NtUVF0sA7MsXsP1UyJoMp4YLEuNSfAP+JcXn/tWtIaxVXM" crossorigin="anonymous"></script>

      <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC" crossorigin="anonymous">

</head>
<body>
<div class ="containerfulid ">
      <div class="sidenav">
     <center> <img src="%s" class="rounded-circle"width="100px" height="100" ><br>
      <h2>%s</h2></center>
     """%(fn, NAME))
print("""
    <a href="shop_info.py?id=%s">Home</a>
      <a href="uploads.py?id=%s">Update product</a>
      <a href="product_list.py?id=%s">Product list</a>
      <a href="orders.py?id=%s">Placed order</a>
      <a href="previous_orders.py?id=%s">previous order</a>
      <a href="slogin.py">Log out</a>"""%(Id,Id,Id,Id,Id) )
print("""</div>
</div>
 <div class="con">
    <div class="container mx-15 my-5 py-4 px-4">
      <form  method="post" enctype="multipart/form-data" class="row g-3 needs-validation" >
        <div class="mb-3">
            <label for="productName" class="form-label">Enter Product Name</label>
            <input type="text" class="form-control"id="sName" name="sName" value="%s" required>
        </div>
        <div class="mb-3">
            <label for="productName" class="form-label">Enter Product Name</label>
            <input type="text" class="form-control"id="productName" name="Name" placeholder=" Product Name" required>
        </div>
         <div class="mb-3">
            <label for="Quantity" class="form-label">Enter Product Quantity</label>
            <input type="text" class="form-control" id="Quantity" name="Quantity" placeholder=" Quantity" required>
            <div class="invalid-feedback">
              Please provide a valid Product Price.
            </div>
         </div>
          <div class="mb-3">
            <label for="Price" class="form-label">Enter Product Price</label>
            <input type="text" class="form-control" id="Price" name="Price" placeholder=" Product Price" required>
            <div class="invalid-feedback">
              Please provide a valid Product Price.
            </div>
          </div>
         <div class="mb-3">
           <label for="unit" class="form-label"   >Choose Product unit</label>
           <select class="form-control" aria-label="unit" id="unit" name="unit" placeholder=" Product unit" required>
            <option selected> </option>
             <option value="grams">grams</option>
             <option value="kilograms">kilograms</option>
             <option value="liters">liters</option>
             <option value="milliliter">milliliters</option>
           </select>
           <div class="invalid-feedback">
             Please provide a valid Product Price.
           </div>
         </div>
         
          <label for="image" class="form-label">Upload Product image</label>
          <div class="input-group mb-3">
            <input type="file" class="form-control" id="image" name="image" aria-describedby="inputGroupFileAddon04" aria-label="Upload" required >
            <div class="invalid-feedback">
              Please provide a valid Product image.
            </div>
          </div>
          <div class="mb-3">
            <label for="description" class="form-label">Enter product description</label>
            <textarea class="form-control" id="description"  rows="3" cols="30" placeholder="description" name="description"required></textarea>
            <div class="invalid-feedback">
              Please provide a valid Product description.
            </div>
          </div>
          <div class="mb-3">
            <input class="btn " type="submit" name="upload" id="button" value="upload">
          </div>
      </form>  
    </div>
 </div>

</body>
</html>"""%(NAME) )
form = cgi.FieldStorage()
pl = form.getvalue("upload")

if pl != None:
    pn = form.getvalue("Name")
    pq = form.getvalue("Quantity")
    pp = form.getvalue("Price")
    pu = form.getvalue("unit")
    pi = form["image"]
    pd = form.getvalue("description")

    if pi.filename:
        fn = os.path.basename(pi.filename)
        open("img/product_upload/" + fn, 'wb').write(pi.file.read())

        query = """insert into product_upload(shop_name, product_name, product_quantity, product_price, units, product_image, product_description)values('%s', '%s','%s','%s','%s','%s','%s')""" %(NAME, pn, pq, pp, pu, fn, pd)
        cur.execute(query)
        con.commit()
        print("""
           <script>
           alert("upload successfully!!!");
           location.href = "admin_home.py"
           </script>
        """)


