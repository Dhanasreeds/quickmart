#! C:/Users/dhanasree/AppData/Local/Programs/Python/Python312/python.exe
print("Content-type:text/html \r\n\r\n")

print("""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>home</title>
    <link rel="stylesheet" href="css/style.css">
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
                    <a class="btn btn-outline-light dropdown-toggle me-2" href="#" role="button" id="dropdownMenuLink" data-bs-toggle="dropdown" aria-expanded="false">
                     Register 
                    </a>
                    <ul class="dropdown-menu" aria-labelledby="dropdownMenuLink">
                      <li><a class="dropdown-item" href="shop_register.py">Shop Keeper</a></li>
                      <li><a class="dropdown-item" href="Register.py">Customer</a></li>
                    </ul>
                  </div>
                  <div class="dropdown">
                    <a class="btn btn-outline-light dropdown-toggle me-2" href="#" role="button" id="dropdownMenuLink" data-bs-toggle="dropdown" aria-expanded="false">
                    Login
                    </a>
                    <ul class="dropdown-menu" aria-labelledby="dropdownMenuLink">
                        <li><a class="dropdown-item" href="alogin.py">Admin</a></li>
                      <li><a class="dropdown-item" href="slogin.py">Shop Keeper</a></li>
                      <li><a class="dropdown-item" href="login.py">Customer</a></li>
                    </ul>
                  </div>
                <form class="d-flex">
                  <input class="form-control me-2" type="search" placeholder="Search" aria-label="Search">
                  <button class="btn btn-outline-light" type="submit">Search</button>
                </form>

              </div>
            </div>
          </nav>
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
          </div>

            </div>
        </div>
      </div>
      <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/js/bootstrap.bundle.min.js" integrity="sha384-MrcW6ZMFYlzcLA8Nl+NtUVF0sA7MsXsP1UyJoMp4YLEuNSfAP+JcXn/tWtIaxVXM" crossorigin="anonymous"></script>
</body>
</html>""")
