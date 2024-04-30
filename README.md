**Vendor Management System with Performance Metrics:**
This Vendor Management System (VMS) is a Django-based application designed to handle vendor profiles, track purchase orders, and calculate vendor performance metrics.

**Features**

**1. Vendor Profile Management**

Create, retrieve, update, and delete vendor profiles.

Track essential information such as name, contact details, address, and a unique vendor code.

**2. Purchase Order Tracking**

Create, retrieve, update, and delete purchase orders.

Track details like PO number, vendor reference, order date, items, quantity, and status.

**3. Vendor Performance Evaluation**

Calculate performance metrics including on-time delivery rate, quality rating average, average response time, and fulfillment rate.

Retrieve performance metrics for a specific vendor.

**Accessing the Folder**

1.Open the folder and activate the virtual environment by:

    /vendor_management_system/env/Scripts/activate.bat

2.The above will activate the virtualenvironment Because the virtualenvironment has all packages and modules present in it.
3.After activating the virtual environment we have to generate the token Because, it is a token based authentication by using the command:

    python manage.py generate_tokens

4.After this it will ask the user to enter the username in which you have created superuser for django it should be created by  using the following command:

    python manage.py createsuperuser

5.After this it will ask the username,emailid,password after entering this it will create the user then generate the token

6.The token will ask the username in which you have created at the time of creating the superuser.

7.The below image shows to how the token is generated:


![Screenshot (23)](https://github.com/harikrishnanakka/vendor/assets/152170400/f30cd308-b7b9-4d29-b1b3-d0b0316cab7c)

8.The above figure shows the details that how to generate the token.

9.After the token genration i was using the postman to test the CRUD operation is performing successfully or not.

10.For this open the Postman and in the Header section in the Key give the Authorzation and in the Value section give the token <genrated_token> as shown inn the below figure.

![Screenshot (16)](https://github.com/harikrishnanakka/vendor/assets/152170400/1f098228-1c8d-4169-883e-1816defc7b45)


11.After completion of the token section we have to do the CRUD operation by using the endpoints for that run the development server in the terminal:

           python manage.py runserver

12.After running the development server you can to CRUD opeartion by using the GET,POST,PUT,DELETE options.

**Vendor management**

13.Lets do the POST method for creating the record by usinng the endpoint:http://localhost:8000/api/vendors/

![Screenshot (17)](https://github.com/harikrishnanakka/vendor/assets/152170400/5fb8075b-8c4b-4c5a-948a-7657fe392885)


14.The POST method is succesfully created the record and it showing the 200 code it means record is created succesfully.

15.Lets retreive the data by using the GET method with the endpoint:http://localhost:8000/api/vendors/

![Screenshot (18)](https://github.com/harikrishnanakka/vendor/assets/152170400/bcb11b61-5530-45da-b11a-2c2f03c5f0c6)

16.The above shows the retreiving of the record and we can also modify the record by using the PUT method as shown in the below using the endpoint:http://localhost:8000/api/vendors/4/.


![Screenshot (24)](https://github.com/harikrishnanakka/vendor/assets/152170400/da9697be-346e-4065-bc90-10502e9a1c19)


17.Enter the data you want to modify in the json format select the POST method and send request.

18.You can also retrieve the specific data by usinng the id  like using the endpoint:http://localhost:8000/api/vendors/4/.

![Screenshot (25)](https://github.com/harikrishnanakka/vendor/assets/152170400/39bb82e3-eebd-4a54-826b-f9d74a2722ee)


19.Based on the provided id it will retrieve the specific data.

20.We can also Delete the specific data by using the id endpoint like:http://localhost:8000/api/vendors/4/.

![Screenshot (26)](https://github.com/harikrishnanakka/vendor/assets/152170400/25a2c414-e1e2-45fb-ac5a-3928b4d82f3a)

**Purchase order tracking**


1.Here also we have to the CRUD operation by using the API.

2.To create the record we have to use the POST method by using the endpoint:http://localhost:8000/api/purchase_orders/


 ![Screenshot (19)](https://github.com/harikrishnanakka/vendor/assets/152170400/45243d58-efbd-4e6b-b211-eeabb378bbc6)

3.The above shows the created record by using the POST method and lets go to the retreival of the data by using the GET method like usinng the endpoint:http://localhost:8000/api/purchase_orders/

![Screenshot (20)](https://github.com/harikrishnanakka/vendor/assets/152170400/c62e6bd9-9ea4-4812-8ba7-48833c43bb23)

4.We can also use the PUT method to modify the data and also we can retrieve the data by using the endpoint:http://localhost:8000/api/purchase_orders/4/


![Screenshot (21)](https://github.com/harikrishnanakka/vendor/assets/152170400/e882a5be-ec97-4327-a067-279d6d766780)

5.Based on the id the above data is retreived we can also DELETE by using the endpoint:http://localhost:8000/api/purchase_orders/4/


**Vendor Performance**


1.In this we have to retreive the performance data of the below points Based on the data provided for the vendor management and purcahse order tracking.

    vendor 
    date 
    on_time_delivery_rate
    quality_rating_avg 
    average_response_time
    fulfillment_rate

2.The above Points values will get based on the data provided the vendor is the id it will retrive if the status is completed then only it will retrive the data.

3.Based on the given endpoint and using the GET method it will retreive the data:http://localhost:8000/api/vendors/4/performance/

4.Here it will shows the data based on the vendor id.Below shows the image of the retreving the data.

![Screenshot (22)](https://github.com/harikrishnanakka/vendor/assets/152170400/8ec2ef75-4339-48b9-92de-a2e0920956be)

5.The above is the data retrived based on the performance.


Data Models

**1. Vendor Model**

name: Vendor's name.

contact_details: Contact information of the vendor.

address: Physical address of the vendor.

vendor_code: A unique identifier for the vendor.

on_time_delivery_rate: Percentage of on-time deliveries.

quality_rating_avg: Average rating of quality based on purchase orders.

average_response_time: Average time taken to acknowledge purchase orders.

fulfillment_rate: Percentage of purchase orders fulfilled successfully.

**2. Purchase Order (PO) Model**

po_number: Unique number identifying the PO.

vendor: Link to the Vendor model.

order_date: Date when the order was placed.

delivery_date: Expected or actual delivery date of the order.

items: Details of items ordered.

quantity: Total quantity of items in the PO.

status: Current status of the PO.

quality_rating: Rating given to the vendor for this PO.

issue_date: Timestamp when the PO was issued to the vendor.

acknowledgment_date: Timestamp when the vendor acknowledged the PO.

**3. Historical Performance Model**

vendor: Link to the Vendor model.

date: Date of the performance record.

on_time_delivery_rate: Historical record of the on-time delivery rate.

quality_rating_avg: Historical record of the quality rating average.

average_response_time: Historical record of the average response time.

fulfillment_rate: Historical record of the fulfillment rate.

**Technologys USED:**

1.python programming 2.Django framework  3.RestApi or Django rest framework  4.Db Sqlite

**______________________________________________________________________ThankYOU_____________________________________________________________________________________**
