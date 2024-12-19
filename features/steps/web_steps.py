# features/steps/web_steps.py
from behave import when, then
from flask import json
from service import app

@when('I request the product with id {id}')
def step_impl(context, id):
    response = context.client.get(f'/products/{id}')
    context.response = response

@when('I update the product with id {id} with the name "{name}"')
def step_impl(context, id, name):
    data = {"name": name}
    response = context.client.put(f'/products/{id}', json=data)
    context.response = response

@when('I delete the product with id {id}')
def step_impl(context, id):
    response = context.client.delete(f'/products/{id}')
    context.response = response

@when('I request all products')
def step_impl(context):
    response = context.client.get('/products')
    context.response = response

@when('I search for products with name "{name}"')
def step_impl(context, name):
    response = context.client.get(f'/products?name={name}')
    context.response = response

@when('I search for products with category "{category}"')
def step_impl(context, category):
    response = context.client.get(f'/products?category={category}')
    context.response = response

@when('I search for products with availability "{available}"')
def step_impl(context, available):
    response = context.client.get(f'/products?available={available}')
    context.response = response

@then('the response should be {status_code}')
def step_impl(context, status_code):
    assert context.response.status_code == int(status_code)