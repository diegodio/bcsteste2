import streamlit as st
from streamlit_qrcode_scanner import qrcode_scanner
import requests

qr_code = qrcode_scanner(key='qrcode_scanner')

if qr_code:
    st.write(qr_code)
    st.write(f'barcode -> {qr_code}')

barcode = qr_code
# Endpoint da API do Open Food Facts
url = f"https://world.openfoodfacts.org/api/v0/product/{barcode}.json"

# Requisição à API
response = requests.get(url)
data = response.json()

if data.get("status") == 1:  # Produto encontrado
    product = data["product"]
    st.write(f"Produto: {product.get('product_name', 'N/A')}")
    st.write(f"Marca: {product.get('brands', 'N/A')}")
    st.write(f"Categoria: {product.get('categories', 'N/A')}")
    st.write(f"Países disponíveis: {product.get('countries', 'N/A')}")
else:
    st.write("Produto não encontrado.")