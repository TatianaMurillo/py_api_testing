import pytest
import logging as logger
from py_api_test.src.utilities.GenericUtility import generate_randon_email_and_password
from py_api_test.src.dao.CustomerDAO import CustomerDAO
from py_api_test.src.helpers.customer_helper import CustomerHelper


@pytest.mark.tcid01
def test_create_customer_only_email_password():
    logger.info("TEST: Create new customer with email and password only")

    rand_info = generate_randon_email_and_password()
    email = rand_info['email']
    password = rand_info['password']

    cust_obj = CustomerHelper()

    cust_api_info = cust_obj.create_customer(email=email, password=password, expected_status_code=201)

    assert cust_api_info['email'] == email, f"Create customer api return wrong email. Email: {email}"
    assert cust_api_info['first_name'] == '', f"Create customer api returned value for first_name"\
                                              f"but it should be empty. "

    cust_dao = CustomerDAO()
    cust_db_info = cust_dao.get_customer_by_email(email)

    assert cust_db_info[0]['user_email'] == email, f"Create customer api return wrong email. Email: {email}"

    id_in_api = cust_api_info['id']
    id_in_db = cust_db_info[0]['ID']
    assert id_in_api == id_in_db, f'Create customer response "id" not same as "ID" in database.'\
                                  f'Email: {email}'



