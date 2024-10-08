# Product Stock Manager

## Overview

The Inventory Management System is a simple command-line application built in Python that allows users to manage a list of products. It serves as an exercise for learning Object-Oriented Programming (OOP) concepts and file handling in Python. The application can be used as a foundational project for understanding inventory management systems and can also serve as a showcase in a resume.

## Features

- Add new products to the inventory
- Remove products from the inventory
- Search for products based on their names
- Display all products in the inventory
- Update product details (this feature is currently in development)
- Automatically saves inventory data to a text file

## Getting Started

### Prerequisites

- Python 3.x installed on your machine.

### Installation

1. Clone the repository or download the code files.
2. Navigate to the project directory in your terminal.
3. Ensure that you have an `inventario.txt` file in the project directory (the application will create one if it does not exist).

### Running the Application

1. Open your terminal.
2. Navigate to the directory where the code is saved.
3. Run the following command:

   ```bash
   python <filename>.py
   ```

   Replace `<filename>` with the actual name of the file.

### Application Flow
Once the program is running, you will see a menu with the following options:

1. Add Product:

- You will be prompted to enter the product's name, category, price, and quantity.
- The product will be added to the inventory, and the inventory will be saved to the file.

2. Remove Product:

- You will be shown a list of existing products and asked to enter the name of the product you want to remove.
- If the product exists, it will be removed from the inventory, and the inventory will be saved.

3. Search Product:

- You can search for a product by entering its name. The program will display matching products.

4. Show Inventory:

- This option displays all the products currently in the inventory in a formatted table.

5. Update Product:

- This feature will allow users to modify the details of existing products in the inventory.

6. Exit:

- Exiting the program will automatically save the current state of the inventory to the `inventario.txt` file.

### Important Notes

- The inventory data is stored in a plain text file named `inventario.txt`. Ensure that this file remains in the same directory as the application.
- The program handles invalid inputs gracefully, prompting the user to enter valid values when necessary.
- If the application is closed unexpectedly, it will save the current state of the inventory upon catching the exit signal.

### Conclusion

This Inventory Management System is a practical project that demonstrates basic principles of programming, including data management, user input validation, and file handling. It can be extended and modified to include more features, making it an excellent starting point for those interested in building more complex applications.

Feel free to explore the code and suggest improvements or additional features!