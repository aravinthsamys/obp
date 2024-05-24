






# for draft


# owner_name=request.POST.get("owner_name")
        # gender=request.POST.get("gender")
        # company_name=request.POST.get("company_name")
        # category=request.POST.get("category")
        # gstin_number=request.POST.get("gstin_number")
        # city=request.POST.get("city")
        # company_address=request.POST.get("company_address")
        # pincode=request.POST.get("pincode")
        # contact_number=request.POST.get("contact_number")
        # email_id=request.POST.get("email_id")
        # photocopy=request.POST.get("photocopy")
        # website_link=request.POST.get("website_link")
        # gmaps_link=request.POST.get("gmaps_link")
        # open_time=request.POST.get("open_time")
        # close_time=request.POST.get("close_time")

        # data1=businessdata(owner_name=owner_name,gender=gender,company_name=company_name,category=category,gstin_number=gstin_number,
        #                  city=city,company_address=company_address,pincode=pincode,contact_number=contact_number,
        #                        email_id=email_id,photocopy=photocopy,website_link=website_link,gmaps_link=gmaps_link,
        #                         open_time=open_time,close_time=close_time)
        # data1.save()

  # if request.method=='POST':
    #    searched=request.POST.get("searched")
    #    search=businessdata.objects.filter(town_address__contains=searched).order_by("-id")
    #    return render(request,'indexauth/alldata.html',{'Businessdata':search})
    # else:


#         <!-- mobile view -->

# <div class="mobileviewstyle">

#   <form action="" method="post" enctype="multipart/form-data" >
#     {% csrf_token %}
#     <h3 class="topicbusiness" style="text-align: center;text-decoration: underline;text-underline-offset: 20px;text-decoration-color: #501779;color: #501779;font-family:'Times New Roman', Times, serif;"> &nbsp; Business Details &nbsp; </h3> <br> <br>

    

# <label for="">Owner Name</label> </td><td class="semicolontd">: &nbsp; &nbsp; <br>
#   <td class="endtd"> <input type="text" name="owner_name" onkeydown="return /[a-zA-Z]/i.test(event.key)" required></td> <br> <br>

# <label for="">Gender</label></td><td class="semicolontd">: &nbsp; &nbsp;</td> <br>
#   <td class="endtd"><select name="gender" id="">
#          <option value="Male">Male</option>
#          <option value="Female">Female</option>
#          <option value="Transgender">Transgender</option>
#        </select> </td><br> <br>

#        <td><label for="">Company</label></td><td class="semicolontd">: &nbsp; &nbsp;</td> <br>
#        <td class="endtd"><input type="text" name="company_name" required></td> <br> <br>

#        <td><label for="">Business Description</label></td><td class="semicolontd">: &nbsp; &nbsp;</td> <br>
#       <td class="endtd"><input type="text" name="description" required></td> <br> <br>

#       <td><label for="">Category</label></td><td class="semicolontd">: &nbsp; &nbsp;</td> <br>
#       <td class="endtd"><select name="category" id="">
#             <option value="retail">Retail</option>
#             <option value="hospitality">Hospitality</option>
#             <option value="healthcare">Healthcare</option>
#             <option value="technology">Technology</option>
#             <option value="finance">Finance</option>
#             <option value="education">Education</option>
#             <option value="manufacturing">Manufacturing</option>
#             <option value="real-estate">Real Estate</option>
#             <option value="transportation">Transportation</option>
#             <option value="agriculture">Agriculture</option>
#             <option value="entertainment">Entertainment</option>
#             <option value="consulting">Consulting</option>
#             <option value="others">others</option>
#       </select></td> <br> <br>
  
#       <td><label for="">GSTIN Number</label></td><td class="semicolontd">: &nbsp; &nbsp;</td> <br>
#       <td class="endtd"><input name="gstin_number" type="text" id="txtGSTIN" pattern="^[0-9]{2}[A-Z]{5}[0-9]{4}[A-Z]{1}[1-9A-Z]{1}Z[0-9A-Z]{1}$" title="Invalid GST Number." /></td>
#     <br> <br>


#       <td><label for="">City</label></td><td class="semicolontd">: &nbsp; &nbsp;</td> <br>
#       <td class="endtd"><select name="city" id="">
#         <option value="Namakkal">Namakkal</option>
#       </select></td> <br> <br>
    
#       <td><label for="">Address</label></td><td class="semicolontd">: &nbsp; &nbsp;</td> <br>
#       <td class="endtd"><input name="company_address" type="text" required></td> <br> <br>
   
#       <td><label for="">PinCode</label></td><td class="semicolontd">: &nbsp; &nbsp;</td> <br>
#       <td class="endtd"><input type="number" name="pincode" id="myKadA" onkeydown="limit(this, 6);" onkeyup="limit(this, 6);" onkeyup="this.value = minmax(this.value, 0, 6)" required></td>
# <br> <br>

#       <td><label for="">Contact Number</label></td><td class="semicolontd">: &nbsp; &nbsp;</td> <br>
#       <td class="endtd"><input type="text" id="phone" name="contact_number" onkeypress="phoneno()" maxlength="10" required> </td>
#     <br> <br>

 
#       <td><label for="">E-mail</label></td><td class="semicolontd">: &nbsp; &nbsp;</td> <br>
#       <td class="endtd"><input name="email_id" type="email" > </td> <br> <br>
   

#       <td><label for="">Logo/Photocopy </label></td><td class="semicolontd">: &nbsp; &nbsp; </td> <br>
#       <td class="endtd"><input name="photocopy" type="file" style="border: none;"></td> <br> <br>
 

#       <td><label for="">Website link</label></td><td class="semicolontd">: &nbsp; &nbsp;</td> <br>
#       <td class="endtd"><input name="website_link" type="text"></td> <br> <br>
  
#       <td><label for="">Google Maps Link</label></td><td class="semicolontd">: &nbsp; &nbsp;</td> <br>
#       <td class="endtd"><input name="gmaps_link" type="text"></td> <br> <br>
   

#     <td><label for="">Business Type</label></td><td class="semicolontd">: &nbsp; &nbsp;</td> <br>
#         <td class="endtd"><select name="business_work_type" id="">
  
#           <option value="Part-time">Part-time</option>
#           <option value="Full-time">Full-time</option>
#         </select></td> <br> <br>


#       </div>




#<!-- <img class="servimg"  src="{{ item.photocopy.url }}" alt="network error"> -->
