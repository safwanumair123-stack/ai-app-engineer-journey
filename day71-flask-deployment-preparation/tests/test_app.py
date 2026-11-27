# Day 69 — Automated tests for the Enquiry Tracker

import gc
import os
import sqlite3
import tempfile

import pytest

import app as app_module


@pytest.fixture
def client():
    database_file_descriptor, database_path = tempfile.mkstemp(suffix=".db")

    os.close(database_file_descriptor)

    app_module.DATABASE_FILE = database_path

    app_module.app.config["TESTING"] = True

    app_module.create_database_tables()

    with app_module.app.test_client() as client:
        with client.session_transaction() as session:
            session.clear()

        yield client

    gc.collect()

    try:
        os.remove(database_path)

    except PermissionError:
        pass


def register_user(client, full_name, email, password):
    return client.post(
        "/register",
        data={
            "full-name": full_name,
            "email": email,
            "password": password,
            "confirm-password": password
        },
        follow_redirects=True
    )


def login_user(client, email, password):
    return client.post(
        "/login",
        data={
            "email": email,
            "password": password
        },
        follow_redirects=True
    )


def create_enquiry(client, customer_name, customer_email, customer_phone, estimated_value):
    return client.post(
        "/create-enquiry",
        data={
            "customer-name": customer_name,
            "customer-email": customer_email,
            "customer-phone": customer_phone,
            "enquiry-type": "Quotation",
            "priority": "High",
            "assigned-to": "Safwan",
            "enquiry-source": "Website",
            "estimated-value": estimated_value,
            "follow-up-date": "2030-01-01",
            "enquiry-details": "Need a quotation for website design",
            "next-action": "Send quotation by Friday"
        },
        follow_redirects=True
    )


def get_latest_enquiry_reference_number(database_path, user_email):
    connection = sqlite3.connect(database_path)
    connection.row_factory = sqlite3.Row

    enquiry = connection.execute(
        "SELECT reference_number FROM enquiries WHERE user_id = (SELECT id FROM users WHERE email = ?) ORDER BY id DESC LIMIT 1",
        (user_email,)
    ).fetchone()

    connection.close()

    return enquiry["reference_number"]


def test_first_registered_user_becomes_admin(client):
    response = register_user(
        client,
        "Safwan Umair",
        "safwan@example.com",
        "StrongPass123"
    )

    assert response.status_code == 200
    assert b"Account created successfully" in response.data

    connection = sqlite3.connect(app_module.DATABASE_FILE)
    connection.row_factory = sqlite3.Row

    user = connection.execute(
        "SELECT role FROM users WHERE email = ?",
        ("safwan@example.com",)
    ).fetchone()

    connection.close()

    assert user["role"] == "admin"


def test_second_registered_user_becomes_regular_user(client):
    register_user(
        client,
        "Safwan Umair",
        "safwan@example.com",
        "StrongPass123"
    )

    register_user(
        client,
        "Ali Khan",
        "ali@example.com",
        "AliPass123"
    )

    connection = sqlite3.connect(app_module.DATABASE_FILE)
    connection.row_factory = sqlite3.Row

    admin_user = connection.execute(
        "SELECT role FROM users WHERE email = ?",
        ("safwan@example.com",)
    ).fetchone()

    regular_user = connection.execute(
        "SELECT role FROM users WHERE email = ?",
        ("ali@example.com",)
    ).fetchone()

    connection.close()

    assert admin_user["role"] == "admin"
    assert regular_user["role"] == "user"


def test_user_can_log_in(client):
    register_user(
        client,
        "Safwan Umair",
        "safwan@example.com",
        "StrongPass123"
    )

    response = login_user(
        client,
        "safwan@example.com",
        "StrongPass123"
    )

    assert response.status_code == 200
    assert b"Welcome, Safwan Umair." in response.data
    assert b"Role:" in response.data
    assert b"admin" in response.data


def test_enquiry_routes_are_protected(client):
    response = client.get("/")

    assert response.status_code == 302


