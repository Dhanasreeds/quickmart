#! C:/Users/dhanasree/AppData/Local/Programs/Python/Python312/python.exe
print("Content-type:text/html \r\n\r\n")

print("""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Admin login</title>
    <link rel="stylesheet" href="css/admin.css" />
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC" crossorigin="anonymous">
</head>
<body>
     <div class="con" id="con">
              <h1>Welcome You </h1>
                  <h3 > Login here</h3>
                  <form class="row g-3 needs-validation my-3" method="post" validate>
                    <div class="row">
                      <div class="col-md-12">
                        <label for="aname" class="form-label">User name</label>
                        <div class="input-group has-validation">
                          <input type="text" class="form-control" name="admin_name" id="aname" aria-describedby="inputGroupPrepend" required>
                          <div class="invalid-feedback">
                            Please enter your user name.
                          </div>
                        </div>
                      </div>           
                    </div><br>
                    <div class="row">
                      <div class="col-md-12">
                        <label for=">Password" class="form-label">Password</label>
                        <div class="input-group has-validation">
                          <input type="password" name="admin_password" class="form-control" id="Password" aria-describedby="inputGroupPrepend" required>
                          <div class="invalid-feedback">
                            Please enter your password.
                          </div>
                        </div>
                      </div>           
                    </div><br>

              <div class="col-12">
                <input class="btn btn-primary" type="submit" name="submit" value="submit">
              </div>
          </form>  

        </div>  
          <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/js/bootstrap.bundle.min.js" integrity="sha384-MrcW6ZMFYlzcLA8Nl+NtUVF0sA7MsXsP1UyJoMp4YLEuNSfAP+JcXn/tWtIaxVXM" crossorigin="anonymous"></script>
      </body>
</html>""")
import cgi

form = cgi.FieldStorage()
sm = form.getvalue("submit")
if sm != None:
    an = form.getvalue("admin_name")
    ap = form.getvalue("admin_password")
    if an == "Admin@quickmart" and ap == "QM@Admin":
        print("""
             <script>
             alert("Logged in Successfully!");
             location.href = "admin_home.py"
             </script>
        """)
    else:
        print("""
                    <script>
                     alert("Logged in failed");
                     location.href = "alogin.py"
                     </script>
                """)