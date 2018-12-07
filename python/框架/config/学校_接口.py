#!/usr/bin/env python
# -*- coding:utf-8 -*-

import requests
import unittest
def tess(a):
    url = "http://testsupport-be.haofenshu.com/v1/schools/infos"
    canshu = {"filterInput": "{}".format(a)}
    headers = {'Cookie': "yz-test-session-id=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJvcGVyYXRvciI6ImxpeGlhbndlaSIsInJvbGVUeXBlIjoxLCJpYXQiOjE1MzkwNTgxOTYsImV4cCI6MTU3MDU5NDE5Nn0.GzWTsN7Sb9W85R1Wem8_HNV7e8oXTQSCPdvODb5f_GA"}
    response = requests.get(url=url, headers=headers, params=canshu)
    aaaa = response.json()
    print(aaaa)
    return aaaa
# tess(123)

# tess(123)
# import json
# class 学校_查询():
#     def 学校_快查(self,a):
#         url = "http://testsupport-be.haofenshu.com/v1/schools/infos"
#         canshu = {"filterInput": "{}".format(a)}
#         headers = {
#             'Cookie': "yz-test-session-id=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJvcGVyYXRvciI6ImxpeGlhbndlaSIsInJvbGVUeXBlIjoxLCJpYXQiOjE1MzkwNTgxOTYsImV4cCI6MTU3MDU5NDE5Nn0.GzWTsN7Sb9W85R1Wem8_HNV7e8oXTQSCPdvODb5f_GA"}
#         response = requests.get(url=url, headers=headers, params=canshu)
#         aaaa = response.json()
#         return aaaa