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
    <title>Document</title>
    <link rel="stylesheet" href="css/prdlist.css">
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC" crossorigin="anonymous">

</head>
<body>
<div class="container mt-5">
    <div class="row">""")

for i in rec:
    NAME = i[1]
    fn = "img/shop_register/shop_photo/" + i[2]

    print("""
        <div class="col-md-3 col-sm-6">
           <div class="card h-40 border" style="box-shadow: 0 4px 8px rgba(0, 0, 0, 0.3);">
                <img src="%s" class="card-img-top" alt="Product Image">
                <div class="card-body">
                    <a href="products.py?id=%s"><h5 class="card-title">%s</h5></a>
                </div>
            </div>
        </div>
    """ % (fn,i[0], NAME))
print("""
    </div>
</div> 
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/js/bootstrap.bundle.min.js" integrity="sha384-MrcW6ZMFYlzcLA8Nl+NtUVF0sA7MsXsP1UyJoMp4YLEuNSfAP+JcXn/tWtIaxVXM" crossorigin="anonymous"></script>

</body>
</html>""")