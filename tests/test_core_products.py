from unittest.mock import Mock, patch
from src.core_modules.core_product import create_products, update_products, delete_products, fetch_products, view_products


# def start_testing(): 
@patch("src.core_modules.core_db.query")
def test_fetch_products(mock):
    expected = []
    actuall = fetch_products()


def test_view_products():
    
    state = {"products":[{"id":1, "product_name":"cat", "quantity":2, "price":2}]}    
    excepted = {"products":[{"id":1, "product_name":"cat", "quantity":2, "price":2}]}
    actuall = view_products
    

@patch("src.core_modules.core_db.conn")
@patch("src.core_modules.core_db.add")
@patch("pyinputplus.inputInt")
@patch("pyinputplus.inputFloat")
@patch("pyinputplus.inputStr")
def test_create_product(mock_str,mock_float,mock_int,mock_add,conn):
    
    state =[]
    mock_str.return_value = "green water"
    mock_float.return_value = 2
    mock_int.return_value= 5
    expected = []
    

    actuall = create_products(state)


@patch("src.core_modules.core_db.add")
@patch("pyinputplus.inputInt")
@patch("builtins.input")
@patch("pyinputplus.inputFloat")
@patch("pyinputplus.inputNum") 
def test_update_product(mock_num,mock_float,mock_input,mock_int,mock_add):
    
    mock_num.return_value = 0
    mock_float.return_value = 1.5
    mock_int.return_value = 4
    mock_input.return_value = "kat"
    state = {"products":[{"id":1, "product_name":"cat", "quantity":2, "price":2}]}
    expected = {"products":[{"id":1, "product_name":"cat", "quantity":2, "price":2}]}
    actuall = update_products(state)




@patch("src.core_modules.core_db.add")
@patch("pyinputplus.inputNum")
def test_delete_products(fake_input,mock_add):
    fake_input.return_value = 0
    state = {"products":[{"id":1, "product_name":"cat", "quantity":2, "price":2}]}
    
    expected = {"products":[{"id":1, "product_name":"cat", "quantity":2, "price":2}]}
    actuall = delete_products(state)

        
# if __name__ == '__main__':
#     start_testing()
