from fastapi import FastApi

api = FastApi()

api.get("/planets")


def planets():
    return "hello"


api.get("/")


def x():
    return "xyz"
