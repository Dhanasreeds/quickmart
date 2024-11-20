#! C:/Users/dhanasree/AppData/Local/Programs/Python/Python312/python.exe
print("Content-type:text/html \r\n\r\n")

import cgi, cgitb, pymysql

cgitb.enable()
con = pymysql.connect(host="localhost", user="root", password="", database="quickmart")
cur = con.cursor()
print("""<!DOCTYPE html>

<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Register</title>
    <link rel="stylesheet" href="css/register.css" />
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC" crossorigin="anonymous">

</head>
<body >
    <div class="con ">
      <h1>Welcome You </h1>
            <h3 > Register here</h3>
            <form class="row g-3 needs-validation my-3"  enctype="multipart/form-data" method="post" validate>
              <div class="row">
                <div class="col-md-12">
                  <label for="Name" class="form-label">Name</label><span> *</span> 
                  <input type="text" class="form-control" id="Name" name="Name" required>
                  <div class="valid-feedback">                   
                  </div>
                </div>
              </div><br>
              <div class="row">
                <div class="col-md-12">
                  <label for="Mail id" class="form-label">Mail id</label><span> *</span> 
                  <div class="input-group has-validation">
                    <input type="email" class="form-control" id="Mail id" name="Mail_id"aria-describedby="inputGroupPrepend" required>
                    <div class="invalid-feedback">
                      Please choose a username.
                    </div>
                  </div>
                </div>           
              </div><br>
              <div class="row">
                <div class="col-md-12">
              <label for="Mobile"class="form-label">Mobile Number</label><span> *</span> 
              <div class="input-group has-validation">
              <input type="number" name="Mobile" id="Mobile"class="form-control" aria-describedby="inputGroupPrepend" required>
              <div class="invalid-feedback">
                Please Enter your Mobile number.
              </div>
            </div>
          </div>           
        </div><br>
                <div class="row ">
                    <div class="col-md-12">
                        <label for="Password" class="form-label">Password</label><span> *</span> 
                          <input type="password" class="form-control" id="Password" name="Password"required>                
                        <div class="invalid-feedback">
                            Please Enter a Password.
                          </div>
                      </div>
                </div><br>
                <div class="row ">
                    <div class="col-md-12">
                        <label for="confrim Password" class="form-label">confirm Password</label><span> *</span>                   
                          <input type="password" class="form-control" id="confrim Password" name="confrim_Password" required>                  
                        <div class="invalid-feedback">
                            Please Re-enter a Password.
                          </div>
                      </div><br>
                      <div class="row ">
                        <div class="col-md-12">
                      <label for="Gender" class="form-label">Gender</label><br>
                      <input type="radio" name="Gender" id="Gender" value="Male" >
                      <label for="Male">Male</label>
                      <input type="radio" name="Gender" id="Gender" value="Female" >
                      <label for="Female">Female</label>
                    </div>
                  </div><br>
                  <div class="row ">
                    <div class="col-md-12">
                      <label for="Address"class="form-label">Address<span> *</span> </label><br>
                      <textarea name="Address" id="fAddress"class="form-control" cols="160" rows="3" ></textarea><br>
                    </div>
                  </div><br>

                  <div class="row ">
                    <div class="col-md-12">
                  <label for="City" class="form-label">City</label>   
                  <input type="text" class="form-control" aria-label="City" id="City" name="City">
                </div>
              </div><br>
              <div class="row ">
                <div class="col-md-12">
              <label for="pincode" class="form-label">Pincode</label>   
              <input type="number" class="form-control" aria-label="pincode" id="pincode" name="pincode">
            </div>
          </div><br>
              <div class="row ">
                <div class="col-md-12">
                 <label for="State" class="form-label">State</label>   
                 <input type="text" class="form-control" aria-label="State" id="State" name="State">
                </div>
              </div><br>
              <div class="row ">
               <div class="col-md-12">
               <label for="Nationality" class="form-label">Nationality</label>   
               <input type="text" class="form-control" aria-label="Nationality" id="Nationality" name="Nationality">
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
                </div><br><br>
                <div class="col-12">
                  <input class="btn btn-primary" type="submit" value="submit" name="submit">
                </div>
              </form><br><br>
              <h6>If you already register then <span><a href="login.py">login</a></span></h6> 
    </div>



     <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/js/bootstrap.bundle.min.js" integrity="sha384-MrcW6ZMFYlzcLA8Nl+NtUVF0sA7MsXsP1UyJoMp4YLEuNSfAP+JcXn/tWtIaxVXM" crossorigin="anonymous"></script>
</body>
</html>""")
form = cgi.FieldStorage()
sm = form.getvalue("submit")
if sm != None:
    un = form.getvalue("Name")
    um = form.getvalue("Mail_id")
    mn = form.getvalue("Mobile")
    pw = form.getvalue("Password")
    cpw = form.getvalue("confrim_Password")
    gn = form.getvalue("Gender")
    ad = form.getvalue("Address")
    cn = form.getvalue("City")
    pc = form.getvalue("pincode")
    stn = form.getvalue("State")
    nt = form.getvalue("Nationality")

    query = """insert into user_register(user_name,Mail_id,Mobile_num,Password,confrim_Password,Gender,Address,City,pincode,state,Nationality)values('%s','%s',%s,'%s','%s', '%s','%s','%s',%s,'%s','%s' )""" % (
    un, um, mn, pw, cpw, gn, ad, cn, pc, stn, nt)
    cur.execute(query)
    con.commit()
    print("""
        <script>
        alert("Registered Successfully!");
        location.href = "login.py"
        </script>
      """)
else:
    print("""
                <script>
                alert("Registered failed!");
                location.href = "register.py"
                <script>
              """)