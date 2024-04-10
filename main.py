import streamlit as st
import requests

BASE_URL = 'http://127.0.0.1:5000'

# Streamlit UI
def view_all_details():
    st.title("All Products Details")
    response = requests.get(BASE_URL + "/products")
    if response.status_code == 200:
        products = response.json()
        for product in products:
            st.write(product)
    else:
        st.error("Failed to fetch products")

def add_data():
    st.title("Add New Product")
    product_data = st.text_area("Enter product data in JSON format")
    if st.button("Add"):
        try:
            product = eval(product_data)
            response = requests.post(BASE_URL + "/products", json=product)
            if response.status_code == 200:
                st.success("Product added successfully")
            else:
                st.success("Product added successfully")
        except Exception as e:
            st.error("Invalid JSON format")

def delete_section():
    st.title("Delete Product")
    product_id = st.text_input("Enter Product ID")
    if st.button("Delete"):
        response = requests.delete(BASE_URL + f"/products/{product_id}")
        if response.status_code == 200:
            st.success("Product deleted successfully")
        else:
            st.error("Failed to delete product")

def update_fields_section():
    st.title("Update Product")
    product_id = st.text_input("Enter Product ID")
    updated_product_data = st.text_area("Enter updated product data in JSON format")
    if st.button("Update"):
        try:
            updated_product = eval(updated_product_data)
            response = requests.put(BASE_URL + f"/products/{product_id}", json=updated_product)
            if response.status_code == 200:
                st.success("Product updated successfully")
            else:
                st.error("Failed to update product")
        except Exception as e:
            st.error("Invalid JSON format")

# Main Streamlit UI
def main():
    st.sidebar.title("Navigation")
    nav_item = st.sidebar.radio("", ["View All Products", "Add Product", "Delete Product", "Update Product"])

    if nav_item == "View All Products":
        view_all_details()
    elif nav_item == "Add Product":
        add_data()
    elif nav_item == "Delete Product":
        delete_section()
    elif nav_item == "Update Product":
        update_fields_section()

if __name__ == "__main__":
    main()
