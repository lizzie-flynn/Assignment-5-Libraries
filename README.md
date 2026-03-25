# DATA 4000 – Assignment 5

## Installation

Install required library:

pip install requests

## How to Run

From the terminal:

python pos_checkout.py
python inventory_spotcheck.py

## Example Run – POS Checkout

Student key: abc123  
Item name: Shirt  
Unit price: 25  
Quantity: 2  
Item name: DONE  

Seed: 444  
Units: 2  
Subtotal: $50.00  
Discount: 0%  
Perk applied: NO  
Total: $50.00  

## Example Run – Inventory Spotcheck

Student key: abc123  
SKU: A100  
On hand: 5  
SKU: DONE  

Seed: 444  
Threshold: 12  
SKUs entered: 1  
Reorder flagged: 1  
Spotcheck term: weezer  
Songs returned: 5  
API status: OK  