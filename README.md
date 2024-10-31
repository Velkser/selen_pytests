# Automated Web Testing with Pytest and Selenium

## Project Description

This project is designed for automating the testing of web applications using **Selenium WebDriver** and **Pytest**. The tests cover functionalities of the main page, product pages, and login forms, including verification of forms, buttons, and links.

The project supports testing for both guest users and registered users, and includes parameterized tests for validating the shopping cart functionality across different product pages.

## Installation and Setup

### Step 1: Clone the repository

```bash
git clone https://github.com/username/repository_name.git
cd repository_name
```
### Step 2: Install dependencies

Make sure you have Python 3.7+ and `pip` installed. Install the required dependencies from the `requirements.txt` file:
```bash
pip install -r requirements.txt
```
### Step 3: Set up WebDriver
To work with Selenium, you need to download the appropriate WebDriver for your browser. For example, for Chrome:

Download ChromeDriver
Make sure the WebDriver is added to your system's environment variables.

## Running Tests
### Basic Commands

Run all tests:
```bash
pytest
```

Run tests with the main_page marker:
```bash
pytest -m main_page
```

Run a specific test:
```bash
pytest path/to/test_file.py::TestClass::test_name
```

### Parameterized Tests
The tests use parameterization to check different products in the catalog:

```python
@pytest.mark.parametrize("book", [
    "hacking-exposed-wireless_208",
    "coders-at-work_207",
    pytest.param("visual-guide-to-lock-picking_206", marks=pytest.mark.xfail),
    ...
])
```

This makes it easy to add new scenarios for testing different products.

## Project Structure
```plaintext
.
├── pages/
│   ├── main_page.py        # Classes and methods for the main page
│   ├── login_page.py       # Classes and methods for the login page
│   └── product_page.py     # Classes and methods for the product page
├── tests/
│   ├── test_main_page.py   # Tests for the main page
├── conftest.py             # Fixtures for the tests
└── requirements.txt        # Project dependencies
```


## Test Examples

Main page test for guest users:
Verifies that a guest user can navigate to the login page.

```python
def test_guest_can_go_to_login_link_on_main_page(self, browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()
    page.go_to_login_page()
```

Parameterized test for adding products to the cart:
Verifies that different books can be added to the shopping cart.

```python
@pytest.mark.parametrize("book", ["book_1", "book_2"])
def test_guest_can_use_add_btn(browser, book):
    link = f"http://selenium1py.pythonanywhere.com/en-gb/catalogue/{book}/"
    page = ProductPage(browser, link)
    page.open()
    page.click_add_to_basket()
```

## Contact
If you have any questions or suggestions, feel free to reach out via email: `vielkinserhii@gmail.com`.


