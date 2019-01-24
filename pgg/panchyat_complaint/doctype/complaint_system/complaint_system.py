# -*- coding: utf-8 -*-
# Copyright (c) 2019, sagmin solution and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document
from frappe.handler import uploadfile

class ComplaintSystem(Document):
	pass

@frappe.whitelist()
def attach_file_to_doc():
    file_upload_response = uploadfile()
    if file_upload_response:
        return file_upload_response
    else:
        frappe.throw('Unable to upload')
