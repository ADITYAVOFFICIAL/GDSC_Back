# main.py

## Imports

- `streamlit`: This library is used to create interactive web applications with Python.
- `requests`: This library allows making HTTP requests to interact with the backend server.

## Constants

- `BASE_URL`: This variable holds the base URL of the backend server where the product management API is hosted.

## Streamlit UI Functions

### view_all_details()

This function displays all product details by making a GET request to the `/products` endpoint of the backend server. It then displays the retrieved products on the Streamlit interface.

### add_data()

This function allows users to add a new product. It provides a text area for users to input product data in JSON format. Upon clicking the "Add" button, it sends a POST request to the backend server with the provided product data.

### delete_section()

This function enables users to delete a product by providing its ID. It takes the product ID as input and sends a DELETE request to the backend server's `/products/{product_id}` endpoint.

### update_fields_section()

This function allows users to update an existing product. It takes the product ID and updated product data as input. Upon clicking the "Update" button, it sends a PUT request to the backend server's `/products/{product_id}` endpoint with the updated product data.

## Main Function (`main()`)

This function sets up the Streamlit interface. It creates a sidebar for navigation with options to view all products, add a product, delete a product, or update a product. Depending on the selected navigation item, it calls the corresponding function to display the appropriate UI section.

## Execution Check

The `if __name__ == "__main__":` block ensures that the `main()` function is executed when the script is run directly.

Overall, this script provides a user-friendly interface to interact with a backend product management API, allowing users to view, add, delete, and update product data.
