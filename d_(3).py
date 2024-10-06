# -*- coding: utf-8 -*-
"""D.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1eNE7L1x4c0Klkvh1kIC9gKY4C2dqohfc
"""

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
# You should place the dataset in the same directory or specify the correct path
@st.cache
def load_data():
    return pd.read_csv("D:\\MBA materials\\Trimester 1\\DEVP(AMitra)\\Imports_Exports_Dataset.csv").sample(n=3001, random_state=55022)

df = load_data()

# Page title
st.title("Global Trade Insights Dashboard")
st.markdown("### A comprehensive dashboard providing insights into global imports and exports.")

# Sidebar with options for each analysis
st.sidebar.title("Problem Statements")
options = st.sidebar.selectbox("Select the analysis you want to view:", (
    'Transaction Value Distribution by Country (Top 10)',
    'Correlation Between Quantity and Transaction Value',
    'Shipping Method Comparison by Transaction Value',
    'Top Products by Transaction Value',
    'Top Suppliers Performance by Transaction Value',
    'Import vs Export Revenue Share',
    'Top 10 Transaction Volume by Port',
    'Weight vs Transaction Value',
    'Payment Terms Distribution by Country',
    'Top 5 Customers by Transaction Value'))

# 1. Transaction Value Distribution by Country (Top 10)
if options == 'Transaction Value Distribution by Country (Top 10)':
    st.subheader('Top 10 Countries by Transaction Value')
    top_countries = df.groupby('Country')['Value'].sum().nlargest(10)

    fig, ax = plt.subplots(figsize=(10, 6))
    sns.barplot(x=top_countries.index, y=top_countries.values, palette='Set2', ax=ax)
    ax.set_title('Top 10 Countries by Transaction Value')
    ax.set_xlabel('Country')
    ax.set_ylabel('Total Transaction Value')
    plt.xticks(rotation=45)
    st.pyplot(fig)

# 2. Correlation Between Quantity and Transaction Value
elif options == 'Correlation Between Quantity and Transaction Value':
    st.subheader('Correlation Between Quantity and Transaction Value')
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.scatter(df['Quantity'], df['Value'], color='orange', label='Quantity vs Value')
    ax.set_title('Correlation Between Quantity and Transaction Value')
    ax.set_xlabel('Quantity')
    ax.set_ylabel('Transaction Value')
    ax.grid(True)
    st.pyplot(fig)

# 3. Shipping Method Comparison by Transaction Value
elif options == 'Shipping Method Comparison by Transaction Value':
    st.subheader('Shipping Method Impact on Transaction Value')
    shipping_agg = df.groupby('Shipping_Method')['Value'].sum()

    fig, ax = plt.subplots(figsize=(10, 6))
    sns.barplot(x=shipping_agg.index, y=shipping_agg.values, palette='Dark2', ax=ax)
    ax.set_title('Shipping Method Impact on Transaction Value')
    ax.set_xlabel('Shipping Method')
    ax.set_ylabel('Total Transaction Value')
    st.pyplot(fig)

# 4. Top Products by Transaction Value
elif options == 'Top Products by Transaction Value':
    st.subheader('Top 5 Products by Transaction Value')
    top_products = df.groupby('Product')['Value'].sum().nlargest(5)

    fig, ax = plt.subplots(figsize=(10, 6))
    sns.barplot(y=top_products.index, x=top_products.values, palette='Paired', ax=ax)
    ax.set_title('Top 5 Products by Transaction Value')
    ax.set_xlabel('Total Transaction Value')
    ax.set_ylabel('Product')
    st.pyplot(fig)

# 5. Top Suppliers Performance by Transaction Value
elif options == 'Top Suppliers Performance by Transaction Value':
    st.subheader('Top 10 Suppliers by Transaction Value')
    top_suppliers = df.groupby('Supplier')['Value'].sum().nlargest(10)

    fig, ax = plt.subplots(figsize=(10, 6))
    sns.barplot(x=top_suppliers.index, y=top_suppliers.values, palette='Set3', ax=ax)
    ax.set_title('Top 10 Suppliers by Transaction Value')
    ax.set_xlabel('Supplier')
    ax.set_ylabel('Total Transaction Value')
    plt.xticks(rotation=45)
    st.pyplot(fig)

# 6. Import vs Export Revenue Share
elif options == 'Import vs Export Revenue Share':
    st.subheader('Import vs Export Revenue Share')
    import_export_agg = df.groupby('Import_Export')['Value'].sum()

    fig, ax = plt.subplots(figsize=(8, 8))
    ax.pie(import_export_agg, labels=import_export_agg.index, autopct='%1.1f%%', startangle=140,
           colors=sns.color_palette('husl', len(import_export_agg)), explode=[0.05, 0.05], shadow=True)
    ax.set_title('Import vs Export Revenue Share')
    st.pyplot(fig)

# 7. Top 10 Transaction Volume by Port
elif options == 'Top 10 Transaction Volume by Port':
    st.subheader('Top 10 Transaction Volume by Port')
    port_agg = df.groupby('Port')['Transaction_ID'].count().nlargest(10)

    fig, ax = plt.subplots(figsize=(10, 6))
    sns.barplot(x=port_agg.index, y=port_agg.values, palette='Set1', ax=ax)
    ax.set_title('Top 10 Transaction Volume by Port')
    ax.set_xlabel('Port')
    ax.set_ylabel('Number of Transactions')
    plt.xticks(rotation=45)
    st.pyplot(fig)

# 8. Weight vs Transaction Value
elif options == 'Weight vs Transaction Value':
    st.subheader('Weight vs Transaction Value')
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.scatter(df['Weight'], df['Value'], color='purple', label='Weight vs Value')
    ax.set_title('Weight vs Transaction Value')
    ax.set_xlabel('Weight')
    ax.set_ylabel('Transaction Value')
    ax.grid(True)
    st.pyplot(fig)

# 9. Payment Terms Distribution by Country
elif options == 'Payment Terms Distribution by Country':
    st.subheader('Payment Terms Distribution by Country')
    payment_terms_count = df['Payment_Terms'].value_counts().sort_index()

    fig, ax = plt.subplots(figsize=(10, 6))
    bars = ax.bar(payment_terms_count.index, payment_terms_count.values, color=sns.color_palette("viridis", len(payment_terms_count)))

    for bar in bars:
        yval = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2, yval + 0.1, int(yval), ha='center', va='bottom', fontsize=12)
    ax.set_title('Count of Countries by Payment Terms')
    ax.set_xlabel('Payment Terms (Days)')
    ax.set_ylabel('Count of Countries')
    st.pyplot(fig)

# 10. Top 5 Customers by Transaction Value
elif options == 'Top 5 Customers by Transaction Value':
    st.subheader('Top 5 Customers by Transaction Value')
    top_customers = df.groupby('Customer')['Value'].sum().nlargest(5)

    fig, ax = plt.subplots(figsize=(10, 6))
    sns.barplot(y=top_customers.index, x=top_customers.values, palette='Blues', ax=ax)
    ax.set_title('Top 5 Customers by Transaction Value')
    ax.set_xlabel('Total Transaction Value')
    ax.set_ylabel('Customer')
    st.pyplot(fig)

# Footer for extra customization
st.sidebar.markdown("### About")
st.sidebar.info("This dashboard is built to provide insights into global trade data, showcasing trends in imports and exports.")