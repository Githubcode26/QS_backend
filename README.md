# Backend Test #
____

As a new developer at SpeedyBoats, your first task is to help the operational team to manage orders 
and create some metrics.

They have asked you to create an API for them, based on the boilerplate code which they have provided for you.

Selling a boat is hard, it takes a lot of negotiation, this is why every boat has a __list price__ but the sale could happen on a different price. 
Let's call that __actual price__. 

Your tasks:
1. create the endpoints to manage the Orders 
2. create a special endpoint and calculate the discount percentage by product. 
___

__Discount Percentage for a product__

discount percentage = (1 - (total actual price / total list price) ) * 100


__Start Script__

Before you start the development, run the start script to populate the database with some default data.
There are 2 tables: Products and Orders. You don't have to worry about Products, it is populated for your convenience

```
python setup/init_db.py
```

### Your Task ###
1. Create API for Orders to help the sales team manage them.
When listing the Orders there should be an option to filter the response for a particular product


2. Create a special endpoint for the metrics. 
This endpoint doesn't accept any parameter just returns the discount percentage per product based on the orders

# How to run task for finding endpoints #
1. Copy repository URL and clone it in local project folder by using following commad
   **git clone (repo URL)**
2. Run the start script to populate the database with the following command
   **python setup/init_db.py**
3. install the packages in requirements.txt by following command
   **pip install -r requirements.txt**
4. The flask command line arguments need to know what module to locate the current **Flask app** instance in. For that set FLASK_APP as a environment varibble.
  **Unix bash (linux, mac etc)**
   $ export FLASK_APP = main
   $ export FLASK_DEBUG = 1
   $ flask run
  **Windows CMD (linux, mac etc)**
   > set FLASK_APP = main
   > set FLASK_DEBUG = 1
   > flask run
   
 5. To access endpoints once the flask application is running copy the URL i.e 127.0.0.1:5000, open postman ( or any other rest client)
   5.1 ## Order endpoint ## (127.0.0.1:5000/orders) :
        a. To list the orders flask maps http request to python function. Here when we connect to flask server at 127.0.0.1:5000/orders then flask    check if there is match between the path provided and the defined function. Here it is mapped to @orders_pages.route('/', method = ['GET']. The function list order is called which takes the value from postman key value pair(in the 'form-data' option under 'body' tab)for 'name' key used as filter to show orders based on particular order.
        
  example:      GET -- 127.0.0.1:5000/orders
                key   |  value
                name  |  Narrowboat
   
 result:         [
                {
                    "actual_price": 179,
                    "order_id": 35
                },
                {
                    "actual_price": 500,
                    "order_id": 38
                },
                {
                    "actual_price": 390,
                    "order_id": 39
                }
            ]
              
      ## 5.2  Listing order endpoint by order id  ((127.0.0.1:5000/orders/order_id) : ##
             example:      GET -- 127.0.0.1:5000/orders/35
               
             result: {
                                  "actual_price": 179,
                                  "order_id": 35,
                                  "product_id": 3
                      }
      5.3 ## Deleting order endpoint by order id ## ((127.0.0.1:5000/orders/order_id)
             example:      DELETE -- 127.0.0.1:5000/orders/35
             
      5.4 ## Updating order endpoint by order id ## ((127.0.0.1:5000/orders/order_id)   
              example:     PUT    -- 127.0.0.1:5000/orders/30
                           key          |  value
                           actualprice  |  1000
                           productid    |  4
      5.5 ## Posting order endpoint  ## ((127.0.0.1:5000/orders/)   
              example:     POST    -- 127.0.0.1:5000/orders/30
                           key          |  value
                           actualprice  |  2034
                           productid    |  2
              result:   Order is Successfully created with id:43
      5.6 ## special metrics discount endpoint  ## ((127.0.0.1:5000/orders/metrics) displays discounts per product
              example:     GET    -- 127.0.0.1:5000/orders/metrics
              result:      [
                                "Catamaran",
                                "65.20",
                                "Narrowboat",
                                "11.00",
                                "Submarine",
                                "18.69"
                            ]
   
