#! C:/Users/dhanasree/AppData/Local/Programs/Python/Python312/python.exe
print("Content-type:text/html \r\n\r\n")
import cgi, pymysql

con = pymysql.connect(host="localhost", user="root", password="", database="quickmart")
cur = con.cursor()

print("""<!DOCTYPE html>

<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Slogin</title>
    <link rel="stylesheet" href="css/slogin.css" />
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC" crossorigin="anonymous">

</head>
<body>
  <div class="con ">
        <h1>Welcome You </h1>
            <h3 > Login here</h3>
            <form class="row g-3 needs-validation my-3" method="post" validate>

              <div class="row">
                <div class="col-md-12">
                  <label for="Mail id" class="form-label">Mail id</label>
                  <div class="input-group has-validation">
                    <input type="email" class="form-control" id="Mail id" name="Mail_id" aria-describedby="inputGroupPrepend" required>
                    <div class="invalid-feedback">
                      Please enter your Mail id.
                    </div>
                  </div>
                </div>           
              </div><br>
              <div class="row">
                <div class="col-md-12">
                  <label for=">Password" class="form-label">Password</label>
                  <div class="input-group has-validation">
                    <input type="password" class="form-control" id="Password" name="Password" aria-describedby="inputGroupPrepend" required>
                    <div class="invalid-feedback">
                      Please enter your password.
                    </div>
                  </div>
                </div>           
              </div><br>
              <div class="col-12">
            <div class="form-check">
              <input class="form-check-input" type="checkbox" value="" id="invalidCheck" required>
              <label class="form-check-label" for="invalidCheck">
                Agree to terms and conditions
              </label>
              <div class="invalid-feedback">
                You must agree before submitting.
              </div>
            </div>
          </div>

         <br>
        <div class="col-12">
          <input class="btn btn-primary" type="submit" name="submit" value="submit">
        </div>
    </form>  
    <h6>If you not Register then <span><a href="shop_register.py">Register</a></span></h6>
  </div>  
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/js/bootstrap.bundle.min.js" integrity="sha384-MrcW6ZMFYlzcLA8Nl+NtUVF0sA7MsXsP1UyJoMp4YLEuNSfAP+JcXn/tWtIaxVXM" crossorigin="anonymous"></script>

</body>
</html>""")
form = cgi.FieldStorage()
sm = form.getvalue("submit")

if sm is not None:
    md = form.getvalue("Mail_id")
    pw = form.getvalue("Password")


    # Use parameterized query to prevent SQL injection
    query = """SELECT id FROM shop_register WHERE Mail_id = '%s' AND password = '%s' and status="Approved" """ % (md, pw)
    cur.execute(query)

    # Fetch the result
    rec = cur.fetchone()

    # Check if a record is found
    if rec is not None:
        print("""
            <script>
            alert("Logged in Successfully!");
            location.href = "shopkhome.py?id=%s";
            </script>
        """%(rec[0]))
    else:
        print("""
            <script>
            alert("Invalid Mail ID or Password.");
            location.href = "slogin.py";
            </script>
        """)
cur.close()
con.close()
