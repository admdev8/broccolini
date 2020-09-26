#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Provide non secret data here for all tests.

Give data in various forms to the test functions.
"""
import random
import shortuuid
import pytest
from faker import Faker


@pytest.fixture(scope="session")
def return_random_uuid():
    """Provide random values."""
    return f"conftest_{shortuuid.uuid()}"


# account_sid = TestTwilioFunctions.get_test_values(return_data_dict["twilio_account_sid"])
#         auth_token = TestTwilioFunctions.get_test_values(return_data_dict["twilio_path_auth_token"])


@pytest.fixture()
def return_data_dict():
    """Provide dictionary values to functions."""
    input_dict = dict(
        github_token="GITHUB_TOKEN_FROM_CONFTEST",
        vault_url="VAULT_URL_FROM_CONFTEST",
        secret_path="python_rising/dev/path1conftest",
        secret=dict(secret_test_key="secret_value_from_conftest"),
        twilio_auth_token="python_rising/dev/twilio_data/TWILIO_AUTH_TOKEN",
        twilio_account_sid="python_rising/dev/twilio_data/TWILIO_ACCOUNT_SID",
        twilio_notification_number="python_rising/dev/twilio_data/TWILIO_NOTIFICATION_NUMBER",
        twilio_phone_number="python_rising/dev/twilio_data/TWILIO_PHONE_NUMBER",
        written_directories=["dir_test1", "dir_test2", "dir_test3"],
        valid_json_file_name="json_file_from_conftest.json",
        faker_files=r"./tests/fake_data_from_conftest/training",
        output_file_name=r"./tests/__output_files/output_json_files.json",
        input_directory_path=r"",
        fauna_secret_path_admin="python_rising/dev/faunadb/admin/api_token",
        fauna_test_data=r"string formatted test data from conftest",
        fauna_secret_path_server="python_rising/dev/faunadb/pythonrising_dev/server/api_token",
        fauna_collection_name_for_delete="collection_name_used_for_delete_test",
        fauna_test_bad_database=r"bad_database",
    )
    return input_dict


@pytest.fixture
def return_a_list():
    """Function returns list values."""
    input_list = [
        {
            "api_version": "v1alpha1",
            "directorate_name": "directname",
            "project_name": "PROJNAMEHERE",
            "target_revision": "master",
        },
        {
            "file1_name": "file_to_be_copied_created_by_conftest.txt",
            "file2_name": "file2_to_be_copied_created_by_conftest.txt",
        },
        {
            "api_version": "v1alpha2",
            "directorate_name": "adsfdssd2",
            "project_name": "PROJNAMEHERE2",
            "target_revision": "targetrev",
        },
    ]
    return input_list


@pytest.fixture
def create_generic_json_test_file(tmpdir_factory):
    """create a generic test directory."""
    folder_name = "generic_test_directory_json"
    file_name = "generic_file_name_json.json"
    a_dir = tmpdir_factory.mktemp(folder_name)
    a_file = a_dir.join(file_name)
    return a_file


@pytest.fixture
def create_dir_to_simulate_json_bulk_load_orig(tmpdir_factory):
    """Create a directory with json files in it."""
    json_string = """
        {
        "website": "website_from_conftest",
        "topic": "json and python",
        "year": 2019,
        "list": [10, 20, 30]
    }
    """
    folder_name = "folder_with_sample_json"
    file_name = "json_vault_test_data.json"
    a_dir = tmpdir_factory.mktemp(folder_name)
    a_file = a_dir.join(file_name)

    with open(a_file, "w") as file_p:
        file_p.write(json_string)
    return a_file


@pytest.fixture(scope="session")
def create_list_of_filenames_and_directories(tmpdir_factory):
    """Create a list of directories and files from various choices."""
    base_file_name = "test_dir_created/training/"
    # base_file_name = "training/"
    test_dir_name = tmpdir_factory.mktemp("test_dir_created")
    # test_dir_name = tmpdir_factory.mktemp(base_file_name)
    # test_dir_name = tmpdir_factory.mktemp()
    # print(f"testdirname {test_dir_name}")
    fake = Faker("en_US")
    # base_file_name = "training/"
    folder_list = ["python", "javascript", "network", "ml_ai"]
    sub_directory_name_list = ["subdir_1", "subdir_2", "subdir_3"]
    folder_type = random.choice(folder_list)
    full_path = base_file_name + folder_type + "/" + fake.file_name(extension="txt", category="office")
    file_path_and_name_list = []
    for _ in range(5):
        folder_type = random.choice(folder_list)
        subdirectory = random.choice(sub_directory_name_list)
        full_path = base_file_name + folder_type + "/" + fake.file_name(extension="txt", category="office")
        full_path_subdir = (
            base_file_name + folder_type + "/" + subdirectory + "/" + fake.file_name(extension="txt", category="office")
        )
        file_path_and_name_list.append(full_path)
        file_path_and_name_list.append(full_path_subdir)
    # return file_path_and_name_list
    # list_of_directories = []
    full_path_including_file = []
    for each in file_path_and_name_list:
        directory_and_path = str(test_dir_name) + "/" + each
        full_path_including_file.append(directory_and_path)
    return full_path_including_file, test_dir_name