def test_logged_in_user_can_create_enquiry(client):
    register_user(
        client,
        "Safwan Umair",
        "safwan@example.com",
        "StrongPass123"
    )

    login_user(
        client,
        "safwan@example.com",
        "StrongPass123"
    )

    response = create_enquiry(
        client,
        "Ahmed Traders",
        "ahmed@example.com",
        "+92 300 1234567",
        "5000"
    )

    assert response.status_code == 200
    assert b"Enquiry created successfully" in response.data
    assert b"Ahmed Traders" in response.data


def test_user_can_edit_enquiry(client):
    register_user(
        client,
        "Safwan Umair",
        "safwan@example.com",
        "StrongPass123"
    )

    login_user(
        client,
        "safwan@example.com",
        "StrongPass123"
    )

    create_enquiry(
        client,
        "Ahmed Traders",
        "ahmed@example.com",
        "+92 300 1234567",
        "5000"
    )

    reference_number = get_latest_enquiry_reference_number(
        app_module.DATABASE_FILE,
        "safwan@example.com"
    )

    response = client.post(
        "/edit-enquiry/" + reference_number,
        data={
            "customer-name": "Ahmed Traders",
            "customer-email": "ahmed@example.com",
            "customer-phone": "+92 300 1234567",
            "enquiry-type": "Quotation",
            "priority": "High",
            "status": "In progress",
            "assigned-to": "Safwan",
            "enquiry-source": "Website",
            "estimated-value": "7500",
            "follow-up-date": "2030-01-01",
            "enquiry-details": "Need a quotation for website design",
            "next-action": "Send quotation by Friday"
        },
        follow_redirects=True
    )

    assert response.status_code == 200
    assert b"Enquiry updated successfully" in response.data
    assert b"7500.0" in response.data


def test_user_can_add_note(client):
    register_user(
        client,
        "Safwan Umair",
        "safwan@example.com",
        "StrongPass123"
    )

    login_user(
        client,
        "safwan@example.com",
        "StrongPass123"
    )

    create_enquiry(
        client,
        "Ahmed Traders",
        "ahmed@example.com",
        "+92 300 1234567",
        "5000"
    )

    reference_number = get_latest_enquiry_reference_number(
        app_module.DATABASE_FILE,
        "safwan@example.com"
    )

    response = client.post(
        "/add-note/" + reference_number,
        data={
            "note-text": "Called customer. They will respond by Friday."
        },
        follow_redirects=True
    )

    assert response.status_code == 200
    assert b"Note added successfully" in response.data
    assert b"Called customer. They will respond by Friday." in response.data


def test_user_can_delete_enquiry(client):
    register_user(
        client,
        "Safwan Umair",
        "safwan@example.com",
        "StrongPass123"
    )

    login_user(
        client,
        "safwan@example.com",
        "StrongPass123"
    )

    create_enquiry(
        client,
        "Ahmed Traders",
        "ahmed@example.com",
        "+92 300 1234567",
        "5000"
    )

    reference_number = get_latest_enquiry_reference_number(
        app_module.DATABASE_FILE,
        "safwan@example.com"
    )

    response = client.post(
        "/delete-enquiry/" + reference_number,
        follow_redirects=True
    )

    assert response.status_code == 200
    assert b"Enquiry " + reference_number.encode() + b" deleted successfully." in response.data
    assert b"Showing 0 of 0 enquiries." in response.data


def test_regular_user_cannot_access_admin_dashboard(client):
    register_user(
        client,
        "Safwan Umair",
        "safwan@example.com",
        "StrongPass123"
    )

    register_user(
        client,
        "Ali Khan",
        "ali@example.com",
        "AliPass123"
    )

    login_user(
        client,
        "ali@example.com",
        "AliPass123"
    )

    response = client.get("/admin")

    assert response.status_code == 200
    assert b"You do not have permission to access the admin dashboard." in response.data


def test_admin_can_access_admin_dashboard(client):
    register_user(
        client,
        "Safwan Umair",
        "safwan@example.com",
        "StrongPass123"
    )

    login_user(
        client,
        "safwan@example.com",
        "StrongPass123"
    )

    response = client.get("/admin")

    assert response.status_code == 200
    assert b"Admin Dashboard" in response.data
    assert b"All users" in response.data
    assert b"All enquiries" in response.data