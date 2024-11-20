#! C:/Users/dhanasree/AppData/Local/Programs/Python/Python312/python.exe
print("Content-type:text/html \r\n\r\n")
import cgi,cgitb,pymysql
form =cgi.FieldStorage()
Id=form.getvalue("id")
cgitb.enable()
con = pymysql.connect(host="localhost", user="root", password="", database="quickmart")
cur = con.cursor()
query = """select * from user_register where id="%s" """% (Id)
cur.execute(query)
rec = cur.fetchall()
q1 = """select * from shop_register where status="Approved" """
cur.execute(q1)
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

</head>
<body class="bg-dark">

        <nav class="navbar navbar-expand-md navbar-dark bg-dark px-4">
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
                        <li><a class="dropdown-item" href="login.py"><i class='fas fa-power-off' ></i> Logout</a></li>
                    </ul>
                  </div>
                    <a class="btn btn-outline-light  me-2" href="addtocart.py?id=%s" role="button">
                    cart
                    </a>
                    <a class="btn btn-outline-light  me-2" href="user_orders.py?id=%s" role="button">
                    view orders
                    </a>
                    
                    """%(Id,Id,Id))
                  
                    
print(""" 
              </div>
            </div>
        </nav>
        <div class="slide_container">
          <button class="carousel-control-prev" type="button" data-bs-target="#carouselExampleControls" data-bs-slide="prev">
            <span class="carousel-control-prev-icon" aria-hidden="true"></span>
            <span class="visually-hidden">Previous</span>
          </button>
          <button class="carousel-control-next" type="button" data-bs-target="#carouselExampleControls" data-bs-slide="next">
            <span class="carousel-control-next-icon" aria-hidden="true"></span>
            <span class="visually-hidden">Next</span>
          </button>
          <div id="carouselExampleControls" class="carousel slide" data-bs-ride="carousel">
            <div class="carousel-inner">
                <div class="carousel-item active">
                  <img height="600px" src="img/src/spices2.avif" class="d-block w-100" alt="...">
                </div>
                <div class="carousel-item">
                  <img  height="600px"src="img/src/veg2.avif" class="d-block w-100" alt="...">
                </div>
                <div class="carousel-item">
                  <img height="600px"src="img/src/dairy2.jpg" class="d-block w-100" alt="...">
                </div>
                <div class="carousel-item">
                  <img height="600px"src="img/src/Bakery2.jpeg" class="d-block w-100 h-" alt="...">
                </div>
                <div class="carousel-item">
                  <img height="600px" src="img/src/frurits.jpeg" class="d-block w-100" alt="...">
                </div>
                <div class="carousel-item">
                  <img height="600px"src="img/src/Personal Care2.jpg" class="d-block w-100" alt="...">
                </div>
                <div class="carousel-item">
                  <img height="600px" src="img/src/baby2.webp" class="d-block w-100" alt="...">
                </div>
                <div class="carousel-item">
                  <img height="600px"src="img/src/Pasta, Rice & Cereal2.jpeg" class="d-block w-100" alt="...">
                </div>
                <div class="carousel-item">
                  <img height="600px"src="img/src/Health Care2.png" class="d-block w-100" alt="...">
                </div>
                <div class="carousel-item">
                  <img height="600px"src="img/src/snacks2.jpeg" class="d-block w-100" alt="...">
                </div>
            </div>
          </div><br>
          
    <div class="row mx-5 my-2">""")

for i in rec:
    NAME = i[1]
    fn = "img/shop_register/shop_photo/" + i[2]

    print("""
        <div class="col-md-3 col-sm-6 my-2 ">
           <div class="card h-40 border" style="box-shadow: 0 4px 8px rgba(0, 0, 0, 0.3);">
                <img src="%s" class="card-img-top" alt="Product Image">
                <div class="card-body">
                    <a href="products.py?sid=%s&uid=%s"><h5 class="card-title">%s</h5></a>
                </div>
            </div>
        </div>
    """ % (fn,i[0],Id,NAME))
print("""
    </div>
</div> 
            
      <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/js/bootstrap.bundle.min.js" integrity="sha384-MrcW6ZMFYlzcLA8Nl+NtUVF0sA7MsXsP1UyJoMp4YLEuNSfAP+JcXn/tWtIaxVXM" crossorigin="anonymous"></script>
</body>
</html>""")
