# PickVisa
This is basic instructions to make it easy for you to go over the project.
First of all we have CRUD API  
1. Create a customer

<img width="825" alt="Screen Shot 2022-08-07 at 00 49 08" src="https://user-images.githubusercontent.com/79960958/183266042-0ddc958e-7808-4200-886d-e8bc2e40ac23.png">

2. Get all customers

<img width="789" alt="Screen Shot 2022-08-07 at 00 49 19" src="https://user-images.githubusercontent.com/79960958/183266043-57ca7d27-2c37-412a-b3d2-28ff7807d0eb.png">

3. Get, Delete or Update certain customer (Same applies to Passports)

<img width="770" alt="Screen Shot 2022-08-07 at 00 50 02" src="https://user-images.githubusercontent.com/79960958/183266044-ff5a20e0-0a36-4fb9-bdbf-cb98cd9add19.png">

4. Get all passports
<img width="814" alt="Screen Shot 2022-08-07 at 00 51 35" src="https://user-images.githubusercontent.com/79960958/183266045-5d087763-a781-45aa-ba3f-109462da00f2.png">

5. Create customer and passports under same endpoint. You have to send passport data inside customer object like a list of dictioneries. You don't have to write customer id again inside passports, it will be set afterwards. Sample data:

<img width="807" alt="customer-passport together" src="https://user-images.githubusercontent.com/79960958/183266243-4706b8b6-d288-4046-9df7-cfe72f9cf594.png">

6. To scan file you can execute scan_file.py file or it will be called when you try to create passport under passports/ endpoint. This one didn't have clear instructions on how should I associate it with other code blocks or not, so wrote 2 examples. Here I used Railway Oriented Programming approach and I used contractsPY library. And when sent an image I got this:

<img width="1032" alt="xmlfile" src="https://user-images.githubusercontent.com/79960958/183266373-e8034d2b-5abd-4217-afe1-a4fedbd9c070.png">
