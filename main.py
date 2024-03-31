import streamlit as st
import requests
import json


# Function to get all products
def get_products():
    response = requests.get("http://127.0.0.1:5000/products")
    if response.status_code == 200:
        products = response.json()
        return products
    else:
        return []


# Function to get product details by ID
def get_product_details(product_id):
    response = requests.get(f"http://127.0.0.1:5000/products/{product_id}")
    if response.status_code == 200:
        product_details = response.json()
        return product_details
    else:
        return None


# Function to add a product
def add_product(product_data):
    response = requests.post("http://127.0.0.1:5000/products", json=product_data)
    return response.json()


# Function to update a product
def update_product(product_id, product_data):
    response = requests.put(f"http://127.0.0.1:5000/products/{product_id}", json=product_data)
    return response.json()


# Function to add a variant
def add_variant(product_id, variant_data):
    response = requests.post(f"http://127.0.0.1:5000/products/{product_id}/variants", json=variant_data)
    return response.json()


# Function to update a variant
def update_variant(product_id, variant_id, variant_data):
    response = requests.put(f"http://127.0.0.1:5000/products/{product_id}/variants/{variant_id}", json=variant_data)
    return response.json()


# Function to delete a product
def delete_product(product_id):
    response = requests.delete(f"http://127.0.0.1:5000/products/{product_id}")
    return response.json()


# Main function
def main():
    st.title("Product Management System")

    menu_selection = st.sidebar.radio("Select:", ["View Products", "Add Product", "Delete Product"])

    if menu_selection == "View Products":
        st.header("View Products")
        products = get_products()
        if products:
            product_names = [product["name"] for product in products]
            selected_product_name = st.selectbox("Select a product:", product_names)
            selected_product = next((product for product in products if product["name"] == selected_product_name), None)
            if selected_product:
                st.write("### Product Details:")
                st.write(selected_product)
            else:
                st.write("Product not found.")
        else:
            st.write("No products found.")

    elif menu_selection == "Add Product":
        st.header("Add Product")
        st.subheader("Enter Product JSON:")
        product_json = st.text_area("Product JSON")

        if st.button("Add"):
            try:
                new_product = json.loads(product_json)
                response = add_product(new_product)
                st.write(response)
            except json.JSONDecodeError as e:
                st.error("Invalid JSON format. Please enter valid JSON data.")
        else:
            print("nONE")

    elif menu_selection == "Delete Product":
        st.header("Delete Product")
        product_id = st.text_input("Product ID")

        if st.button("Delete"):
            response = delete_product(product_id)
            st.write(response)


if __name__ == "__main__":
    main()
